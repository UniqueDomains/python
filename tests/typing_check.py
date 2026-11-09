"""Checked by mypy, never run: the typed methods' answers have the types the README promises."""

from __future__ import annotations

from typing import Any, assert_type

from uniquedomains import Answer, Client, TextAnswer
from uniquedomains.models import (
    GetNameResponse200,
    GetNameResponse200Data,
    ListTldsResponse200,
    ListTldsResponse200DataItem,
)


def typed_answers(ud: Client) -> None:
    name = ud.names.get_name("get.plumbing")
    assert_type(name, Answer[GetNameResponse200, GetNameResponse200Data])
    assert_type(name.data, GetNameResponse200Data)
    assert_type(name.body, GetNameResponse200)
    tlds = ud.tlds.list_tlds(public_set=True, limit=3)
    assert_type(tlds, Answer[ListTldsResponse200, list[ListTldsResponse200DataItem]])
    assert_type(ud.shared.get_llms_txt(), TextAnswer)
    answer = ud.request("get_name", path={"name": "get.plumbing"})
    assert_type(answer, Answer[dict[str, Any], Any] | TextAnswer)
    ud.names.batch_names(body={"names": ["get.plumbing"]})
