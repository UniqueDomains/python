"""A local HTTP server answering recorded and synthetic responses.

The recorded answers (``tests/fixtures/recorded/``) were taken keyless from the public API on 2026-11-08 (the Node SDK's
``scripts/record-fixtures.mjs``). The synthetic ones below are what cannot be recorded keyless: a 304, the 429s, a 202, a
member key's quota, a proxy's page, a gateway's refusal. The server logs every request, so a test can assert what the
client sent, and answers 404 ``not_found`` to anything it has no fixture for. Paths match with or without ``/v1``
only when a RapidAPI host is sent, so a client on the public base must use ``/v1``.
"""

from __future__ import annotations

import json
import threading
from collections.abc import Iterator
from dataclasses import dataclass, field
from datetime import UTC, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlsplit

RECORDED_DIR = Path(__file__).parent / "fixtures" / "recorded"

# `X-Quota-Reset` is the first instant of the next UTC month in unix seconds: 2026-12-01T00:00:00Z.
QUOTA_RESET = str(int(datetime(2026, 12, 1, tzinfo=UTC).timestamp()))
MEMBER_KEY = "ud_live_test_member"
WHOIS_HOST = "whois-lookup24.p.rapidapi.com"


def load_recorded() -> list[dict[str, Any]]:
    return [json.loads(file.read_text(encoding="utf-8")) for file in sorted(RECORDED_DIR.glob("*.json"))]


def recorded(name: str) -> dict[str, Any]:
    return next(fixture for fixture in load_recorded() if fixture["name"] == name)


def problem(code: str, status: int, detail: str, **extra: Any) -> dict[str, Any]:
    return {
        "type": f"https://unique.domains/api/problems/{code}",
        "title": code,
        "status": status,
        "detail": detail,
        "instance": "/v1/test",
        "code": code,
        **extra,
    }


def answer(status: int, body: Any, **headers: str) -> dict[str, Any]:
    content_type = "application/problem+json" if status >= 400 else "application/json; charset=utf-8"
    return {
        "status": status,
        "headers": {"content-type": content_type, **{k.replace("_", "-"): v for k, v in headers.items()}},
        "body": body,
    }


def envelope(data: Any, self_path: str, cursor: str | None = None) -> dict[str, Any]:
    return {
        "data": data,
        "meta": {"asOf": None, "cursor": cursor, "limit": None if cursor is None else 2},
        "links": {
            "self": f"https://api.unique.domains/v1{self_path}",
            "next": None,
            "register": None,
            "product": None,
            "dataset": None,
        },
    }


def get_name_body(name: str) -> dict[str, Any]:
    body = recorded("names-get-name")["response"]["body"]
    return {**body, "data": {**body["data"], "name": name}}


def expiring_row(name: str) -> dict[str, Any]:
    return {"id": f"dom_{name}", "name": name, "ending": "io", "expiresOn": "2026-11-20", "status": "expiring"}


GET_KEY_DATA = {
    "access": "member",
    "plan": "founder",
    "keyPrefix": "ud_live_test",
    "listing": None,
    "subscription": None,
    "month": "2026-11",
    "resetsOn": "2026-12-01",
    "calls": {"used": 412, "allowance": 10000},
    "liveChecks": {"used": 3, "allowance": 50},
    "appraisals": {"used": 0, "allowance": 0},
    "intakes": {"used": 0, "allowance": 0},
    "investorEndpoints": False,
}

QUOTA = {"x_quota_limit": "10000", "x_quota_remaining": "9588", "x_quota_reset": QUOTA_RESET}


