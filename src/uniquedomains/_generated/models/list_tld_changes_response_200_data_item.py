from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_tld_changes_response_200_data_item_kind import (
    ListTldChangesResponse200DataItemKind,
    check_list_tld_changes_response_200_data_item_kind,
)

if TYPE_CHECKING:
    from ..models.list_tld_changes_response_200_data_item_after_type_0 import (
        ListTldChangesResponse200DataItemAfterType0,
    )


T = TypeVar("T", bound="ListTldChangesResponse200DataItem")


@_attrs_define
class ListTldChangesResponse200DataItem:
    """
    Attributes:
        kind (ListTldChangesResponse200DataItemKind):
        after (ListTldChangesResponse200DataItemAfterType0 | None):
        seen_on (datetime.date): UTC day the scanner saw the change.
    """

    kind: ListTldChangesResponse200DataItemKind
    after: ListTldChangesResponse200DataItemAfterType0 | None
    seen_on: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_tld_changes_response_200_data_item_after_type_0 import (
            ListTldChangesResponse200DataItemAfterType0,
        )

        kind: str = self.kind

        after: dict[str, Any] | None
        if isinstance(self.after, ListTldChangesResponse200DataItemAfterType0):
            after = self.after.to_dict()
        else:
            after = self.after

        seen_on = self.seen_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "after": after,
                "seenOn": seen_on,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_tld_changes_response_200_data_item_after_type_0 import (
            ListTldChangesResponse200DataItemAfterType0,
        )

        d = dict(src_dict)
        kind = check_list_tld_changes_response_200_data_item_kind(d.pop("kind"))

        def _parse_after(
            data: object,
        ) -> ListTldChangesResponse200DataItemAfterType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                after_type_0 = ListTldChangesResponse200DataItemAfterType0.from_dict(
                    data
                )

                return after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListTldChangesResponse200DataItemAfterType0 | None, data)

        after = _parse_after(d.pop("after"))

        seen_on = datetime.date.fromisoformat(d.pop("seenOn"))

        list_tld_changes_response_200_data_item = cls(
            kind=kind,
            after=after,
            seen_on=seen_on,
        )

        list_tld_changes_response_200_data_item.additional_properties = d
        return list_tld_changes_response_200_data_item

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
