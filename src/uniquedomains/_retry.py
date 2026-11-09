"""The opt-in retry, as the Node SDK's.

Retried: a 429 ``rate_limited`` with a ``Retry-After`` within ``max_delay``, a 503 ``not_ready`` or
``check_unavailable``, a 5xx without a problem body, and a network failure. The wait is ``Retry-After`` when the answer
gives one, otherwise exponential backoff with full jitter. Anything but a GET is retried only on the 429: the call was
refused, not run, while a timed-out metered POST may have spent a unit.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import Any

__all__ = ["Retry"]

_BACKOFF_BASE = 0.5
_RETRIED_503_CODES = frozenset({"not_ready", "check_unavailable"})


@dataclass(frozen=True)
class Retry:
    """How the client retries when ``retry`` is on.

    Attributes:
        attempts: how many times a call is tried, the first included.
        max_delay: the longest wait, in seconds. A longer ``Retry-After`` is not waited for: the error is raised.
    """

    attempts: int = 3
    max_delay: float = 30.0

    def __post_init__(self) -> None:
        if not isinstance(self.attempts, int) or isinstance(self.attempts, bool) or self.attempts < 1:
            raise ValueError(f"Retry.attempts must be a whole number, 1 or more: {self.attempts!r}.")
        if (
            not isinstance(self.max_delay, (int, float))
            or isinstance(self.max_delay, bool)
            or not math.isfinite(self.max_delay)
            or self.max_delay < 0
        ):
            raise ValueError(f"Retry.max_delay must be a finite number of seconds, 0 or more: {self.max_delay!r}.")


def resolve_retry(option: bool | Retry | None) -> Retry | None:
    if option is None or option is False:
        return None
    if option is True:
        return Retry()
    if isinstance(option, Retry):
        return option
    raise TypeError(f"retry takes True, False or a Retry: {option!r}.")


def _code_of(body: Any) -> str | None:
    if isinstance(body, dict) and isinstance(body.get("code"), str):
        return str(body["code"])
    return None


def _backoff(policy: Retry, attempt: int) -> float:
    return random.random() * min(policy.max_delay, _BACKOFF_BASE * 2.0**attempt)


def _wait_of_retry_after(policy: Retry, seconds: float) -> float | None:
    return seconds if seconds <= policy.max_delay else None


def retry_wait(
    policy: Retry, attempt: int, method: str, status: int | None, retry_after: float | None, body: Any
) -> float | None:
    """How long to wait before trying again, or None to stop. ``status`` is None on a network failure."""
    if attempt + 1 >= policy.attempts:
        return None
    is_get = method.upper() == "GET"
    if status is None:
        return _backoff(policy, attempt) if is_get else None
    code = _code_of(body)
    if status == 429:
        return _wait_of_retry_after(policy, retry_after) if code == "rate_limited" and retry_after is not None else None
    if not is_get:
        return None
    retried = (status == 503 and code in _RETRIED_503_CODES) or (status >= 500 and code is None)
    if not retried:
        return None
    return _backoff(policy, attempt) if retry_after is None else _wait_of_retry_after(policy, retry_after)
