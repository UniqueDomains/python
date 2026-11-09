"""The live smoke: a few keyless calls to the public API, free endpoints only (7 calls).

Run with ``pytest -m live``. The sample name is ``get.plumbing``, a tracked name with real data. The keyless window is
60 calls an hour and 100 a day per address, so this file stays small.
"""

from __future__ import annotations

import os
from collections.abc import Iterator

import pytest

from uniquedomains import Answer, Client, PlanRequiredError, TextAnswer

pytestmark = pytest.mark.live

SAMPLE = "get.plumbing"


@pytest.fixture(scope="module")
def ud() -> Iterator[Client]:
    with Client(api_key="", base_url=os.environ.get("UD_API_BASE") or None) as client:
        yield client


def test_a_name(ud: Client) -> None:
    answer = ud.names.get_name(SAMPLE)
    assert answer.status == 200
    assert answer.data.name == SAMPLE
    assert answer.data.tracked is True
    assert answer.rate_limit is not None and answer.rate_limit.limit > 0
    assert answer.quota is None
    assert answer.etag


def test_an_unchanged_name_answers_304(ud: Client) -> None:
    first = ud.request("get_name", path={"name": SAMPLE})
    assert isinstance(first, Answer) and first.etag
    second = ud.request("get_name", path={"name": SAMPLE}, if_none_match=first.etag)
    assert second.status in (200, 304)
    if second.status == 200:
        pytest.skip("The answer changed between the two calls, or the edge answered in full.")
    assert second.not_modified


def test_a_registry_record(ud: Client) -> None:
    answer = ud.names.get_name_registry(SAMPLE)
    assert answer.status == 200
    assert answer.json is not None and "registrar" in answer.json["data"]
    # The generated models read today's answer, every member of it.
    assert answer.body.to_dict()["data"].keys() == answer.json["data"].keys()


def test_tlds_as_models_and_as_csv(ud: Client) -> None:
    answer = ud.tlds.list_tlds(limit=2)
    assert len(answer.data) == 2
    csv = ud.request("list_tlds", query={"limit": 2}, format="csv")
    assert isinstance(csv, TextAnswer) and csv.text is not None
    assert csv.text.startswith("tld,")


def test_a_keyed_operation_without_a_key(ud: Client) -> None:
    with pytest.raises(PlanRequiredError) as caught:
        ud.names.get_name_prices(SAMPLE)
    assert caught.value.status == 403
    assert caught.value.product is not None
