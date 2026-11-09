from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_tld_application_changes_response_200_data_item_kind import (
    ListTldApplicationChangesResponse200DataItemKind,
    check_list_tld_application_changes_response_200_data_item_kind,
)

T = TypeVar("T", bound="ListTldApplicationChangesResponse200DataItem")


@_attrs_define
class ListTldApplicationChangesResponse200DataItem:
    """
    Attributes:
        application_id (str):
        string (str):
        kind (ListTldApplicationChangesResponse200DataItemKind):
        before (None | str):
        after (None | str):
        seen_at (datetime.datetime): Timestamp the import saw it.
    """

    application_id: str
    string: str
    kind: ListTldApplicationChangesResponse200DataItemKind
    before: None | str
    after: None | str
    seen_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_id = self.application_id

        string = self.string

        kind: str = self.kind

        before: None | str
        before = self.before

        after: None | str
        after = self.after

        seen_at = self.seen_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applicationId": application_id,
                "string": string,
                "kind": kind,
                "before": before,
                "after": after,
                "seenAt": seen_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        application_id = d.pop("applicationId")

        string = d.pop("string")

        kind = check_list_tld_application_changes_response_200_data_item_kind(
            d.pop("kind")
        )

        def _parse_before(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        before = _parse_before(d.pop("before"))

        def _parse_after(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        after = _parse_after(d.pop("after"))

        seen_at = datetime.datetime.fromisoformat(d.pop("seenAt"))

        list_tld_application_changes_response_200_data_item = cls(
            application_id=application_id,
            string=string,
            kind=kind,
            before=before,
            after=after,
            seen_at=seen_at,
        )

        list_tld_application_changes_response_200_data_item.additional_properties = d
        return list_tld_application_changes_response_200_data_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
