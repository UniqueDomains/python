"""The client against the fixture server: one recorded answer per tag, the problems, the 304, the 429s, the listing
guard, the keys, the quota, the unreadable answers, CSV, paging and the retry option."""

from __future__ import annotations

import re
import time
from datetime import UTC, datetime

import pytest

from uniquedomains import (
    Answer,
    AnswerShapeError,
    ApiProblemError,
    AuthError,
    Client,
    ListingMismatchError,
    NotFoundError,
    NotReadyError,
    PlanRequiredError,
    QuotaError,
    RapidApi,
    RateLimitError,
    Retry,
    TextAnswer,
    ValidationError,
)
from uniquedomains.models import BatchNamesBody

from .fixture_server import MEMBER_KEY, WHOIS_HOST, FixtureServer, recorded

# ----------------------------------------------------------------------------------------------------------------------
# One recorded answer per tag, through the typed methods and the generated models
# ----------------------------------------------------------------------------------------------------------------------

_ISO_TIME = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")


def _same(left: object, right: object) -> bool:
    """JSON equality where two spellings of one instant (`Z` or `+00:00`, with or without milliseconds) agree."""
    if isinstance(left, dict) and isinstance(right, dict):
        return left.keys() == right.keys() and all(_same(left[key], right[key]) for key in left)
    if isinstance(left, list) and isinstance(right, list):
        return len(left) == len(right) and all(_same(a, b) for a, b in zip(left, right, strict=True))
    if isinstance(left, str) and isinstance(right, str) and _ISO_TIME.match(left) and _ISO_TIME.match(right):
        return datetime.fromisoformat(left.replace("Z", "+00:00")) == datetime.fromisoformat(
            right.replace("Z", "+00:00")
        )
    return left == right


TAG_CALLS = [
    ("names", "names-get-name", lambda ud: ud.names.get_name("harbor.io")),
    ("names", "names-get-name-registry", lambda ud: ud.names.get_name_registry("harbor.io")),
    ("words", "words-resolve-word", lambda ud: ud.words.resolve_word(q="harbor")),
    ("catalog", "catalog-list-domains", lambda ud: ud.catalog.list_domains(limit=2)),
    ("tlds", "tlds-list-tlds", lambda ud: ud.tlds.list_tlds(limit=3)),
    ("registrars", "registrars-list-registrars", lambda ud: ud.registrars.list_registrars()),
    ("registrars", "prices-list-tld-prices", lambda ud: ud.registrars.list_tld_prices("io")),
    ("market", "market-get-market-sales", lambda ud: ud.market.get_market_sales()),
    ("trends", "trends-list-trend-categories", lambda ud: ud.trends.list_trend_categories()),
    ("agenda", "agenda-list-events", lambda ud: ud.agenda.list_events()),
    ("shared", "shared-get-meta-freshness", lambda ud: ud.shared.get_meta_freshness()),
]


@pytest.mark.parametrize(
    ("tag", "fixture", "call"), TAG_CALLS, ids=[f"{tag}:{fixture}" for tag, fixture, _ in TAG_CALLS]
)
def test_one_recorded_answer_per_tag(ud: Client, fixtures: FixtureServer, tag: str, fixture: str, call) -> None:
    answer = call(ud)
    expected = recorded(fixture)["response"]
    assert isinstance(answer, Answer)
    assert answer.status == 200
    assert answer.json == expected["body"]
    # The generated model reads the recorded envelope, and writes it back unchanged (times as ISO 8601 either way).
    assert _same(answer.body.to_dict()["data"], expected["body"]["data"])
    assert answer.data is answer.body.data
    assert answer.etag == expected["headers"]["etag"]
    assert answer.rate_limit is not None and answer.rate_limit.limit == 60
    assert answer.quota is None
    assert fixtures.calls == {fixture: 1}


def test_every_tag_has_a_recorded_answer() -> None:
    from uniquedomains import OPERATIONS

    assert {tag for tag, _, _ in TAG_CALLS} == {operation["module"].split(".")[0] for operation in OPERATIONS.values()}


