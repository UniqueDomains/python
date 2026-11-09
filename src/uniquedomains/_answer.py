"""What a call answers: the body and the facts its headers carry."""

from __future__ import annotations

from collections.abc import Callable
from functools import cached_property
from typing import Any, Generic, TypeVar

import httpx

from ._errors import AnswerShapeError
from ._headers import Quota, RateLimit, parse_quota, parse_rate_limit, parse_retry_after

E = TypeVar("E")
D = TypeVar("D")

__all__ = ["Answer", "TextAnswer"]


class _Facts:
    """The facts every answer carries, read from its status and headers."""

    def __init__(self, response: httpx.Response) -> None:
        self.status: int = response.status_code
        self.headers: httpx.Headers = response.headers
        self.etag: str | None = response.headers.get("etag")
        """Pass it back as ``if_none_match`` to ``Client.request``: an unchanged answer comes back as a 304."""
        self.quota: Quota | None = parse_quota(response.headers)
        self.rate_limit: RateLimit | None = parse_rate_limit(response.headers)
        self.retry_after: float | None = parse_retry_after(response.headers)
        self.location: str | None = response.headers.get("location")
        """On a 202: where the answer will be."""


class Answer(_Facts, Generic[E, D]):
    """A JSON answer: the ``{data, meta, links}`` envelope and the header facts.

    From a typed method (``ud.names.get_name(...)``), ``body`` is the envelope as the generated model and ``data`` its
    ``data`` member, both typed. From ``Client.request``, ``body`` is the decoded JSON and ``data`` its ``data`` member.
    ``json`` is always the decoded JSON. On a 304 (``not_modified``), there is no body.
    """

    def __init__(
        self, response: httpx.Response, json: dict[str, Any] | None, parse: Callable[[], E] | None = None
    ) -> None:
        super().__init__(response)
        self.not_modified: bool = response.status_code == 304
        self.json: dict[str, Any] | None = json
        self._parse = parse

    def __repr__(self) -> str:
        return f"Answer(status={self.status}, not_modified={self.not_modified})"

    @cached_property
    def body(self) -> E:
        """The envelope: the generated model for a typed method, the decoded JSON for ``Client.request``."""
        if self.json is None:
            raise AttributeError("A 304 answer has no body: keep the one you read with this ETag.")
        if self._parse is None:
            return self.json  # type: ignore[return-value]
        try:
            parsed = self._parse()
        except (KeyError, TypeError, ValueError, AttributeError) as error:
            raise AnswerShapeError(
                f"The answer's envelope does not fit this version's models ({error!r}). Read answer.json, or update the package."
            ) from error
        # A status the operation does not declare parses to None, and a problem model has no `data`: neither is the
        # envelope this method promises (review R3-9).
        if parsed is None or not hasattr(parsed, "data"):
            raise AnswerShapeError(
                f"The answer ({self.status}) is not an envelope this version's models declare. Read answer.json."
            )
        return parsed

    @property
    def data(self) -> D:
        """The envelope's ``data``."""
        body = self.body
        if isinstance(body, dict):
            return body.get("data")  # type: ignore[return-value]
        return body.data  # type: ignore[attr-defined, no-any-return]

    @property
    def meta(self) -> dict[str, Any]:
        """The envelope's ``meta`` as decoded JSON (``asOf``, ``cursor``, ``limit``)."""
        return dict((self.json or {}).get("meta") or {})

    @property
    def links(self) -> dict[str, Any]:
        """The envelope's ``links`` as decoded JSON (``self``, ``next``, ``register``, ``product``, ``dataset``)."""
        return dict((self.json or {}).get("links") or {})

    @property
    def cursor(self) -> str | None:
        """The next page's cursor, when there is one."""
        cursor = self.meta.get("cursor")
        return cursor if isinstance(cursor, str) and cursor else None


class TextAnswer(_Facts):
    """A file answer: the OpenAPI document, ``llms.txt``, a calendar, or a ``.csv`` form. On a 304, ``text`` is None."""

    def __init__(self, response: httpx.Response) -> None:
        super().__init__(response)
        self.not_modified: bool = response.status_code == 304
        self.text: str | None = None if self.not_modified else response.text
        self.content_type: str | None = response.headers.get("content-type")

    def __repr__(self) -> str:
        return f"TextAnswer(status={self.status}, content_type={self.content_type!r})"
