"""The answer headers: the quota, the rate limit and the retry wait, read into typed facts.

A missing or malformed header reads as ``None``, never as 0: a caller deciding whether to wait must not mistake
"unknown" for "nothing left".
"""

from __future__ import annotations

import math
import time
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime


@dataclass(frozen=True)
class QuotaUnit:
    """A metered unit of a member key's month (``X-Quota-Unit``): live checks, appraisals or word intakes."""

    name: str
    limit: int
    remaining: int


@dataclass(frozen=True)
class Quota:
    """A member key's month, from ``X-Quota-*``: the calls it allows, the calls left, and when the month resets."""

    limit: int
    remaining: int
    resets_at: datetime | None
    """``X-Quota-Reset`` (unix seconds): the first instant of the next UTC month."""
    unit: QuotaUnit | None


@dataclass(frozen=True)
class RateLimit:
    """The keyless window, from ``X-RateLimit-*``."""

    limit: int
    remaining: int
    reset_in_seconds: int | None
    """``X-RateLimit-Reset``: seconds until the window resets."""


def _integer(headers: Mapping[str, str], name: str) -> int | None:
    raw = headers.get(name)
    if raw is None or not raw.strip():
        return None
    try:
        value = float(raw)
    except ValueError:
        return None
    if not math.isfinite(value) or value != int(value):
        return None
    return int(value)


def _instant(seconds: int | None) -> datetime | None:
    """Unix seconds as a UTC time; a value no date can hold (milliseconds sent by mistake) reads as None."""
    if seconds is None:
        return None
    try:
        return datetime.fromtimestamp(seconds, tz=UTC)
    except (ValueError, OverflowError, OSError):
        return None


def parse_quota(headers: Mapping[str, str]) -> Quota | None:
    """``X-Quota-*``, sent on a member key's answers that reached the month counter."""
    limit = _integer(headers, "x-quota-limit")
    remaining = _integer(headers, "x-quota-remaining")
    if limit is None or remaining is None:
        return None
    reset = _integer(headers, "x-quota-reset")
    unit_name = headers.get("x-quota-unit")
    unit_limit = _integer(headers, "x-quota-unit-limit")
    unit_remaining = _integer(headers, "x-quota-unit-remaining")
    unit = (
        QuotaUnit(unit_name, unit_limit, unit_remaining)
        if unit_name and unit_limit is not None and unit_remaining is not None
        else None
    )
    return Quota(
        limit=limit,
        remaining=remaining,
        resets_at=_instant(reset),
        unit=unit,
    )


def parse_rate_limit(headers: Mapping[str, str]) -> RateLimit | None:
    """``X-RateLimit-*``, the keyless window. (RapidAPI's own limit headers are ``X-RateLimit-Requests-*``, not read.)"""
    limit = _integer(headers, "x-ratelimit-limit")
    remaining = _integer(headers, "x-ratelimit-remaining")
    if limit is None or remaining is None:
        return None
    return RateLimit(limit=limit, remaining=remaining, reset_in_seconds=_integer(headers, "x-ratelimit-reset"))


def parse_retry_after(headers: Mapping[str, str], now: float | None = None) -> float | None:
    """``Retry-After`` in seconds: the API sends delta seconds; an HTTP date (allowed by RFC 9110) is converted."""
    raw = headers.get("retry-after")
    if raw is None or not raw.strip():
        return None
    try:
        seconds = float(raw)
    except ValueError:
        seconds = None
    if seconds is not None:
        return max(0.0, seconds) if math.isfinite(seconds) else None
    try:
        when = parsedate_to_datetime(raw)
    except (TypeError, ValueError):
        return None
    if when.tzinfo is None:
        when = when.replace(tzinfo=UTC)
    current = time.time() if now is None else now
    return float(max(0, math.ceil(when.timestamp() - current)))
