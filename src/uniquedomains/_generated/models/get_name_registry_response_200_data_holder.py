from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNameRegistryResponse200DataHolder")


@_attrs_define
class GetNameRegistryResponse200DataHolder:
    """
    Attributes:
        holder (None | str | Unset):
        redacted_by (None | str | Unset):
        held_at_registrar (bool | Unset):
    """

    holder: None | str | Unset = UNSET
    redacted_by: None | str | Unset = UNSET
    held_at_registrar: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        holder: None | str | Unset
        if isinstance(self.holder, Unset):
            holder = UNSET
        else:
            holder = self.holder

        redacted_by: None | str | Unset
        if isinstance(self.redacted_by, Unset):
            redacted_by = UNSET
        else:
            redacted_by = self.redacted_by

        held_at_registrar = self.held_at_registrar

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if holder is not UNSET:
            field_dict["holder"] = holder
        if redacted_by is not UNSET:
            field_dict["redactedBy"] = redacted_by
        if held_at_registrar is not UNSET:
            field_dict["heldAtRegistrar"] = held_at_registrar

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_holder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        holder = _parse_holder(d.pop("holder", UNSET))

        def _parse_redacted_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        redacted_by = _parse_redacted_by(d.pop("redactedBy", UNSET))

        held_at_registrar = d.pop("heldAtRegistrar", UNSET)

        get_name_registry_response_200_data_holder = cls(
            holder=holder,
            redacted_by=redacted_by,
            held_at_registrar=held_at_registrar,
        )

        get_name_registry_response_200_data_holder.additional_properties = d
        return get_name_registry_response_200_data_holder

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
