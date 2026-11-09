"""The generated tables and the package's own facts."""

from __future__ import annotations

import importlib
import inspect
import re
import tomllib
from pathlib import Path

import uniquedomains
from uniquedomains import LISTINGS, OPERATIONS, Client, find_listing, listings_serving
from uniquedomains._headers import parse_quota, parse_rate_limit, parse_retry_after

ROOT = Path(__file__).resolve().parent.parent
SHARED = [
    "get_meta_enums",
    "get_meta_freshness",
    "get_key",
    "get_openapi",
    "get_llms_txt",
    "get_health",
    "get_latest_edition",
    "get_edition",
]


def test_eighty_seven_operations_and_sixteen_listings() -> None:
    assert len(OPERATIONS) == 87
    assert len(LISTINGS) == 16
    assert uniquedomains.API_PUBLIC_BASE == "https://api.unique.domains/v1"


def test_the_listing_table() -> None:
    names = find_listing("names")
    whois = find_listing("whois")
    assert names is not None and whois is not None
    assert "get_name" in names["operations"]
    assert {"get_name_registry", "get_name_registry_history"} <= set(whois["operations"])
    assert whois["host"] == "whois-lookup24.p.rapidapi.com"
    for listing in LISTINGS:
        assert set(SHARED) <= set(listing["operations"]), listing["id"]
        assert listing["host"].endswith(".p.rapidapi.com")
        assert set(listing["operations"]) <= set(OPERATIONS), listing["id"]
    assert "whois" in listings_serving("get_name_registry")


def test_every_operation_has_a_typed_method_and_a_generated_module() -> None:
    ud = Client(api_key="")
    for operation_id, operation in OPERATIONS.items():
        tag, module_name = operation["module"].split(".")
        method = getattr(getattr(ud, tag), operation_id)
        assert callable(method)
        module = importlib.import_module(f"uniquedomains._generated.api.{tag}.{module_name}")
        assert callable(module._get_kwargs) and callable(module._parse_response)
        # The method's parameters are the generated request builder's, `fields` aside (a projection is `request`'s).
        built = [name for name in inspect.signature(module._get_kwargs).parameters if name != "fields"]
        assert list(inspect.signature(method).parameters) == built, operation_id
        # Path parameters come first, in path order, under the generator's names.
        path_args = [param["arg"] for param in operation["parameters"] if param["in"] == "path"]
        assert built[: len(path_args)] == path_args, operation_id
    ud.close()


def test_the_version_is_the_same_everywhere() -> None:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    assert project["version"] == uniquedomains.__version__
    assert project["license"] == "MIT"
    assert project["requires-python"] == ">=3.11"
    assert re.fullmatch(r"\d+\.\d+\.\d+", uniquedomains.__version__)


def test_quota_headers() -> None:
    quota = parse_quota({"x-quota-limit": "10000", "x-quota-remaining": "9000", "x-quota-reset": "1764547200"})
    assert (
        quota is not None and quota.resets_at is not None and quota.resets_at.isoformat() == "2025-12-01T00:00:00+00:00"
    )
    assert parse_quota({"x-quota-limit": "10000"}) is None
    assert parse_quota({"x-quota-limit": "lots", "x-quota-remaining": "1"}) is None
    no_reset = parse_quota({"x-quota-limit": "1", "x-quota-remaining": "0", "x-quota-unit": "Live"})
    assert no_reset is not None and no_reset.resets_at is None and no_reset.unit is None


def test_rate_limit_headers() -> None:
    limit = parse_rate_limit({"x-ratelimit-limit": "60", "x-ratelimit-remaining": "0"})
    assert limit is not None and limit.reset_in_seconds is None
    assert parse_rate_limit({}) is None


def test_retry_after() -> None:
    assert parse_retry_after({"retry-after": "900"}) == 900
    assert parse_retry_after({"retry-after": "-3"}) == 0
    assert parse_retry_after({"retry-after": "soon"}) is None
    assert parse_retry_after({}) is None
    # An HTTP date, 2 minutes ahead of "now".
    assert parse_retry_after({"retry-after": "Wed, 21 Oct 2015 07:30:00 GMT"}, now=1445412480.0) == 120