def test_the_typed_method_sends_the_query(ud: Client, fixtures: FixtureServer) -> None:
    with pytest.raises(NotFoundError):  # no fixture answers this query; what was sent is the point
        ud.tlds.list_tlds(public_set=True, limit=2)
    assert fixtures.requests[-1].query == sorted([("publicSet", "true"), ("limit", "2")])
    assert fixtures.requests[-1].path == "/v1/tlds"
    assert fixtures.requests[-1].headers["accept"] == "application/json"


def test_the_request_path_answers_decoded_json(ud: Client) -> None:
    answer = ud.request("get_name", path={"name": "harbor.io"})
    assert isinstance(answer, Answer)
    assert answer.body == recorded("names-get-name")["response"]["body"]
    assert answer.data["name"] == "harbor.io"
    assert answer.meta == answer.json["meta"]
    assert answer.links["self"].endswith("/names/harbor.io")


def test_a_text_operation_answers_text(ud: Client) -> None:
    answer = ud.shared.get_llms_txt()
    assert isinstance(answer, TextAnswer)
    assert answer.text == "# Unique Domains API\n"
    assert answer.content_type.startswith("text/plain")


def test_a_value_the_models_do_not_know_keeps_the_json(ud: Client) -> None:
    answer = ud.names.get_name("drift.io")
    assert answer.json["data"]["drop"]["kind"] == "a_kind_from_the_future"
    with pytest.raises(AnswerShapeError):
        _ = answer.body


# ----------------------------------------------------------------------------------------------------------------------
# The three problem shapes
# ----------------------------------------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("fixture", "error_class", "call"),
    [
        ("problem-keyed-only", PlanRequiredError, lambda ud: ud.names.get_name_prices("harbor.io")),
        ("problem-not-found", NotFoundError, lambda ud: ud.trends.get_trend("zzz-no-such")),
        ("problem-validation-failed", ValidationError, lambda ud: ud.names.get_name("harbor")),
    ],
)
def test_the_three_problem_shapes(ud: Client, fixture: str, error_class: type[ApiProblemError], call) -> None:
    expected = recorded(fixture)["response"]
    with pytest.raises(error_class) as caught:
        call(ud)
    error = caught.value
    assert isinstance(error, ApiProblemError)
    assert error.status == expected["status"]
    assert error.code == expected["body"]["code"]
    assert error.detail == expected["body"]["detail"] == str(error)
    assert error.problem["type"] == expected["body"]["type"]
    assert error.product == expected["body"].get("product")
    assert error.rate_limit is not None


def test_the_request_path_raises_the_same_problem(ud: Client) -> None:
    with pytest.raises(PlanRequiredError) as caught:
        ud.request("get_name_prices", path={"name": "harbor.io"})
    assert caught.value.product == "https://unique.domains/pricing" or caught.value.product.startswith("https://")


# ----------------------------------------------------------------------------------------------------------------------
# A 304, the 429s
# ----------------------------------------------------------------------------------------------------------------------


def test_a_304_with_the_etag(ud: Client, fixtures: FixtureServer) -> None:
    etag = recorded("names-get-name")["response"]["headers"]["etag"]
    answer = ud.request("get_name", path={"name": "harbor.io"}, if_none_match=etag)
    assert isinstance(answer, Answer)
    assert answer.not_modified and answer.status == 304 and answer.json is None
    assert fixtures.requests[-1].headers["if-none-match"] == etag
    with pytest.raises(AttributeError):
        _ = answer.body


def test_if_none_match_comes_only_from_the_option(base: str, fixtures: FixtureServer) -> None:
    with Client(api_key="", base_url=base, headers={"If-None-Match": 'W/"x"'}) as ud:
        answer = ud.request("get_name", path={"name": "harbor.io"}, headers={"if-none-match": 'W/"y"'})
    assert not answer.not_modified
    assert "if-none-match" not in fixtures.requests[-1].headers


def test_a_429_with_retry_after_1_is_retried_once(ud: Client, fixtures: FixtureServer) -> None:
    started = time.monotonic()
    answer = ud.names.get_name("limited.io")
    assert time.monotonic() - started >= 0.9
    assert answer.data.name == "limited.io"
    assert fixtures.calls["rate-limited-then-ok"] == 2


def test_a_429_with_a_long_retry_after_raises(ud: Client, fixtures: FixtureServer) -> None:
    with pytest.raises(RateLimitError) as caught:
        ud.names.get_name("slow.io")
    error = caught.value
    assert error.status == 429 and error.code == "rate_limited"
    assert error.retry_after == 900
    assert error.rate_limit is not None and error.rate_limit.remaining == 0 and error.rate_limit.reset_in_seconds == 900
    assert fixtures.calls["rate-limited-long"] == 1


