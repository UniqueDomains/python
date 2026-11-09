# Unique Domains for Python

The Unique Domains API answers questions about domain names: whether a name is free, its registry record, what registrars charge for each ending, and what the domain market did. It covers names, words, endings, registrar prices, the market, trends and the industry agenda, and most of it works without a key.

`uniquedomains` is its Python client, generated from the API's OpenAPI document: every operation is a typed method, every answer a typed model.

## Install

```bash
pip install uniquedomains
```

Python 3.11 or later. The client depends on `httpx` and `attrs`.

## A first call

No key needed for the free endpoints:

```python
from uniquedomains import Client

ud = Client()
answer = ud.names.get_name("get.plumbing")
print(answer.data.status, answer.data.price.kind)
```

The methods are grouped by the API's tags (`ud.names`, `ud.words`, `ud.catalog`, `ud.tlds`, `ud.registrars`, `ud.market`, `ud.trends`, `ud.agenda`, `ud.shared`) and named by their operation id, the name the [API reference](https://unique.domains/api) uses: `get_name` is documented at `https://unique.domains/api/get-name`.

Every method answers an `Answer`:

| Member | What it is |
|---|---|
| `data` | The answer's data, as a typed model (`answer.data.status`) |
| `body` | The whole envelope as a typed model (`data`, `meta`, `links`) |
| `json` | The envelope as decoded JSON |
| `meta`, `links`, `cursor` | The envelope's `meta` and `links` as dictionaries, and the next page's cursor |
| `status`, `headers`, `etag`, `location`, `retry_after` | What the answer's status and headers say |
| `quota`, `rate_limit` | A member key's month and the keyless window (below) |

The four file answers (the OpenAPI document, `llms.txt`, the two calendars) come back as a `TextAnswer` with `text`.

Optional parameters are keywords:

```python
endings = ud.tlds.list_tlds(public_set=True, limit=3)
for ending in endings.data:
    print(ending.tld, ending.kind)
```

A body takes a dictionary or its model (`uniquedomains.models`):

```python
ud.names.batch_names(body={"names": ["get.plumbing", "harbor.io"]})
```

Use the client as a context manager, or call `ud.close()`, to release its connections. Redirects are followed. To share one connection pool, pass your `httpx.Client` as `http_client`: each client sends its own URL, key and headers with every request and never changes the pool, so a member client and a RapidAPI client can share it.

## Keys

Without a key you read the free endpoints, within a limit per hour and per day. Two ways go further.

**A member key.** The Founder and Investor plans include the API with a key of your own (`ud_live_...`). Create it in the product under Settings, Account, API, then set `UD_API_KEY`, or pass it:

```python
ud = Client(api_key="ud_live_...")
key = ud.shared.get_key()
print(key.data.plan, key.data.calls)
```

The client reads `UD_API_KEY` when you pass no key; `Client(api_key="")` calls without one even when it is set.

**A RapidAPI subscription.** The API is also on RapidAPI as sixteen listings. Pass your RapidAPI key with the listing it subscribes to:

```python
ud = Client(rapidapi=("your-rapidapi-key", "whois"))
record = ud.names.get_name_registry("get.plumbing")
```

The client then calls that listing's RapidAPI host with `X-RapidAPI-Key` and `X-RapidAPI-Host`. A method the listing does not serve raises `ListingMismatchError` before any call, and names the listings that serve it. `uniquedomains.LISTINGS` lists the sixteen with their operations.

