from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_name_registry_history_response_200_data_lock_changes_item_kind import (
    GetNameRegistryHistoryResponse200DataLockChangesItemKind,
    check_get_name_registry_history_response_200_data_lock_changes_item_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNameRegistryHistoryResponse200DataLockChangesItem")


@_attrs_define
class GetNameRegistryHistoryResponse200DataLockChangesItem:
    """
    Attributes:
        at (datetime.datetime | Unset):
        kind (GetNameRegistryHistoryResponse200DataLockChangesItemKind | Unset):
    """

    at: datetime.datetime | Unset = UNSET
    kind: GetNameRegistryHistoryResponse200DataLockChangesItemKind | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: str | Unset = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _at = d.pop("at", UNSET)
        at: datetime.datetime | Unset
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = datetime.datetime.fromisoformat(_at)

        _kind = d.pop("kind", UNSET)
        kind: GetNameRegistryHistoryResponse200DataLockChangesItemKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_get_name_registry_history_response_200_data_lock_changes_item_kind(
                _kind
            )

        get_name_registry_history_response_200_data_lock_changes_item = cls(
            at=at,
            kind=kind,
        )

        get_name_registry_history_response_200_data_lock_changes_item.additional_properties = d
        return get_name_registry_history_response_200_data_lock_changes_item

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
