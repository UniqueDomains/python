"""The client.

Three ways in: no key (the free grade), a member key (``Authorization: Bearer``), or a RapidAPI key with its listing
(the listing's own host, ``X-RapidAPI-Key`` and ``X-RapidAPI-Host``). Every answer that is not a success raises an
``ApiProblemError``; a call the RapidAPI listing does not serve raises ``ListingMismatchError`` before any request.

Two surfaces over one sending path:

- the typed methods, one class per tag, one method per operation (``ud.names.get_name("get.plumbing")``), built on the
  modules ``openapi-python-client`` generated: their request builders and their models;
- ``request(operation_id, ...)``, the generic path for tools and loops, which also carries the ``.csv`` forms and
  conditional requests (``if_none_match``), and answers the decoded JSON.

The base URL, the key and the other headers belong to this client and travel with each request: an ``httpx.Client``
passed in is never changed, so several clients can share one connection pool without mixing their keys.
"""

from __future__ import annotations

import importlib
import json
import os
import time
from collections.abc import Callable, Iterator, Mapping, Sequence
from datetime import date, datetime
from types import ModuleType
from typing import Any, Literal, NamedTuple
from urllib.parse import quote

import httpx

from ._answer import Answer, TextAnswer
from ._errors import ApiProblemError, CursorLoopError, ListingMismatchError
from ._generated.client import Client as _GeneratedClient
from ._headers import parse_retry_after
from ._listings import LISTINGS
from ._namespace_support import join_list
from ._namespaces import NamespacedClient
from ._operations import API_PUBLIC_BASE, OPERATIONS
from ._retry import Retry, resolve_retry, retry_wait
from ._version import __version__

__all__ = ["Client", "RapidApi", "find_listing", "listings_serving"]

# Without the `retry` option, the one retry the client makes on its own is a 429 `rate_limited` whose `Retry-After` is
# exactly `1` (a member key's burst limiter). Any other wait is the caller's decision, so it surfaces as the error.
_RETRY_AFTER_HEADER = "1"
_RETRY_DELAY = 1.0

# Path values the URL would resolve away (`..` climbs out of the operation's path).
_DOT_SEGMENTS = frozenset({"", ".", ".."})

_DEFAULT_TIMEOUT = httpx.Timeout(30.0, connect=10.0)


class RapidApi(NamedTuple):
    """A RapidAPI key and the listing it subscribes to (``"whois"``, ``"names"``...)."""

    key: str
    listing: str


def find_listing(listing_id: str) -> dict[str, Any] | None:
    """A RapidAPI listing by id: its ``title``, ``host`` and ``operations``."""
    return next((listing for listing in LISTINGS if listing["id"] == listing_id), None)


def listings_serving(operation_id: str) -> list[str]:
    """The listings whose RapidAPI subscription opens an operation."""
    return [listing["id"] for listing in LISTINGS if operation_id in listing["operations"]]


def _without_conditional(headers: Mapping[str, str] | None) -> dict[str, str]:
    """``If-None-Match`` comes only from ``if_none_match``, so a 304 never answers a call that did not ask for one."""
    return {name: value for name, value in (headers or {}).items() if name.lower() != "if-none-match"}


def _merge(headers: httpx.Headers, extra: Mapping[str, str] | httpx.Headers | None) -> httpx.Headers:
    """Sets each header over ``headers``, whatever the case of its name: last wins, one header never goes twice."""
    for name, value in (extra or {}).items():
        headers[name] = value
    return headers


def _query_value(value: Any) -> Any:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return value


def _json_of(response: httpx.Response) -> Any:
    """The answer's body as JSON, or None when it is not JSON."""
    try:
        return json.loads(response.text)
    except ValueError:
        return None


def _envelope(body: Any) -> dict[str, Any] | None:
    """The ``{data, meta, links}`` envelope of a 200 or 202, or None when the body is not that."""
    if (
        not isinstance(body, dict)
        or "data" not in body
        or not isinstance(body.get("meta"), dict)
        or not isinstance(body.get("links"), dict)
    ):
        return None
    return body


def _check_path_value(operation_id: str, name: str, value: Any) -> None:
    if str(value) in _DOT_SEGMENTS:
        raise ValueError(f'{operation_id}: {name} cannot be "{value}".')


