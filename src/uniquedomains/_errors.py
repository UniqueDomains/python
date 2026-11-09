"""The errors of the client.

``ApiProblemError`` is every answer that is not a success: the API's problem body (RFC 9457), or one built for an
answer that carried none (a proxy's page, a gateway's own refusal). ``ApiProblemError.from_response`` picks a subclass by
the problem's code, so a caller can branch with ``except RateLimitError``; a code no subclass claims, a newer API's
included, stays a plain ``ApiProblemError``.

``ListingMismatchError`` is a call the client's RapidAPI listing does not serve, raised before any request.

A network failure stays httpx's own ``httpx.TransportError``.
"""

from __future__ import annotations

import json
from typing import Any

import httpx

from ._headers import Quota, RateLimit, parse_quota, parse_rate_limit, parse_retry_after

__all__ = [
    "AnswerShapeError",
    "ApiProblemError",
    "AuthError",
    "ListingMismatchError",
    "NotFoundError",
    "NotReadyError",
    "PlanRequiredError",
    "QuotaError",
    "RateLimitError",
    "UniqueDomainsError",
    "ValidationError",
    "WordRejectedError",
]

_RAW_TEXT_LIMIT = 2000


class UniqueDomainsError(Exception):
    """The base class of every error this package raises (network failures stay httpx's own)."""


def _keep_raw(body: Any) -> Any:
    if isinstance(body, dict):
        return dict(body)
    if isinstance(body, str):
        return body[:_RAW_TEXT_LIMIT]
    return None


def _decode(response: httpx.Response) -> Any:
    try:
        return json.loads(response.text)
    except ValueError:
        return response.text


class ApiProblemError(UniqueDomainsError):
    """An answer that is not a success, with the API's problem body.

    Attributes:
        status: the answer's HTTP status (never the body's: a gateway may rewrite one and not the other).
        code: the problem's code (``rate_limited``, ``keyed_only``, ``not_found``...), or ``unexpected_response``.
        title, detail, type, instance: the problem's members.
        product: where to get what was refused, on a tier or plan refusal (the plans page, or the account page for a member key).
        retry_after: seconds to wait, from ``Retry-After`` (a 429 or a 503).
        problem: the whole problem body, extension members included (``reason``, ``suggestion``, ``allowed``...).
        headers: the answer's headers.
        quota, rate_limit: the answer's ``X-Quota-*`` and ``X-RateLimit-*`` facts.
    """

    def __init__(
        self,
        problem: dict[str, Any],
        *,
        headers: httpx.Headers | None = None,
        retry_after: float | None = None,
        quota: Quota | None = None,
        rate_limit: RateLimit | None = None,
    ) -> None:
        super().__init__(str(problem.get("detail", "")))
        self.problem: dict[str, Any] = problem
        self.status: int = int(problem["status"])
        self.code: str = str(problem["code"])
        self.title: str = str(problem.get("title", ""))
        self.detail: str = str(problem.get("detail", ""))
        self.type: str = str(problem.get("type", "about:blank"))
        self.instance: str = str(problem.get("instance", ""))
        product = problem.get("product")
        self.product: str | None = product if isinstance(product, str) else None
        self.retry_after: float | None = retry_after
        self.headers: httpx.Headers = headers if headers is not None else httpx.Headers()
        self.quota: Quota | None = quota
        self.rate_limit: RateLimit | None = rate_limit

    def __repr__(self) -> str:
        return f"{type(self).__name__}(status={self.status}, code={self.code!r}, detail={self.detail!r})"

    @classmethod
    def from_response(cls, response: httpx.Response) -> ApiProblemError:
        """The error for an answer that is not a success, of the subclass its problem code names."""
        problem = _to_problem(_decode(response), response)
        error_class = _ERROR_CLASSES.get(problem["code"], ApiProblemError)
        return error_class(problem, **_facts(response))

    @classmethod
    def unreadable(cls, response: httpx.Response) -> ApiProblemError:
        """A success the client could not read as the API's envelope (not JSON, or not ``{data, meta, links}``):
        a captive portal, a CDN page, a wrong ``base_url``. Its body is kept in ``problem["raw"]``."""
        instance = response.request.url.path if response.request else "/"
        detail = f"The answer to {instance} ({response.status_code}) is not the API's JSON envelope."
        problem = _unexpected(response, detail, _keep_raw(_decode(response)))
        return ApiProblemError(problem, **_facts(response))


