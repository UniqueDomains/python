from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_market_sales_lengths_response_200_data_ai_item import (
        GetMarketSalesLengthsResponse200DataAiItem,
    )
    from ..models.get_market_sales_lengths_response_200_data_co_item import (
        GetMarketSalesLengthsResponse200DataCoItem,
    )
    from ..models.get_market_sales_lengths_response_200_data_com_item import (
        GetMarketSalesLengthsResponse200DataComItem,
    )
    from ..models.get_market_sales_lengths_response_200_data_io_item import (
        GetMarketSalesLengthsResponse200DataIoItem,
    )


T = TypeVar("T", bound="GetMarketSalesLengthsResponse200Data")


@_attrs_define
class GetMarketSalesLengthsResponse200Data:
    """
    Attributes:
        com (list[GetMarketSalesLengthsResponse200DataComItem]):
        ai (list[GetMarketSalesLengthsResponse200DataAiItem]):
        io (list[GetMarketSalesLengthsResponse200DataIoItem]):
        co (list[GetMarketSalesLengthsResponse200DataCoItem]):
    """

    com: list[GetMarketSalesLengthsResponse200DataComItem]
    ai: list[GetMarketSalesLengthsResponse200DataAiItem]
    io: list[GetMarketSalesLengthsResponse200DataIoItem]
    co: list[GetMarketSalesLengthsResponse200DataCoItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        com = []
        for com_item_data in self.com:
            com_item = com_item_data.to_dict()
            com.append(com_item)

        ai = []
        for ai_item_data in self.ai:
            ai_item = ai_item_data.to_dict()
            ai.append(ai_item)

        io = []
        for io_item_data in self.io:
            io_item = io_item_data.to_dict()
            io.append(io_item)

        co = []
        for co_item_data in self.co:
            co_item = co_item_data.to_dict()
            co.append(co_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "com": com,
                "ai": ai,
                "io": io,
                "co": co,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_market_sales_lengths_response_200_data_ai_item import (
            GetMarketSalesLengthsResponse200DataAiItem,
        )
        from ..models.get_market_sales_lengths_response_200_data_co_item import (
            GetMarketSalesLengthsResponse200DataCoItem,
        )
        from ..models.get_market_sales_lengths_response_200_data_com_item import (
            GetMarketSalesLengthsResponse200DataComItem,
        )
        from ..models.get_market_sales_lengths_response_200_data_io_item import (
            GetMarketSalesLengthsResponse200DataIoItem,
        )

        d = dict(src_dict)
        com = []
        _com = d.pop("com")
        for com_item_data in _com:
            com_item = GetMarketSalesLengthsResponse200DataComItem.from_dict(
                com_item_data
            )

            com.append(com_item)

        ai = []
        _ai = d.pop("ai")
        for ai_item_data in _ai:
            ai_item = GetMarketSalesLengthsResponse200DataAiItem.from_dict(ai_item_data)

            ai.append(ai_item)

        io = []
        _io = d.pop("io")
        for io_item_data in _io:
            io_item = GetMarketSalesLengthsResponse200DataIoItem.from_dict(io_item_data)

            io.append(io_item)

        co = []
        _co = d.pop("co")
        for co_item_data in _co:
            co_item = GetMarketSalesLengthsResponse200DataCoItem.from_dict(co_item_data)

            co.append(co_item)

        get_market_sales_lengths_response_200_data = cls(
            com=com,
            ai=ai,
            io=io,
            co=co,
        )

        get_market_sales_lengths_response_200_data.additional_properties = d
        return get_market_sales_lengths_response_200_data

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
