from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_meta_enums_response_200_data_parking_services_item_kind import (
    GetMetaEnumsResponse200DataParkingServicesItemKind,
    check_get_meta_enums_response_200_data_parking_services_item_kind,
)

T = TypeVar("T", bound="GetMetaEnumsResponse200DataParkingServicesItem")


@_attrs_define
class GetMetaEnumsResponse200DataParkingServicesItem:
    """
    Attributes:
        id (str):
        label (str):
        kind (GetMetaEnumsResponse200DataParkingServicesItemKind):
    """

    id: str
    label: str
    kind: GetMetaEnumsResponse200DataParkingServicesItemKind
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        kind: str = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        kind = check_get_meta_enums_response_200_data_parking_services_item_kind(
            d.pop("kind")
        )

        get_meta_enums_response_200_data_parking_services_item = cls(
            id=id,
            label=label,
            kind=kind,
        )

        get_meta_enums_response_200_data_parking_services_item.additional_properties = d
        return get_meta_enums_response_200_data_parking_services_item

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
