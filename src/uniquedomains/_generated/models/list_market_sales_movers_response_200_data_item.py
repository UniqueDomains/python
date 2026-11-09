from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_market_sales_movers_response_200_data_item_direction import (
    ListMarketSalesMoversResponse200DataItemDirection,
    check_list_market_sales_movers_response_200_data_item_direction,
)

T = TypeVar("T", bound="ListMarketSalesMoversResponse200DataItem")


@_attrs_define
class ListMarketSalesMoversResponse200DataItem:
    """
    Attributes:
        word (str):
        sales30d (int):
        prev30d (int):
        direction (ListMarketSalesMoversResponse200DataItemDirection):
        sales90d (int):
        median_12_m_usd (int | None):
        prev_median_12_m_usd (int | None):
        endings_sold_on (list[str]):
    """

    word: str
    sales30d: int
    prev30d: int
    direction: ListMarketSalesMoversResponse200DataItemDirection
    sales90d: int
    median_12_m_usd: int | None
    prev_median_12_m_usd: int | None
    endings_sold_on: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        word = self.word

        sales30d = self.sales30d

        prev30d = self.prev30d

        direction: str = self.direction

        sales90d = self.sales90d

        median_12_m_usd: int | None
        median_12_m_usd = self.median_12_m_usd

        prev_median_12_m_usd: int | None
        prev_median_12_m_usd = self.prev_median_12_m_usd

        endings_sold_on = self.endings_sold_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "word": word,
                "sales30d": sales30d,
                "prev30d": prev30d,
                "direction": direction,
                "sales90d": sales90d,
                "median12mUsd": median_12_m_usd,
                "prevMedian12mUsd": prev_median_12_m_usd,
                "endingsSoldOn": endings_sold_on,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        word = d.pop("word")

        sales30d = d.pop("sales30d")

        prev30d = d.pop("prev30d")

        direction = check_list_market_sales_movers_response_200_data_item_direction(
            d.pop("direction")
        )

        sales90d = d.pop("sales90d")

        def _parse_median_12_m_usd(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        median_12_m_usd = _parse_median_12_m_usd(d.pop("median12mUsd"))

        def _parse_prev_median_12_m_usd(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        prev_median_12_m_usd = _parse_prev_median_12_m_usd(d.pop("prevMedian12mUsd"))

        endings_sold_on = cast(list[str], d.pop("endingsSoldOn"))

        list_market_sales_movers_response_200_data_item = cls(
            word=word,
            sales30d=sales30d,
            prev30d=prev30d,
            direction=direction,
            sales90d=sales90d,
            median_12_m_usd=median_12_m_usd,
            prev_median_12_m_usd=prev_median_12_m_usd,
            endings_sold_on=endings_sold_on,
        )

        list_market_sales_movers_response_200_data_item.additional_properties = d
        return list_market_sales_movers_response_200_data_item

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