def synthetic() -> list[dict[str, Any]]:
    get_name = recorded("names-get-name")["response"]
    return [
        # A conditional request: the recorded ETag answers 304.
        {
            "name": "not-modified",
            "request": {
                "method": "GET",
                "path": "/names/harbor.io",
                "header": ("if-none-match", get_name["headers"]["etag"]),
            },
            "response": {"status": 304, "headers": {"etag": get_name["headers"]["etag"]}, "body": None},
        },
        {
            "name": "member-get-key",
            "request": {"method": "GET", "path": "/meta/key", "header": ("authorization", f"Bearer {MEMBER_KEY}")},
            "response": answer(200, envelope(GET_KEY_DATA, "/meta/key"), **QUOTA),
        },
        {
            "name": "keyless-get-key",
            "request": {"method": "GET", "path": "/meta/key"},
            "response": answer(401, problem("invalid_key", 401, "GET /meta/key needs a key.")),
        },
        {
            "name": "rate-limited-then-ok",
            "request": {"method": "GET", "path": "/names/limited.io"},
            "responses": [
                answer(429, problem("rate_limited", 429, "Too many calls this second."), retry_after="1"),
                answer(200, get_name_body("limited.io"), etag='W/"limited"'),
            ],
        },
        {
            "name": "rate-limited-long",
            "request": {"method": "GET", "path": "/names/slow.io"},
            "response": answer(
                429,
                problem("rate_limited", 429, "The keyless hourly window is spent."),
                retry_after="900",
                x_ratelimit_limit="60",
                x_ratelimit_remaining="0",
                x_ratelimit_reset="900",
            ),
        },
        {
            "name": "rate-limited-twice",
            "request": {"method": "GET", "path": "/names/twice.io"},
            "response": answer(429, problem("rate_limited", 429, "Too many calls this second."), retry_after="1"),
        },
        {
            "name": "retry-after-zero",
            "request": {"method": "GET", "path": "/names/zero.io"},
            "response": answer(429, problem("rate_limited", 429, "Too many calls this second."), retry_after="0"),
        },
        {
            "name": "quota-spent",
            "request": {"method": "GET", "path": "/names/quota.io/prices"},
            "response": answer(
                429,
                problem(
                    "quota_spent",
                    429,
                    "This key's calls for 2026-11 are spent.",
                    product="https://app.unique.domains/settings/account",
                ),
                retry_after="86400",
                x_quota_limit="10000",
                x_quota_remaining="0",
                x_quota_reset=QUOTA_RESET,
            ),
        },
        {
            "name": "check-accepted",
            "request": {
                "method": "POST",
                "path": "/names/lantern.io/check",
                "header": ("authorization", f"Bearer {MEMBER_KEY}"),
            },
            "response": answer(
                202,
                get_name_body("lantern.io"),
                location="https://api.unique.domains/v1/names/lantern.io",
                retry_after="30",
                x_quota_unit="Live",
                x_quota_unit_limit="50",
                x_quota_unit_remaining="46",
                **QUOTA,
            ),
        },
        {
            "name": "batch-names",
            "request": {"method": "POST", "path": "/names/batch", "header": ("authorization", f"Bearer {MEMBER_KEY}")},
            "response": answer(200, envelope([], "/names/batch")),
        },
        {
            "name": "proxy-error",
            "request": {"method": "GET", "path": "/names/proxy.io"},
            "response": {
                "status": 502,
                "headers": {"content-type": "text/html"},
                "body": "<html><body>Bad gateway</body></html>",
            },
        },
        {
            "name": "html-success",
            "request": {"method": "GET", "path": "/names/portal.io"},
            "response": {
                "status": 200,
                "headers": {"content-type": "text/html"},
                "body": "<html><body>Sign in to the network</body></html>",
            },
        },
        {
            "name": "status-mismatch",
            "request": {"method": "GET", "path": "/names/mismatch.io"},
            "response": answer(403, problem("keyed_only", 400, "A gateway rewrote the status.")),
        },
        {
            "name": "unknown-value",
            "request": {"method": "GET", "path": "/names/drift.io"},
            "response": answer(
                200,
                {
                    **get_name_body("drift.io"),
                    "data": {**get_name_body("drift.io")["data"], "drop": {"kind": "a_kind_from_the_future"}},
                },
            ),
        },
        {
            "name": "not-ready-then-ok",
            "request": {"method": "GET", "path": "/names/ready.io"},
            "responses": [
                answer(503, problem("not_ready", 503, "The answer is being prepared.")),
                answer(200, get_name_body("ready.io")),
            ],
        },
        {
            "name": "check-unavailable-post",
            "request": {"method": "POST", "path": "/names/busy.io/check"},
            "response": answer(503, problem("check_unavailable", 503, "The check could not run just now.")),
        },
        {
            "name": "rapidapi-registry",
            "request": {
                "method": "GET",
                "path": "/names/harbor.io/registry",
                "header": ("x-rapidapi-host", WHOIS_HOST),
            },
            "response": answer(
                200,
                recorded("names-get-name-registry")["response"]["body"],
                x_ratelimit_limit="1000",
                x_ratelimit_remaining="999",
            ),
        },
        {
            "name": "gateway-refusal",
            "request": {
                "method": "GET",
                "path": "/names/gateway.io/registry",
                "header": ("x-rapidapi-host", WHOIS_HOST),
            },
            "response": {
                "status": 403,
                "headers": {"content-type": "application/json"},
                "body": {"message": "You are not subscribed to this API."},
            },
        },
        {
            "name": "csv-with-path-param",
            "request": {"method": "GET", "path": "/tlds/io/phases.csv"},
            "response": {
                "status": 200,
                "headers": {"content-type": "text/csv; charset=utf-8"},
                "body": "phase,startsOn,endsOn\ngeneral,1997-09-16,\n",
            },
        },
        {
            "name": "llms-txt",
            "request": {"method": "GET", "path": "/meta/llms.txt"},
            "response": {
                "status": 200,
                "headers": {"content-type": "text/plain; charset=utf-8"},
                "body": "# Unique Domains API\n",
            },
        },
        {
            "name": "expiring-io-1",
            "request": {"method": "GET", "path": "/domains/expiring", "query": "ending=io"},
            "response": answer(
                200,
                envelope([expiring_row("anchor.io"), expiring_row("beacon.io")], "/domains/expiring?ending=io", "c2"),
            ),
        },
        {
            "name": "expiring-io-2",
            "request": {"method": "GET", "path": "/domains/expiring", "query": "ending=io&cursor=c2"},
            "response": answer(
                200,
                envelope(
                    [expiring_row("cove.io"), expiring_row("dune.io")], "/domains/expiring?ending=io&cursor=c2", "c3"
                ),
            ),
        },
        {
            "name": "expiring-io-3",
            "request": {"method": "GET", "path": "/domains/expiring", "query": "ending=io&cursor=c3"},
            "response": answer(200, envelope([expiring_row("ember.io")], "/domains/expiring?ending=io&cursor=c3")),
        },
        {
            "name": "expiring-loop",
            "request": {"method": "GET", "path": "/domains/expiring", "query": "ending=ai"},
            "response": answer(200, envelope([expiring_row("loop.ai")], "/domains/expiring?ending=ai", "same")),
        },
        {
            "name": "expiring-loop-2",
            "request": {"method": "GET", "path": "/domains/expiring", "query": "ending=ai&cursor=same"},
            "response": answer(
                200, envelope([expiring_row("loop.ai")], "/domains/expiring?ending=ai&cursor=same", "same")
            ),
        },
    ]