def test_a_second_429_raises(ud: Client, fixtures: FixtureServer) -> None:
    with pytest.raises(RateLimitError):
        ud.names.get_name("twice.io")
    assert fixtures.calls["rate-limited-twice"] == 2


def test_retry_after_0_is_not_retried(ud: Client, fixtures: FixtureServer) -> None:
    with pytest.raises(RateLimitError) as caught:
        ud.names.get_name("zero.io")
    assert caught.value.retry_after == 0
    assert fixtures.calls["retry-after-zero"] == 1


def test_a_spent_quota(ud: Client) -> None:
    with pytest.raises(QuotaError) as caught:
        ud.names.get_name_prices("quota.io")
    error = caught.value
    assert error.quota is not None and error.quota.remaining == 0
    assert error.retry_after == 86400
    assert error.product == "https://app.unique.domains/settings/account"


# ----------------------------------------------------------------------------------------------------------------------
# Keys and the listing guard
# ----------------------------------------------------------------------------------------------------------------------


def test_the_member_key_from_the_environment(
    base: str, fixtures: FixtureServer, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("UD_API_KEY", MEMBER_KEY)
    with Client(base_url=base) as ud:
        assert ud.auth == "member"
        answer = ud.shared.get_key()
    assert fixtures.requests[-1].headers["authorization"] == f"Bearer {MEMBER_KEY}"
    assert answer.data.plan == "founder"
    assert answer.quota is not None
    assert answer.quota.limit == 10000 and answer.quota.remaining == 9588
    assert answer.quota.resets_at == datetime(2026, 12, 1, tzinfo=UTC)
    assert answer.quota.unit is None


def test_an_empty_key_calls_keyless_even_with_the_environment(
    base: str, fixtures: FixtureServer, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("UD_API_KEY", MEMBER_KEY)
    with Client(api_key="", base_url=base) as ud:
        assert ud.auth == "none"
        with pytest.raises(AuthError):
            ud.shared.get_key()
    assert "authorization" not in fixtures.requests[-1].headers


def test_an_explicit_key_wins_over_the_environment(
    base: str, fixtures: FixtureServer, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("UD_API_KEY", "ud_live_other")
    with Client(api_key=MEMBER_KEY, base_url=base) as ud:
        ud.shared.get_key()
    assert fixtures.requests[-1].headers["authorization"] == f"Bearer {MEMBER_KEY}"
    assert fixtures.requests[-1].headers["user-agent"].startswith("uniquedomains-python/")


def test_a_rapidapi_key_goes_to_its_listing_host(fixtures: FixtureServer, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("UD_API_KEY", MEMBER_KEY)
    with Client(rapidapi=("rapid-key", "whois")) as default:
        assert default.base_url == f"https://{WHOIS_HOST}"
        assert default.auth == "rapidapi"
    with Client(rapidapi=RapidApi("rapid-key", "whois"), base_url=fixtures.url) as ud:
        answer = ud.names.get_name_registry("harbor.io")
    sent = fixtures.requests[-1]
    assert sent.path == "/names/harbor.io/registry"
    assert sent.headers["x-rapidapi-key"] == "rapid-key"
    assert sent.headers["x-rapidapi-host"] == WHOIS_HOST
    assert "authorization" not in sent.headers
    assert answer.rate_limit is not None and answer.rate_limit.limit == 1000


def test_an_operation_outside_the_listing_raises_before_any_call(fixtures: FixtureServer) -> None:
    with Client(rapidapi=("rapid-key", "whois"), base_url=fixtures.url) as ud:
        with pytest.raises(ListingMismatchError) as caught:
            ud.names.get_name("harbor.io")
        with pytest.raises(ListingMismatchError):
            ud.request("list_tlds")
    error = caught.value
    assert error.operation_id == "get_name"
    assert error.listing == "whois"
    assert "names" in error.served_by
    assert "not part of the WHOIS Lookup API listing (whois)" in str(error) and "It is in: " in str(error)
    assert fixtures.requests == []


def test_a_gateway_refusal_keeps_its_message(fixtures: FixtureServer) -> None:
    with Client(rapidapi=("rapid-key", "whois"), base_url=fixtures.url) as ud:
        with pytest.raises(ApiProblemError) as caught:
            ud.names.get_name_registry("gateway.io")
    error = caught.value
    assert error.code == "unexpected_response" and error.status == 403
    assert error.detail == "You are not subscribed to this API."
    assert error.problem["raw"] == {"message": "You are not subscribed to this API."}


def test_the_client_refuses_bad_options() -> None:
    with pytest.raises(ValueError, match="Unknown RapidAPI listing"):
        Client(rapidapi=("key", "nope"))
    with pytest.raises(ValueError, match="either api_key or rapidapi"):
        Client(api_key="ud_live_x", rapidapi=("key", "whois"))
    with pytest.raises(ValueError, match="empty"):
        Client(rapidapi=("", "whois"))


# ----------------------------------------------------------------------------------------------------------------------
# What is not the API's answer
# ----------------------------------------------------------------------------------------------------------------------


def test_a_proxy_page_is_a_problem(ud: Client) -> None:
    with pytest.raises(ApiProblemError) as caught:
        ud.names.get_name("proxy.io")
    error = caught.value
    assert error.status == 502 and error.code == "unexpected_response"
    assert "Bad gateway" in error.problem["raw"]


def test_a_success_that_is_not_the_envelope(ud: Client) -> None:
    with pytest.raises(ApiProblemError) as caught:
        ud.names.get_name("portal.io")
    assert caught.value.code == "unexpected_response" and caught.value.status == 200
    with pytest.raises(ApiProblemError):
        ud.request("get_name", path={"name": "portal.io"})


def test_the_status_comes_from_the_answer(ud: Client) -> None:
    with pytest.raises(PlanRequiredError) as caught:
        ud.names.get_name("mismatch.io")
    assert caught.value.status == 403


# ----------------------------------------------------------------------------------------------------------------------
# Bodies, 202, CSV, projections, path values
# ----------------------------------------------------------------------------------------------------------------------


def test_a_body_as_a_mapping_or_a_model(base: str, fixtures: FixtureServer) -> None:
    with Client(api_key=MEMBER_KEY, base_url=base) as ud:
        ud.names.batch_names(body={"names": ["get.plumbing", "harbor.io"]})
        assert fixtures.requests[-1].body == {"names": ["get.plumbing", "harbor.io"]}
        ud.names.batch_names(body=BatchNamesBody(names=["harbor.io"]))
        assert fixtures.requests[-1].body == {"names": ["harbor.io"]}
        ud.request("batch_names", body={"names": ["harbor.io"]})
        assert fixtures.requests[-1].body == {"names": ["harbor.io"]}


def test_a_202_carries_location_retry_after_and_the_unit(base: str) -> None:
    with Client(api_key=MEMBER_KEY, base_url=base) as ud:
        answer = ud.names.check_name("lantern.io", body={})
    assert answer.status == 202
    assert answer.location == "https://api.unique.domains/v1/names/lantern.io"
    assert answer.retry_after == 30
    assert answer.quota is not None and answer.quota.unit is not None
    assert (answer.quota.unit.name, answer.quota.unit.limit, answer.quota.unit.remaining) == ("Live", 50, 46)


def test_the_csv_form(ud: Client, fixtures: FixtureServer) -> None:
    answer = ud.request("list_tlds", query={"limit": 3}, format="csv")
    assert isinstance(answer, TextAnswer)
    assert answer.text == recorded("csv-list-tlds")["response"]["body"]
    assert fixtures.requests[-1].path == "/v1/tlds.csv"
    assert fixtures.requests[-1].headers["accept"] == "text/csv"
    phases = ud.request("list_tld_phases", path={"tld": "io"}, format="csv")
    assert phases.text.startswith("phase,")
    with pytest.raises(TypeError, match="no CSV form"):
        ud.request("get_name", path={"name": "harbor.io"}, format="csv")


def test_projections_and_parameters_are_checked(ud: Client, fixtures: FixtureServer) -> None:
    with pytest.raises(TypeError, match="takes no include"):
        ud.request("get_name", path={"name": "harbor.io"}, include="cheapest")
    with pytest.raises(TypeError, match="no query parameter 'limt'"):
        ud.request("list_tlds", query={"limt": 3})
    with pytest.raises(TypeError, match="needs the path parameter 'name'"):
        ud.request("get_name")
    with pytest.raises(ValueError, match="Unknown operation"):
        ud.request("get_names")
    assert fixtures.requests == []
    ud.request("list_tlds", query={"limit": 3}, fields=[])
    assert ("fields", "") not in fixtures.requests[-1].query
    ud.request("list_tlds", query={"limit": 3}, fields="")
    assert all(name != "fields" for name, _ in fixtures.requests[-1].query)


def test_a_projection_answers_decoded_json(ud: Client) -> None:
    answer = ud.request("list_tlds", query={"publicSet": True, "limit": 2}, fields=["tld", "kind"])
    assert isinstance(answer, Answer)
    assert answer.data == [{"tld": ".ai", "kind": "root"}, {"tld": ".app", "kind": "root"}]
    assert not hasattr(ud.tlds.list_tlds, "fields")
    import inspect

    assert "fields" not in inspect.signature(ud.tlds.list_tlds).parameters


def test_dot_path_values_are_refused(ud: Client, fixtures: FixtureServer) -> None:
    for value in ("..", ".", ""):
        with pytest.raises(ValueError, match="cannot be"):
            ud.names.get_name(value)
        with pytest.raises(ValueError, match="cannot be"):
            ud.request("get_name", path={"name": value})
    assert fixtures.requests == []


# ----------------------------------------------------------------------------------------------------------------------
# Paging
# ----------------------------------------------------------------------------------------------------------------------


def test_iter_rows_follows_the_cursor(base: str, fixtures: FixtureServer) -> None:
    with Client(api_key="", base_url=base) as ud:
        rows = list(ud.iter_rows("list_expiring_domains", query={"ending": "io"}))
        assert [row["name"] for row in rows] == ["anchor.io", "beacon.io", "cove.io", "dune.io", "ember.io"]
        assert len(list(ud.iter_rows("list_expiring_domains", query={"ending": "io"}, max_rows=3))) == 3
        pages = list(ud.iter_pages("list_expiring_domains", query={"ending": "io"}, max_rows=3))
        assert len(pages) == 2
        assert list(ud.iter_rows("list_expiring_domains", query={"ending": "io"}, max_rows=0)) == []
        with pytest.raises(TypeError, match="does not page"):
            list(ud.iter_rows("get_name", path={"name": "harbor.io"}))


def test_iter_rows_stops_on_a_repeated_cursor(ud: Client) -> None:
    with pytest.raises(ApiProblemError, match="cursor it was sent"):
        list(ud.iter_rows("list_expiring_domains", query={"ending": "ai"}))


# ----------------------------------------------------------------------------------------------------------------------
# The retry option
# ----------------------------------------------------------------------------------------------------------------------


def test_retry_tries_a_503_not_ready_again(base: str, fixtures: FixtureServer) -> None:
    with Client(api_key="", base_url=base, retry=Retry(attempts=2, max_delay=0.2)) as ud:
        answer = ud.names.get_name("ready.io")
    assert answer.data.name == "ready.io"
    assert fixtures.calls["not-ready-then-ok"] == 2


def test_without_retry_a_503_raises(ud: Client) -> None:
    with pytest.raises(NotReadyError):
        ud.names.get_name("ready.io")


def test_retry_never_repeats_a_post_on_a_503(base: str, fixtures: FixtureServer) -> None:
    with Client(api_key="", base_url=base, retry=True) as ud:
        with pytest.raises(NotReadyError):
            ud.names.check_name("busy.io", body={})
    assert fixtures.calls["check-unavailable-post"] == 1


def test_retry_does_not_wait_past_max_delay(base: str, fixtures: FixtureServer) -> None:
    with Client(api_key="", base_url=base, retry=Retry(attempts=3, max_delay=10)) as ud:
        with pytest.raises(RateLimitError):
            ud.names.get_name("slow.io")
    assert fixtures.calls["rate-limited-long"] == 1


def test_retry_refuses_bad_options() -> None:
    with pytest.raises(ValueError):
        Retry(attempts=0)
    with pytest.raises(ValueError):
        Retry(max_delay=-1)
    with pytest.raises(TypeError):
        Client(retry="yes")  # type: ignore[arg-type]
