from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListDomainHacksResponse200DataItemCoverageType0")


@_attrs_define
class ListDomainHacksResponse200DataItemCoverageType0:
    """The same word on other endings: available, premium, for sale.

    Attributes:
        available (int | Unset):
        premium (int | Unset):
        for_sale (int | Unset):
        unavailable (int | Unset):
    """

    available: int | Unset = UNSET
    premium: int | Unset = UNSET
    for_sale: int | Unset = UNSET
    unavailable: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available = self.available

        premium = self.premium

        for_sale = self.for_sale

        unavailable = self.unavailable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available is not UNSET:
            field_dict["available"] = available
        if premium is not UNSET:
            field_dict["premium"] = premium
        if for_sale is not UNSET:
            field_dict["forSale"] = for_sale
        if unavailable is not UNSET:
            field_dict["unavailable"] = unavailable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        available = d.pop("available", UNSET)

        premium = d.pop("premium", UNSET)

        for_sale = d.pop("forSale", UNSET)

        unavailable = d.pop("unavailable", UNSET)

        list_domain_hacks_response_200_data_item_coverage_type_0 = cls(
            available=available,
            premium=premium,
            for_sale=for_sale,
            unavailable=unavailable,
        )

        list_domain_hacks_response_200_data_item_coverage_type_0.additional_properties = d
        return list_domain_hacks_response_200_data_item_coverage_type_0

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