Keep a key on a server. What each plan includes is on the [API page](https://unique.domains/api).

## Errors

Every answer that is not a success raises an `ApiProblemError`, carrying the API's problem: `status`, `code`, `detail`, `product` (where to get what was refused) and `retry_after`. A subclass names the kind:

```python
from uniquedomains import ApiProblemError, PlanRequiredError, RateLimitError

try:
    ud.names.get_name_prices("get.plumbing")
except PlanRequiredError as error:
    print("Needs a key or another plan:", error.product)
except RateLimitError as error:
    print(f"Wait {error.retry_after} seconds")
except ApiProblemError as error:
    print(error.status, error.code, error.detail)
```

| Error | Problem codes |
|---|---|
| `RateLimitError` | `rate_limited` |
| `QuotaError` | `quota_spent`, `budget_spent`, `consumer_day_cap`, `intake_day_cap` |
| `PlanRequiredError` | `keyed_only`, `plan_required` |
| `NotFoundError` | `not_found` |
| `ValidationError` | `validation_failed`, `cursor_invalid`, `unsupported_field`, `unsupported_format` |
| `AuthError` | `invalid_key`, `invalid_proxy_secret`, `listing_mismatch` |
| `NotReadyError` | `not_ready`, `check_unavailable`, `gate_unavailable` |
| `WordRejectedError` | `invalid_word`, `disabled_in_catalog`, `not_a_word`, `brand`, `offensive` |

An answer with no problem body (a proxy's page, a gateway's own refusal) is an `ApiProblemError` with the code `unexpected_response`, its body in `error.problem["raw"]`. A network failure stays httpx's own `httpx.TransportError`.

The client retries once on its own: after a `rate_limited` answer with `Retry-After: 1`. `Client(retry=True)` retries what is worth retrying (a short `rate_limited` wait, a 503 `not_ready`, a 5xx without a problem body, a network failure or a timeout on a GET), up to three tries; `Retry(attempts=..., max_delay=...)` sets both.

## Quota and rate limit

A member key's answers carry its month in `quota`: `limit`, `remaining`, `resets_at` (a UTC `datetime`, from `X-Quota-Reset` in unix seconds) and `unit`, the metered unit a call spent (live checks, appraisals). Keyless answers carry the window in `rate_limit`: `limit`, `remaining`, `reset_in_seconds`. Each is `None` when its headers are absent.

```python
answer = ud.names.get_name("get.plumbing")
if answer.quota:
    print(answer.quota.remaining, "calls left until", answer.quota.resets_at)
if answer.rate_limit:
    print(answer.rate_limit.remaining, "keyless calls left in this window")
```

## Tools and loops

`request` calls any operation by its id, with the API's own parameter names, and answers the envelope as decoded JSON. It also carries projections (`fields`, a list or a comma string: a partial row does not fit the typed models), the `.csv` forms and conditional requests:

```python
answer = ud.request("get_name", path={"name": "get.plumbing"}, fields=["name", "status"])
again = ud.request("get_name", path={"name": "get.plumbing"}, if_none_match=answer.etag)
print(again.not_modified)

csv = ud.request("list_tlds", query={"limit": 10}, format="csv")
print(csv.text)
```

A list that pages with a cursor reads page after page:

```python
for row in ud.iter_rows("list_tlds", query={"publicSet": True}, max_rows=50):
    print(row["tld"])
```

`uniquedomains.OPERATIONS` describes the 87 operations (method, path, tag, tier, plan, parameters).

## Also from Unique Domains

- [The API reference](https://unique.domains/api): every endpoint, with examples.
- [The datasets](https://github.com/UniqueDomains): one-word domain names, expiring names, the daily editions and the new gTLD applications, as files on GitHub.
- [`@uniquedomains/sdk`](https://www.npmjs.com/package/@uniquedomains/sdk): the Node client, with the `ud` command in [`@uniquedomains/cli`](https://www.npmjs.com/package/@uniquedomains/cli) ([UniqueDomains/nodejs](https://github.com/UniqueDomains/nodejs)).
- [`@uniquedomains/mcp-server`](https://www.npmjs.com/package/@uniquedomains/mcp-server): the API as tools for AI assistants, through the Model Context Protocol, also hosted at `https://mcp.unique.domains/mcp` ([UniqueDomains/mcp-server](https://github.com/UniqueDomains/mcp-server)).

## Working on this repository

```bash
python -m venv .venv && . .venv/bin/activate
python -m pip install --upgrade pip           # --group needs pip 25.1 or later
pip install --group dev -e .
pytest                                         # offline, against a local fixture server
pytest -m live                                 # 7 keyless calls to the public API, free endpoints only
python scripts/generate.py                     # refresh openapi/ from the live document and regenerate
python scripts/generate.py --offline --check   # the generated code matches the committed snapshot
```

The client under `src/uniquedomains/_generated/` is written by [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client) from `openapi/v1.json`; `_operations.py`, `_listings.py` and `_namespaces.py` come from the same script. Edit `scripts/generate.py`, never the generated files.

## License

MIT