class Client(NamespacedClient):
    """A client for the Unique Domains API (``https://api.unique.domains/v1``).

    Args:
        api_key: a member key (``ud_live_...``, created in the product under Settings, Account, API). Defaults to the
            ``UD_API_KEY`` environment variable; ``""`` calls without a key even when ``UD_API_KEY`` is set.
        rapidapi: a RapidAPI key and the listing it subscribes to, as ``(key, listing)`` or ``RapidApi(key, listing)``:
            calls go to that listing's host, for its operations only.
        base_url: another base URL (a local run). Defaults to the public base, or the listing's host with ``rapidapi``.
        headers: headers sent on every call (``If-None-Match`` excepted: pass ``if_none_match`` to ``request``). A
            header given here replaces the client's own of the same name, whatever its case.
        timeout: seconds, or an ``httpx.Timeout``. Defaults to 30 seconds (10 to connect), or the ``http_client``'s.
        retry: ``True`` retries what is worth retrying (see ``Retry``) up to 3 tries; a ``Retry`` sets the tries and the
            longest wait. Off by default, where the client retries once, after a ``rate_limited`` answer with
            ``Retry-After: 1``.
        user_agent: the ``User-Agent`` header. Defaults to ``uniquedomains-python/<version>``.
        http_client: an ``httpx.Client`` of your own (a proxy, a transport, a pool shared by several clients). It is
            never changed: this client sends its URL and headers with each request, over the pool's own headers.

    Redirects are followed, as a browser's ``fetch`` does. Use the client as a context manager, or call ``close()``,
    to release the connection pool (an ``http_client`` you passed stays open).
    """

    def __init__(
        self,
        api_key: str | None = None,
        rapidapi: RapidApi | tuple[str, str] | None = None,
        base_url: str | None = None,
        *,
        headers: Mapping[str, str] | None = None,
        timeout: float | httpx.Timeout | None = None,
        retry: bool | Retry = False,
        user_agent: str | None = None,
        http_client: httpx.Client | None = None,
    ) -> None:
        self.listing: dict[str, Any] | None = None
        self.auth: Literal["none", "member", "rapidapi"]
        sent = httpx.Headers({"User-Agent": user_agent or f"uniquedomains-python/{__version__}"})
        if rapidapi is not None:
            if api_key is not None:
                raise ValueError("Pass either api_key or rapidapi, not both.")
            key, listing_id = RapidApi(*rapidapi)
            listing = find_listing(listing_id)
            if listing is None:
                known = ", ".join(entry["id"] for entry in LISTINGS)
                raise ValueError(f'Unknown RapidAPI listing "{listing_id}". The listings: {known}.')
            if not key:
                raise ValueError("The RapidAPI key is empty.")
            self.listing = listing
            self.auth = "rapidapi"
            sent["X-RapidAPI-Key"] = key
            sent["X-RapidAPI-Host"] = listing["host"]
        else:
            key = (os.environ.get("UD_API_KEY") or "").strip() if api_key is None else api_key.strip()
            self.auth = "member" if key else "none"
            if key:
                sent["Authorization"] = f"Bearer {key}"
        self._headers = _merge(sent, _without_conditional(headers))

        default_base = f"https://{self.listing['host']}" if self.listing else API_PUBLIC_BASE
        self.base_url: str = (base_url or default_base).rstrip("/")
        self._retry = resolve_retry(retry)
        self._timeout: httpx.Timeout | None = (
            None if timeout is None else timeout if isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout)
        )
        self._owns_http = http_client is None
        self._http = http_client if http_client is not None else httpx.Client(timeout=_DEFAULT_TIMEOUT)
        # The generated parsers read the generated client (nothing else does); it holds the same pool, untouched.
        self._generated = _GeneratedClient(base_url=self.base_url)
        self._generated.set_httpx_client(self._http)
        self._bind_namespaces(self)

    # ------------------------------------------------------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------------------------------------------------------

    def close(self) -> None:
        """Closes the connection pool (not an ``http_client`` you passed)."""
        if self._owns_http:
            self._http.close()

    def __enter__(self) -> Client:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def __repr__(self) -> str:
        listing = f", listing={self.listing['id']!r}" if self.listing else ""
        return f"Client(base_url={self.base_url!r}, auth={self.auth!r}{listing})"

    # ------------------------------------------------------------------------------------------------------------------
    # Sending
    # ------------------------------------------------------------------------------------------------------------------

    def _operation(self, operation_id: str) -> dict[str, Any]:
        operation = OPERATIONS.get(operation_id)
        if operation is None:
            raise ValueError(f'Unknown operation "{operation_id}".')
        if self.listing is not None and operation_id not in self.listing["operations"]:
            raise ListingMismatchError(operation_id, self.listing, listings_serving(operation_id))
        return operation

    def _send_once(self, request: dict[str, Any]) -> httpx.Response:
        """One request: this client's base URL and headers, the request's own headers over them, redirects followed."""
        headers = _merge(httpx.Headers(self._headers), request.get("headers"))
        options: dict[str, Any] = {"follow_redirects": True}
        if self._timeout is not None:
            options["timeout"] = self._timeout
        return self._http.request(
            request["method"],
            self.base_url + request["url"],
            params=request.get("params"),
            json=request.get("json"),
            headers=headers,
            **options,
        )

    def _send(self, method: str, request: dict[str, Any]) -> httpx.Response:
        if self._retry is None:
            response = self._send_once(request)
            if (
                response.status_code == 429
                and response.headers.get("retry-after", "").strip() == _RETRY_AFTER_HEADER
                and isinstance(body := _json_of(response), dict)
                and body.get("code") == "rate_limited"
            ):
                time.sleep(_RETRY_DELAY)
                response = self._send_once(request)
            return response
        attempt = 0
        while True:
            try:
                response = self._send_once(request)
            except httpx.UnsupportedProtocol:
                raise  # a wrong scheme in the base URL: trying again changes nothing
            except httpx.TransportError:
                # A network failure or a timeout: tried again on a GET only.
                wait = retry_wait(self._retry, attempt, method, None, None, None)
                if wait is None:
                    raise
            else:
                if response.is_success or response.status_code == 304:
                    return response
                wait = retry_wait(
                    self._retry,
                    attempt,
                    method,
                    response.status_code,
                    parse_retry_after(response.headers),
                    _json_of(response),
                )
                if wait is None:
                    return response
            time.sleep(wait)
            attempt += 1

    def _answer(
        self, method: str, request: dict[str, Any], text: bool, parse: Callable[[httpx.Response], Any] | None = None
    ) -> Any:
        """Sends, raises on a problem, and reads the answer: a file, a 304, or the envelope."""
        response = self._send(method, request)
        if response.status_code != 304 and not response.is_success:
            raise ApiProblemError.from_response(response)
        if text:
            return TextAnswer(response)
        if response.status_code == 304:
            return Answer(response, None)
        envelope = _envelope(_json_of(response))
        if envelope is None:
            raise ApiProblemError.unreadable(response)
        return Answer(response, envelope, None if parse is None else lambda: parse(response))

    def _call(self, operation_id: str, arguments: dict[str, Any]) -> Any:
        """A typed method's call: the generated request builder, the shared sending path, the generated parser."""
        operation = self._operation(operation_id)
        for param in operation["parameters"]:
            if param["in"] == "path":
                _check_path_value(operation_id, param["arg"], arguments.get(param["arg"], ""))
        module: ModuleType = importlib.import_module(f"uniquedomains._generated.api.{operation['module']}")
        request = module._get_kwargs(**arguments)
        text = operation["answer"] == "text"
        request["headers"] = {"Accept": "*/*" if text else "application/json", **request.get("headers", {})}
        return self._answer(
            operation["method"],
            request,
            text,
            lambda response: module._parse_response(client=self._generated, response=response),
        )

    # ------------------------------------------------------------------------------------------------------------------
    # The generic path
    # ------------------------------------------------------------------------------------------------------------------

    def request(
        self,
        operation_id: str,
        *,
        path: Mapping[str, str | int] | None = None,
        query: Mapping[str, Any] | None = None,
        body: Mapping[str, Any] | None = None,
        fields: str | Sequence[str] | None = None,
        include: str | Sequence[str] | None = None,
        format: Literal["csv"] | None = None,
        if_none_match: str | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Answer[dict[str, Any], Any] | TextAnswer:
        """Calls one operation by its id: ``request("get_name", path={"name": "get.plumbing"})``.

        Answers an ``Answer`` whose ``body`` is the decoded JSON envelope, or a ``TextAnswer`` for a file answer and
        for ``format="csv"``. With ``if_none_match`` (an ``etag`` you read before), an unchanged answer comes back with
        ``not_modified`` set and no body. ``headers`` replace the client's own of the same name, whatever the case.
        """
        operation = self._operation(operation_id)
        declared = {(param["in"], param["name"]) for param in operation["parameters"]}
        path = dict(path or {})
        query = dict(query or {})
        for name in path:
            if ("path", name) not in declared:
                raise TypeError(f"{operation_id} has no path parameter {name!r}.")
        for name in query:
            if ("query", name) not in declared:
                raise TypeError(f"{operation_id} has no query parameter {name!r}.")
        for option, value in (("fields", fields), ("include", include)):
            joined = join_list(value)
            if joined is None:
                continue
            if ("query", option) not in declared:
                raise TypeError(f"{operation_id} takes no {option}.")
            query[option] = joined
        if format == "csv" and not operation["csv"]:
            raise TypeError(f"{operation_id} has no CSV form.")
        if format not in (None, "csv"):
            raise ValueError(f'format takes "csv" or None, not {format!r}.')
        if body is not None and operation["body"] is None:
            raise TypeError(f"{operation_id} takes no body.")

        url = operation["path"]
        for param in operation["parameters"]:
            if param["in"] != "path":
                continue
            if param["name"] not in path:
                raise TypeError(f"{operation_id} needs the path parameter {param['name']!r}.")
            value = str(path[param["name"]])
            _check_path_value(operation_id, param["name"], value)
            url = url.replace("{" + param["name"] + "}", quote(value, safe=""))
        if format == "csv":
            url += ".csv"
        text = format == "csv" or operation["answer"] == "text"

        sent_headers = httpx.Headers(
            {"Accept": "text/csv" if format == "csv" else "*/*" if text else "application/json"}
        )
        _merge(sent_headers, _without_conditional(headers))
        if if_none_match:
            sent_headers["If-None-Match"] = if_none_match
        params = {name: _query_value(value) for name, value in query.items() if value is not None}
        request: dict[str, Any] = {"method": operation["method"], "url": url, "params": params, "headers": sent_headers}
        if body is not None or (operation["body"] is not None and operation["body"]["required"]):
            request["json"] = dict(body or {})
        answer: Answer[dict[str, Any], Any] | TextAnswer = self._answer(operation["method"], request, text)
        return answer

    def iter_pages(
        self, operation_id: str, *, max_rows: int | None = None, **params: Any
    ) -> Iterator[Answer[dict[str, Any], Any]]:
        """Every page of a list an operation pages through with ``cursor``, each fetched when the previous one is read.

        ``params`` are ``request``'s (``path``, ``query``, ``fields``...). With ``max_rows``, the page that reaches it
        comes whole and is the last. An API that answers the cursor it was sent raises ``CursorLoopError``.
        """
        operation = self._operation(operation_id)
        if not any(param["in"] == "query" and param["name"] == "cursor" for param in operation["parameters"]):
            raise TypeError(f"{operation_id} does not page with a cursor.")
        if max_rows is not None and (not isinstance(max_rows, int) or isinstance(max_rows, bool) or max_rows < 0):
            raise ValueError(f"max_rows must be a whole number, 0 or more: {max_rows!r}.")
        if params.get("format") is not None or params.get("if_none_match") is not None:
            raise TypeError("iter_pages reads the JSON envelope: format and if_none_match are request's.")
        if max_rows == 0:
            return
        query = dict(params.pop("query", None) or {})
        seen = 0
        sent_cursor: str | None = query.get("cursor")
        while True:
            answer = self.request(operation_id, query=query, **params)
            if not isinstance(answer, Answer):
                raise TypeError(f"{operation_id} answers a file, not pages.")
            yield answer
            data = answer.data
            if isinstance(data, list):
                seen += len(data)
            cursor = answer.cursor
            if cursor is None or (max_rows is not None and seen >= max_rows):
                return
            # The same page again would loop until the caller's quota runs out.
            if cursor == sent_cursor:
                raise CursorLoopError(f"The API answered the cursor it was sent ({cursor}): the list stops here.")
            sent_cursor = cursor
            query["cursor"] = cursor

    def iter_rows(self, operation_id: str, *, max_rows: int | None = None, **params: Any) -> Iterator[Any]:
        """Every row of every page, as decoded JSON: ``for row in ud.iter_rows("list_tlds", query={"publicSet": True})``."""
        seen = 0
        for page in self.iter_pages(operation_id, max_rows=max_rows, **params):
            rows = page.data
            if not isinstance(rows, list):
                raise TypeError("This answer is a summary, not a list of rows: read it with request().")
            for row in rows:
                if max_rows is not None and seen >= max_rows:
                    return
                seen += 1
                yield row
