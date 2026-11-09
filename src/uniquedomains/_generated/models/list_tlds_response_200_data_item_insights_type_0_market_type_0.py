from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_tlds_response_200_data_item_insights_type_0_market_type_0_sales_trend_type_0 import (
    ListTldsResponse200DataItemInsightsType0MarketType0SalesTrendType0,
    check_list_tlds_response_200_data_item_insights_type_0_market_type_0_sales_trend_type_0,
)

T = TypeVar("T", bound="ListTldsResponse200DataItemInsightsType0MarketType0")


@_attrs_define
class ListTldsResponse200DataItemInsightsType0MarketType0:
    """
    Attributes:
        computed_at (datetime.datetime): Timestamp of the rollup.
        available_one_word (int): One-word names available on the ending.
        registrations90d (int): Names registered in 90 days among those tracked.
        median_buy (float | None):
        median_renew (float | None):
        cheapest_registrar (None | str):
        sales12m (int): Usable sales, rolling 365 days.
        sales_median_12_m_usd (int | None):
        sales_trend (ListTldsResponse200DataItemInsightsType0MarketType0SalesTrendType0 | None):
    """

    computed_at: datetime.datetime
    available_one_word: int
    registrations90d: int
    median_buy: float | None
    median_renew: float | None
    cheapest_registrar: None | str
    sales12m: int
    sales_median_12_m_usd: int | None
    sales_trend: (
        ListTldsResponse200DataItemInsightsType0MarketType0SalesTrendType0 | None
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        computed_at = self.computed_at.isoformat()

        available_one_word = self.available_one_word

        registrations90d = self.registrations90d

        median_buy: float | None
        median_buy = self.median_buy

        median_renew: float | None
        median_renew = self.median_renew

        cheapest_registrar: None | str
        cheapest_registrar = self.cheapest_registrar

        sales12m = self.sales12m

        sales_median_12_m_usd: int | None
        sales_median_12_m_usd = self.sales_median_12_m_usd

        sales_trend: None | str
        if isinstance(self.sales_trend, str):
            sales_trend = self.sales_trend
        else:
            sales_trend = self.sales_trend

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "computedAt": computed_at,
                "availableOneWord": available_one_word,
                "registrations90d": registrations90d,
                "medianBuy": median_buy,
                "medianRenew": median_renew,
                "cheapestRegistrar": cheapest_registrar,
                "sales12m": sales12m,
                "salesMedian12mUsd": sales_median_12_m_usd,
                "salesTrend": sales_trend,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        computed_at = datetime.datetime.fromisoformat(d.pop("computedAt"))

        available_one_word = d.pop("availableOneWord")

        registrations90d = d.pop("registrations90d")

        def _parse_median_buy(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        median_buy = _parse_median_buy(d.pop("medianBuy"))

        def _parse_median_renew(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        median_renew = _parse_median_renew(d.pop("medianRenew"))

        def _parse_cheapest_registrar(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cheapest_registrar = _parse_cheapest_registrar(d.pop("cheapestRegistrar"))

        sales12m = d.pop("sales12m")

        def _parse_sales_median_12_m_usd(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sales_median_12_m_usd = _parse_sales_median_12_m_usd(d.pop("salesMedian12mUsd"))

        def _parse_sales_trend(
            data: object,
        ) -> ListTldsResponse200DataItemInsightsType0MarketType0SalesTrendType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sales_trend_type_0 = check_list_tlds_response_200_data_item_insights_type_0_market_type_0_sales_trend_type_0(
                    data
                )

                return sales_trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListTldsResponse200DataItemInsightsType0MarketType0SalesTrendType0
                | None,
                data,
            )

        sales_trend = _parse_sales_trend(d.pop("salesTrend"))

        list_tlds_response_200_data_item_insights_type_0_market_type_0 = cls(
            computed_at=computed_at,
            available_one_word=available_one_word,
            registrations90d=registrations90d,
            median_buy=median_buy,
            median_renew=median_renew,
            cheapest_registrar=cheapest_registrar,
            sales12m=sales12m,
            sales_median_12_m_usd=sales_median_12_m_usd,
            sales_trend=sales_trend,
        )

        list_tlds_response_200_data_item_insights_type_0_market_type_0.additional_properties = d
        return list_tlds_response_200_data_item_insights_type_0_market_type_0

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
