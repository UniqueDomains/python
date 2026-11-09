from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.batch_names_response_200_data_item_type_2_error import (
    BatchNamesResponse200DataItemType2Error,
    check_batch_names_response_200_data_item_type_2_error,
)

T = TypeVar("T", bound="BatchNamesResponse200DataItemType2")


@_attrs_define
class BatchNamesResponse200DataItemType2:
    """
    Attributes:
        name (str):
        error (BatchNamesResponse200DataItemType2Error):
    """

    name: str
    error: BatchNamesResponse200DataItemType2Error
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        error: str = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        error = check_batch_names_response_200_data_item_type_2_error(d.pop("error"))

        batch_names_response_200_data_item_type_2 = cls(
            name=name,
            error=error,
        )

        batch_names_response_200_data_item_type_2.additional_properties = d
        return batch_names_response_200_data_item_type_2

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
