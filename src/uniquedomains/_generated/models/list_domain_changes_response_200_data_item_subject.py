from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_domain_changes_response_200_data_item_subject_kind import (
    ListDomainChangesResponse200DataItemSubjectKind,
    check_list_domain_changes_response_200_data_item_subject_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListDomainChangesResponse200DataItemSubject")


@_attrs_define
class ListDomainChangesResponse200DataItemSubject:
    """
    Attributes:
        kind (ListDomainChangesResponse200DataItemSubjectKind | Unset):
        key (None | str | Unset):
    """

    kind: ListDomainChangesResponse200DataItemSubjectKind | Unset = UNSET
    key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: ListDomainChangesResponse200DataItemSubjectKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_list_domain_changes_response_200_data_item_subject_kind(_kind)

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))

        list_domain_changes_response_200_data_item_subject = cls(
            kind=kind,
            key=key,
        )

        list_domain_changes_response_200_data_item_subject.additional_properties = d
        return list_domain_changes_response_200_data_item_subject

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
