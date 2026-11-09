from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetRegistrarFootprintResponse200DataTopEndingsItem")


@_attrs_define
class GetRegistrarFootprintResponse200DataTopEndingsItem:
    """
    Attributes:
        ending (str):
        names (int): Rounded count on the ending.
    """

    ending: str
    names: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ending = self.ending

        names = self.names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ending": ending,
                "names": names,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ending = d.pop("ending")

        names = d.pop("names")

        get_registrar_footprint_response_200_data_top_endings_item = cls(
            ending=ending,
            names=names,
        )

        get_registrar_footprint_response_200_data_top_endings_item.additional_properties = d
        return get_registrar_footprint_response_200_data_top_endings_item

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
