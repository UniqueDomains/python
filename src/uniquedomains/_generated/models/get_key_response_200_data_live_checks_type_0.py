from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetKeyResponse200DataLiveChecksType0")


@_attrs_define
class GetKeyResponse200DataLiveChecksType0:
    """
    Attributes:
        used (int):
        allowance (int):
    """

    used: int
    allowance: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used = self.used

        allowance = self.allowance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "used": used,
                "allowance": allowance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        used = d.pop("used")

        allowance = d.pop("allowance")

        get_key_response_200_data_live_checks_type_0 = cls(
            used=used,
            allowance=allowance,
        )

        get_key_response_200_data_live_checks_type_0.additional_properties = d
        return get_key_response_200_data_live_checks_type_0

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