def _facts(response: httpx.Response) -> dict[str, Any]:
    return {
        "headers": response.headers,
        "retry_after": parse_retry_after(response.headers),
        "quota": parse_quota(response.headers),
        "rate_limit": parse_rate_limit(response.headers),
    }


def _unexpected(response: httpx.Response, detail: str, raw: Any) -> dict[str, Any]:
    return {
        "type": "about:blank",
        "title": response.reason_phrase or "Unexpected response",
        "status": response.status_code,
        "detail": detail,
        "instance": response.request.url.path if response.request else "/",
        "code": "unexpected_response",
        "raw": raw,
    }


def _to_problem(body: Any, response: httpx.Response) -> dict[str, Any]:
    if isinstance(body, dict) and isinstance(body.get("code"), str) and isinstance(body.get("detail"), str):
        return {
            **body,
            "type": body["type"] if isinstance(body.get("type"), str) else "about:blank",
            "title": body["title"] if isinstance(body.get("title"), str) else response.reason_phrase,
            "status": response.status_code,
            "instance": body["instance"]
            if isinstance(body.get("instance"), str)
            else (response.request.url.path if response.request else "/"),
        }
    # Not a problem body: a gateway's own refusal (RapidAPI answers `{"message": "..."}`) or a proxy's page. Its
    # message becomes the detail and the body is kept in `raw`, so the reason is never lost.
    message = body.get("message") if isinstance(body, dict) and isinstance(body.get("message"), str) else None
    return _unexpected(
        response, message or f"The API answered {response.status_code} without a problem body.", _keep_raw(body)
    )


class RateLimitError(ApiProblemError):
    """``rate_limited``: too many calls for now. ``retry_after`` says how many seconds to wait."""


class QuotaError(ApiProblemError):
    """The month's calls or units, or a day's cap, are spent. ``quota`` and ``retry_after`` say what is left and when it returns."""


class PlanRequiredError(ApiProblemError):
    """The operation needs a key or a higher plan. ``product`` says where to get it."""


class NotFoundError(ApiProblemError):
    """``not_found``."""


class ValidationError(ApiProblemError):
    """A parameter, a cursor, a field or a format the API refused. ``problem`` carries ``reason``, ``suggestion`` or ``allowed``."""


class AuthError(ApiProblemError):
    """The key was refused, or it belongs to another listing."""


class NotReadyError(ApiProblemError):
    """The answer is not ready, or a check could not run just now. Try again later."""


class WordRejectedError(ApiProblemError):
    """The word cannot be taken into the catalog. ``code`` says why."""


_ERROR_CLASSES: dict[str, type[ApiProblemError]] = {
    "rate_limited": RateLimitError,
    **dict.fromkeys(["quota_spent", "budget_spent", "consumer_day_cap", "intake_day_cap"], QuotaError),
    **dict.fromkeys(["plan_required", "keyed_only"], PlanRequiredError),
    "not_found": NotFoundError,
    **dict.fromkeys(
        ["validation_failed", "cursor_invalid", "unsupported_field", "unsupported_format"], ValidationError
    ),
    **dict.fromkeys(["invalid_key", "invalid_proxy_secret", "listing_mismatch"], AuthError),
    **dict.fromkeys(["not_ready", "check_unavailable", "gate_unavailable"], NotReadyError),
    **dict.fromkeys(["invalid_word", "disabled_in_catalog", "not_a_word", "brand", "offensive"], WordRejectedError),
}


class ListingMismatchError(UniqueDomainsError):
    """An operation the client's RapidAPI listing does not serve. Raised before any request.

    Attributes:
        operation_id: the operation called.
        listing: the listing the client's RapidAPI key subscribes to.
        served_by: the listings whose subscription opens the operation.
    """

    def __init__(self, operation_id: str, listing: dict[str, Any], served_by: list[str]) -> None:
        where = f" It is in: {', '.join(served_by)}." if served_by else " No RapidAPI listing serves it."
        super().__init__(f"{operation_id} is not part of the {listing['title']} listing ({listing['id']}).{where}")
        self.operation_id = operation_id
        self.listing: str = listing["id"]
        self.served_by: list[str] = served_by


class AnswerShapeError(UniqueDomainsError):
    """A success whose envelope the generated models cannot read (the API added a value this version does not know).

    The answer itself is fine: ``answer.json`` holds it as decoded JSON. Updating the package brings the new models.
    """
