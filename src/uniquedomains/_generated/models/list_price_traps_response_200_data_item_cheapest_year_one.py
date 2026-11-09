from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListPriceTrapsResponse200DataItemCheapestYearOne")


@_attrs_define
class ListPriceTrapsResponse200DataItemCheapestYearOne:
    """
    Attributes:
        registrar (str):
        price (float):
        renewal (float):
    """

    registrar: str
    price: float
    renewal: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registrar = self.registrar

        price = self.price

        renewal = self.renewal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registrar": registrar,
                "price": price,
                "renewal": renewal,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        registrar = d.pop("registrar")

        price = d.pop("price")

        renewal = d.pop("renewal")

        list_price_traps_response_200_data_item_cheapest_year_one = cls(
            registrar=registrar,
            price=price,
            renewal=renewal,
        )

        list_price_traps_response_200_data_item_cheapest_year_one.additional_properties = d
        return list_price_traps_response_200_data_item_cheapest_year_one

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
