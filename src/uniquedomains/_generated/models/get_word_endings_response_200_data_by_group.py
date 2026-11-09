from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWordEndingsResponse200DataByGroup")


@_attrs_define
class GetWordEndingsResponse200DataByGroup:
    """
    Attributes:
        scanned (int | Unset):
        taken (int | Unset):
        available (int | Unset):
        for_sale (int | Unset):
    """

    scanned: int | Unset = UNSET
    taken: int | Unset = UNSET
    available: int | Unset = UNSET
    for_sale: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scanned = self.scanned

        taken = self.taken

        available = self.available

        for_sale = self.for_sale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scanned is not UNSET:
            field_dict["scanned"] = scanned
        if taken is not UNSET:
            field_dict["taken"] = taken
        if available is not UNSET:
            field_dict["available"] = available
        if for_sale is not UNSET:
            field_dict["forSale"] = for_sale

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        scanned = d.pop("scanned", UNSET)

        taken = d.pop("taken", UNSET)

        available = d.pop("available", UNSET)

        for_sale = d.pop("forSale", UNSET)

        get_word_endings_response_200_data_by_group = cls(
            scanned=scanned,
            taken=taken,
            available=available,
            for_sale=for_sale,
        )

        get_word_endings_response_200_data_by_group.additional_properties = d
        return get_word_endings_response_200_data_by_group

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
