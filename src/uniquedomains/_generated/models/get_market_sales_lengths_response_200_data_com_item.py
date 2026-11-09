from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_market_sales_lengths_response_200_data_com_item_trend_word import (
    GetMarketSalesLengthsResponse200DataComItemTrendWord,
    check_get_market_sales_lengths_response_200_data_com_item_trend_word,
)

T = TypeVar("T", bound="GetMarketSalesLengthsResponse200DataComItem")


@_attrs_define
class GetMarketSalesLengthsResponse200DataComItem:
    """
    Attributes:
        length (int):
        count12m (int):
        median_12_m_usd (int | None):
        prev_median_12_m_usd (int | None):
        trend_word (GetMarketSalesLengthsResponse200DataComItemTrendWord):
        count30d (int):
        median_30_d_usd (int | None):
    """

    length: int
    count12m: int
    median_12_m_usd: int | None
    prev_median_12_m_usd: int | None
    trend_word: GetMarketSalesLengthsResponse200DataComItemTrendWord
    count30d: int
    median_30_d_usd: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        length = self.length

        count12m = self.count12m

        median_12_m_usd: int | None
        median_12_m_usd = self.median_12_m_usd

        prev_median_12_m_usd: int | None
        prev_median_12_m_usd = self.prev_median_12_m_usd

        trend_word: str = self.trend_word

        count30d = self.count30d

        median_30_d_usd: int | None
        median_30_d_usd = self.median_30_d_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "length": length,
                "count12m": count12m,
                "median12mUsd": median_12_m_usd,
                "prevMedian12mUsd": prev_median_12_m_usd,
                "trendWord": trend_word,
                "count30d": count30d,
                "median30dUsd": median_30_d_usd,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        length = d.pop("length")

        count12m = d.pop("count12m")

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

        trend_word = (
            check_get_market_sales_lengths_response_200_data_com_item_trend_word(
                d.pop("trendWord")
            )
        )

        count30d = d.pop("count30d")

        def _parse_median_30_d_usd(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        median_30_d_usd = _parse_median_30_d_usd(d.pop("median30dUsd"))

        get_market_sales_lengths_response_200_data_com_item = cls(
            length=length,
            count12m=count12m,
            median_12_m_usd=median_12_m_usd,
            prev_median_12_m_usd=prev_median_12_m_usd,
            trend_word=trend_word,
            count30d=count30d,
            median_30_d_usd=median_30_d_usd,
        )

        get_market_sales_lengths_response_200_data_com_item.additional_properties = d
        return get_market_sales_lengths_response_200_data_com_item

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