def _query_of(raw: str) -> list[tuple[str, str]]:
    return sorted(parse_qsl(raw, keep_blank_values=True))


@dataclass
class Logged:
    method: str
    path: str
    query: list[tuple[str, str]]
    headers: dict[str, str]
    body: Any


@dataclass
class FixtureServer:
    url: str
    requests: list[Logged] = field(default_factory=list)
    calls: dict[str, int] = field(default_factory=dict)

    def reset(self) -> None:
        self.requests.clear()
        self.calls.clear()


def _matches(
    fixture: dict[str, Any], method: str, path: str, query: list[tuple[str, str]], headers: dict[str, str]
) -> bool:
    request = fixture["request"]
    if request["method"] != method:
        return False
    rapidapi = "x-rapidapi-host" in headers
    if path.startswith("/v1/"):
        path = path[3:]
    elif not rapidapi:
        return False
    if request["path"] != path or _query_of(request.get("query", "")) != query:
        return False
    header = request.get("header")
    return header is None or headers.get(header[0]) == header[1]


def _handler(server: FixtureServer, fixtures: list[dict[str, Any]]) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, *args: Any) -> None:  # quiet
            pass

        def _serve(self) -> None:
            parts = urlsplit(self.path)
            headers = {name.lower(): value for name, value in self.headers.items()}
            length = int(headers.get("content-length") or 0)
            raw = self.rfile.read(length) if length else b""
            body = json.loads(raw) if raw else None
            query = _query_of(parts.query)
            server.requests.append(Logged(self.command, parts.path, query, headers, body))
            fixture = next((f for f in fixtures if _matches(f, self.command, parts.path, query, headers)), None)
            if fixture is None:
                reply = answer(404, problem("not_found", 404, f"No fixture for {self.command} {self.path}"))
            elif "responses" in fixture:
                count = server.calls.get(fixture["name"], 0)
                server.calls[fixture["name"]] = count + 1
                reply = fixture["responses"][min(count, len(fixture["responses"]) - 1)]
            else:
                server.calls[fixture["name"]] = server.calls.get(fixture["name"], 0) + 1
                reply = fixture["response"]
            content = reply["body"]
            payload = (
                b""
                if content is None
                else (content if isinstance(content, str) else json.dumps(content)).encode("utf-8")
            )
            self.send_response(reply["status"])
            for name, value in reply["headers"].items():
                self.send_header(name, value)
            self.send_header("content-length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        do_GET = _serve
        do_POST = _serve

    return Handler


def start() -> Iterator[FixtureServer]:
    fixtures = synthetic() + [
        {**f, "request": {**f["request"], "query": f["request"]["query"]}} for f in load_recorded()
    ]
    state = FixtureServer(url="")
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), _handler(state, fixtures))
    state.url = f"http://127.0.0.1:{httpd.server_address[1]}"
    thread = threading.Thread(target=httpd.serve_forever)
    thread.start()
    try:
        yield state
    finally:
        httpd.shutdown()
        httpd.server_close()
