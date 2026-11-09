from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_name_prices_response_200_data_quotes_item import (
        GetNamePricesResponse200DataQuotesItem,
    )


T = TypeVar("T", bound="GetNamePricesResponse200Data")


@_attrs_define
class GetNamePricesResponse200Data:
    """
    Attributes:
        quotes (list[GetNamePricesResponse200DataQuotesItem]):
        trap (bool):
    """

    quotes: list[GetNamePricesResponse200DataQuotesItem]
    trap: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quotes = []
        for quotes_item_data in self.quotes:
            quotes_item = quotes_item_data.to_dict()
            quotes.append(quotes_item)

        trap = self.trap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quotes": quotes,
                "trap": trap,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_name_prices_response_200_data_quotes_item import (
            GetNamePricesResponse200DataQuotesItem,
        )

        d = dict(src_dict)
        quotes = []
        _quotes = d.pop("quotes")
        for quotes_item_data in _quotes:
            quotes_item = GetNamePricesResponse200DataQuotesItem.from_dict(
                quotes_item_data
            )

            quotes.append(quotes_item)

        trap = d.pop("trap")

        get_name_prices_response_200_data = cls(
            quotes=quotes,
            trap=trap,
        )

        get_name_prices_response_200_data.additional_properties = d
        return get_name_prices_response_200_data

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
