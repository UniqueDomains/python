"""The review of 2026-11-09 (findings R3-1 to R3-21): each finding's reproduction, now holding."""

from __future__ import annotations

import pickle
from typing import Any

import httpx
import pytest

from uniquedomains import (
    OPERATIONS,
    Answer,
    AnswerShapeError,
    ApiProblemError,
    AuthError,
    Client,
    CursorLoopError,
    ListingMismatchError,
    NotFoundError,
    NotReadyError,
    PlanRequiredError,
    QuotaError,
    RateLimitError,
    Retry,
    ValidationError,
    WordRejectedError,
    listings_serving,
)
from uniquedomains._errors import _ERROR_CLASSES
from uniquedomains._headers import parse_quota
from uniquedomains._retry import retry_wait

from .fixture_server import MEMBER_KEY, WHOIS_HOST, FixtureServer, recorded

# ----------------------------------------------------------------------------------------------------------------------
# R3-1: redirects are followed
# ----------------------------------------------------------------------------------------------------------------------


def test_a_308_is_followed_by_a_typed_method_and_by_request(ud: Client, fixtures: FixtureServer) -> None:
    answer = ud.shared.get_meta_tlds()
    assert answer.status == 200
    assert answer.json == recorded("tlds-list-tlds")["response"]["body"]
    assert [entry.path for entry in fixtures.requests] == ["/v1/meta/tlds", "/v1/tlds"]
    again = ud.request("get_meta_tlds")
    assert isinstance(again, Answer) and again.status == 200


def test_a_308_keeps_a_post_a_post_with_its_body_and_key(base: str, fixtures: FixtureServer) -> None:
    with Client(api_key=MEMBER_KEY, base_url=base) as ud:
        answer = ud.names.check_name("moved.io", body={})
    assert answer.status == 202
    first, second = fixtures.requests
    assert (first.method, second.method) == ("POST", "POST")
    assert second.path == "/v1/names/lantern.io/check"
    assert second.body == {}
    assert second.headers["authorization"] == f"Bearer {MEMBER_KEY}"


def test_a_308_is_followed_on_a_caller_http_client(base: str, fixtures: FixtureServer) -> None:
    with httpx.Client() as pool:  # httpx's own default: follow_redirects=False
        answer = Client(api_key="", base_url=base, http_client=pool).shared.get_meta_tlds()
    assert answer.status == 200


# ----------------------------------------------------------------------------------------------------------------------
# R3-2 and R3-3: a shared pool is never changed; one header never goes twice
# ----------------------------------------------------------------------------------------------------------------------


def test_two_clients_on_one_pool_send_their_own_keys(fixtures: FixtureServer, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("UD_API_KEY", raising=False)
    with httpx.Client() as pool:
        before = (pool.base_url, dict(pool.headers))
        member = Client(api_key="ud_live_secret", base_url=f"{fixtures.url}/v1", http_client=pool)
        rapid = Client(rapidapi=("rk", "whois"), base_url=fixtures.url, http_client=pool)
        keyless = Client(api_key="", base_url=f"{fixtures.url}/v1", http_client=pool)
        assert (pool.base_url, dict(pool.headers)) == before

        rapid.names.get_name_registry("harbor.io")
        sent = fixtures.requests[-1].headers
        assert "authorization" not in sent
        assert sent["x-rapidapi-key"] == "rk" and sent["x-rapidapi-host"] == WHOIS_HOST

        with pytest.raises(AuthError):
            keyless.shared.get_key()
        assert "authorization" not in fixtures.requests[-1].headers
        assert "x-rapidapi-key" not in fixtures.requests[-1].headers

        member.names.get_name("harbor.io")
        assert fixtures.requests[-1].headers["authorization"] == "Bearer ud_live_secret"
        assert "x-rapidapi-key" not in fixtures.requests[-1].headers
        assert fixtures.requests[-1].path == "/v1/names/harbor.io"


def test_one_header_never_goes_twice(base: str, fixtures: FixtureServer, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("UD_API_KEY", "ud_live_env")
    with Client(base_url=base, headers={"authorization": f"Bearer {MEMBER_KEY}", "user-agent": "mine/1"}) as ud:
        ud.shared.get_key()
        ud.request("list_tlds", query={"limit": 3}, headers={"accept": "text/csv", "ACCEPT": "text/csv"})
    first, second = fixtures.requests
    assert first.raw_headers.count(("authorization", f"Bearer {MEMBER_KEY}")) == 1
    assert [name for name, _ in first.raw_headers].count("authorization") == 1
    assert [name for name, _ in first.raw_headers].count("user-agent") == 1
    assert first.headers["user-agent"] == "mine/1"
    assert [name for name, _ in second.raw_headers].count("accept") == 1


# ----------------------------------------------------------------------------------------------------------------------
# R3-7: a malformed quota reset reads as None
# ----------------------------------------------------------------------------------------------------------------------


def test_a_quota_reset_in_milliseconds_reads_as_none() -> None:
    quota = parse_quota({"x-quota-limit": "10", "x-quota-remaining": "9", "x-quota-reset": "1764547200000000"})
    assert quota is not None and quota.resets_at is None and quota.remaining == 9


# ----------------------------------------------------------------------------------------------------------------------
# R3-8: the errors cross a process boundary
# ----------------------------------------------------------------------------------------------------------------------


def test_the_errors_pickle(ud: Client, fixtures: FixtureServer) -> None:
    with pytest.raises(NotFoundError) as caught:
        ud.trends.get_trend("zzz-no-such")
    copy = pickle.loads(pickle.dumps(caught.value))
    assert type(copy) is NotFoundError
    assert (copy.status, copy.code, copy.detail, copy.problem) == (
        caught.value.status,
        caught.value.code,
        caught.value.detail,
        caught.value.problem,
    )
    assert copy.headers["etag"] == caught.value.headers["etag"]
    assert copy.rate_limit == caught.value.rate_limit

    mismatch = ListingMismatchError("get_name", {"id": "whois", "title": "WHOIS Lookup API"}, ["names"])
    again = pickle.loads(pickle.dumps(mismatch))
    assert str(again) == str(mismatch) and again.served_by == ["names"] and again.listing == "whois"


# ----------------------------------------------------------------------------------------------------------------------
# R3-9: an undeclared success is an AnswerShapeError, never a silent None
# ----------------------------------------------------------------------------------------------------------------------


def test_an_answer_the_models_do_not_declare(ud: Client) -> None:
    response = httpx.Response(
        206, json={"data": {}, "meta": {}, "links": {}}, request=httpx.Request("GET", "http://x/")
    )
    answer: Answer[Any, Any] = Answer(response, {"data": {}, "meta": {}, "links": {}}, lambda: None)
    with pytest.raises(AnswerShapeError):
        _ = answer.data


# ----------------------------------------------------------------------------------------------------------------------
# R3-10: a typed method sends only what the caller passed
# ----------------------------------------------------------------------------------------------------------------------


def test_the_typed_methods_send_no_default_of_their_own(ud: Client, fixtures: FixtureServer) -> None:
    ud.tlds.list_tlds(limit=3)
    assert fixtures.requests[-1].query == [("limit", "3")]
    ud.catalog.list_domains(limit=2)
    assert fixtures.requests[-1].query == [("limit", "2")]
    ud.agenda.list_events()
    assert fixtures.requests[-1].query == []


# ----------------------------------------------------------------------------------------------------------------------
# R3-14, R3-16: the retry option's edges
# ----------------------------------------------------------------------------------------------------------------------


def test_retry_refuses_an_endless_or_boolean_wait() -> None:
    for value in (float("inf"), float("nan"), True):
        with pytest.raises(ValueError):
            Retry(max_delay=value)


def test_a_wrong_scheme_is_not_retried(monkeypatch: pytest.MonkeyPatch) -> None:
    with Client(api_key="", base_url="ftp://127.0.0.1/v1", retry=Retry(attempts=3, max_delay=5)) as ud:
        monkeypatch.setattr("uniquedomains._client.time.sleep", lambda _: pytest.fail("slept before a retry"))
        with pytest.raises(httpx.UnsupportedProtocol):
            ud.names.get_name("harbor.io")


def test_a_timeout_raises_and_a_get_is_tried_again_with_retry(base: str, fixtures: FixtureServer) -> None:
    with Client(api_key="", base_url=base, timeout=0.2) as ud:
        with pytest.raises(httpx.TimeoutException):
            ud.names.get_name("slow-answer.io")
    assert fixtures.calls["slow"] == 1
    with Client(api_key="", base_url=base, timeout=0.2, retry=Retry(attempts=2, max_delay=0.1)) as ud:
        with pytest.raises(httpx.TimeoutException):
            ud.names.get_name("slow-answer.io")
    assert fixtures.calls["slow"] == 3


@pytest.mark.parametrize(
    ("method", "status", "retry_after", "body", "waits"),
    [
        ("GET", 429, 2.0, {"code": "rate_limited"}, True),
        ("POST", 429, 2.0, {"code": "rate_limited"}, True),
        ("GET", 429, 60.0, {"code": "rate_limited"}, False),  # past max_delay
        ("GET", 429, None, {"code": "rate_limited"}, False),
        ("GET", 429, 1.0, {"code": "quota_spent"}, False),
        ("GET", 503, None, {"code": "not_ready"}, True),
        ("GET", 503, None, {"code": "check_unavailable"}, True),
        ("POST", 503, None, {"code": "not_ready"}, False),
        ("GET", 502, None, None, True),
        ("GET", 500, None, {"code": "internal"}, False),
        ("GET", 404, None, {"code": "not_found"}, False),
        ("GET", None, None, None, True),  # a network failure
        ("POST", None, None, None, False),
    ],
)
def test_retry_wait(method: str, status: int | None, retry_after: float | None, body: Any, waits: bool) -> None:
    policy = Retry(attempts=3, max_delay=30)
    wait = retry_wait(policy, 0, method, status, retry_after, body)
    assert (wait is not None) == waits
    if waits and retry_after is not None:
        assert wait == retry_after
    if wait is not None:
        assert 0 <= wait <= 30
    assert retry_wait(policy, 2, method, status, retry_after, body) is None  # the last try


def test_the_backoff_grows_and_stays_under_max_delay() -> None:
    policy = Retry(attempts=10, max_delay=1.5)
    for attempt in range(9):
        wait = retry_wait(policy, attempt, "GET", None, None, None)
        assert wait is not None and 0 <= wait <= min(1.5, 0.5 * 2**attempt)


# ----------------------------------------------------------------------------------------------------------------------
# R3-21: the Node SDK's tests that had no Python twin
# ----------------------------------------------------------------------------------------------------------------------


def test_every_problem_code_maps_to_its_class() -> None:
    expected = {
        RateLimitError: ["rate_limited"],
        QuotaError: ["quota_spent", "budget_spent", "consumer_day_cap", "intake_day_cap"],
        PlanRequiredError: ["plan_required", "keyed_only"],
        NotFoundError: ["not_found"],
        ValidationError: ["validation_failed", "cursor_invalid", "unsupported_field", "unsupported_format"],
        AuthError: ["invalid_key", "invalid_proxy_secret", "listing_mismatch"],
        NotReadyError: ["not_ready", "check_unavailable", "gate_unavailable"],
        WordRejectedError: ["invalid_word", "disabled_in_catalog", "not_a_word", "brand", "offensive"],
    }
    assert _ERROR_CLASSES == {code: cls for cls, codes in expected.items() for code in codes}
    request = httpx.Request("GET", "http://x/v1/y")
    for code, cls in _ERROR_CLASSES.items():
        response = httpx.Response(400, json={"code": code, "detail": "d"}, request=request)
        assert type(ApiProblemError.from_response(response)) is cls
    newer = httpx.Response(400, json={"code": "a_newer_code", "detail": "d"}, request=request)
    assert type(ApiProblemError.from_response(newer)) is ApiProblemError


def test_include_is_joined(ud: Client, fixtures: FixtureServer) -> None:
    with pytest.raises(NotFoundError):  # no fixture answers it; what was sent is the point
        ud.words.get_word_endings("harbor", include=["cheapest", "sales"])
    assert ("include", "cheapest,sales") in fixtures.requests[-1].query
    with pytest.raises(NotFoundError):
        ud.request("get_word_endings", path={"word": "harbor"}, include=["cheapest"])
    assert ("include", "cheapest") in fixtures.requests[-1].query


def test_a_bad_max_rows_is_refused(ud: Client, fixtures: FixtureServer) -> None:
    for value in (-1, 1.5, True):
        with pytest.raises(ValueError, match="max_rows"):
            list(ud.iter_rows("list_expiring_domains", query={"ending": "io"}, max_rows=value))  # type: ignore[arg-type]
    assert fixtures.requests == []


def test_the_four_file_operations_are_text() -> None:
    text = sorted(op_id for op_id, op in OPERATIONS.items() if op["answer"] == "text")
    assert text == ["get_agenda_ics", "get_events_ics", "get_llms_txt", "get_openapi"]


def test_every_operation_but_the_shared_ones_is_served_by_a_listing() -> None:
    for operation_id, operation in OPERATIONS.items():
        if operation["tag"] != "shared":
            assert listings_serving(operation_id), operation_id


def test_a_202_reads_through_data(base: str) -> None:
    with Client(api_key=MEMBER_KEY, base_url=base) as ud:
        answer = ud.names.check_name("lantern.io", body={})
    assert answer.status == 202
    assert type(answer.body).__name__ == "CheckNameResponse202"
    assert answer.data.name == "lantern.io"


def test_a_repeated_cursor_is_not_an_api_problem(ud: Client) -> None:
    with pytest.raises(CursorLoopError) as caught:
        list(ud.iter_rows("list_expiring_domains", query={"ending": "ai"}))
    assert not isinstance(caught.value, ApiProblemError)
