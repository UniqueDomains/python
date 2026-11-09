from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_tld_response_200_data_market_type_0_sales_trend_type_0 import (
    GetTldResponse200DataMarketType0SalesTrendType0,
    check_get_tld_response_200_data_market_type_0_sales_trend_type_0,
)

if TYPE_CHECKING:
    from ..models.get_tld_response_200_data_market_type_0_sales_monthly_type_0 import (
        GetTldResponse200DataMarketType0SalesMonthlyType0,
    )


T = TypeVar("T", bound="GetTldResponse200DataMarketType0")


@_attrs_define
class GetTldResponse200DataMarketType0:
    """
    Attributes:
        computed_at (datetime.datetime): When these figures were computed.
        available_one_word (int): One-word names available on the ending.
        registrations90d (int): Names registered in 90 days among those tracked.
        median_buy (float | None):
        median_renew (float | None):
        cheapest_registrar (None | str):
        sales12m (int): Usable sales, rolling 365 days.
        sales_median_12_m_usd (int | None):
        sales_trend (GetTldResponse200DataMarketType0SalesTrendType0 | None):
        tracked (int): Names tracked on the ending.
        available (int): Tracked names available.
        resell (int): Tracked names listed for resale.
        expiring90d (int): Tracked names expiring within 90 days.
        sales_monthly (GetTldResponse200DataMarketType0SalesMonthlyType0 | None):
    """

    computed_at: datetime.datetime
    available_one_word: int
    registrations90d: int
    median_buy: float | None
    median_renew: float | None
    cheapest_registrar: None | str
    sales12m: int
    sales_median_12_m_usd: int | None
    sales_trend: GetTldResponse200DataMarketType0SalesTrendType0 | None
    tracked: int
    available: int
    resell: int
    expiring90d: int
    sales_monthly: GetTldResponse200DataMarketType0SalesMonthlyType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_tld_response_200_data_market_type_0_sales_monthly_type_0 import (
            GetTldResponse200DataMarketType0SalesMonthlyType0,
        )

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

        tracked = self.tracked

        available = self.available

        resell = self.resell

        expiring90d = self.expiring90d

        sales_monthly: dict[str, Any] | None
        if isinstance(
            self.sales_monthly, GetTldResponse200DataMarketType0SalesMonthlyType0
        ):
            sales_monthly = self.sales_monthly.to_dict()
        else:
            sales_monthly = self.sales_monthly

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
                "tracked": tracked,
                "available": available,
                "resell": resell,
                "expiring90d": expiring90d,
                "salesMonthly": sales_monthly,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_tld_response_200_data_market_type_0_sales_monthly_type_0 import (
            GetTldResponse200DataMarketType0SalesMonthlyType0,
        )

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
        ) -> GetTldResponse200DataMarketType0SalesTrendType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sales_trend_type_0 = (
                    check_get_tld_response_200_data_market_type_0_sales_trend_type_0(
                        data
                    )
                )

                return sales_trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetTldResponse200DataMarketType0SalesTrendType0 | None, data)

        sales_trend = _parse_sales_trend(d.pop("salesTrend"))

        tracked = d.pop("tracked")

        available = d.pop("available")

        resell = d.pop("resell")

        expiring90d = d.pop("expiring90d")

        def _parse_sales_monthly(
            data: object,
        ) -> GetTldResponse200DataMarketType0SalesMonthlyType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sales_monthly_type_0 = (
                    GetTldResponse200DataMarketType0SalesMonthlyType0.from_dict(data)
                )

                return sales_monthly_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetTldResponse200DataMarketType0SalesMonthlyType0 | None, data)

        sales_monthly = _parse_sales_monthly(d.pop("salesMonthly"))

        get_tld_response_200_data_market_type_0 = cls(
            computed_at=computed_at,
            available_one_word=available_one_word,
            registrations90d=registrations90d,
            median_buy=median_buy,
            median_renew=median_renew,
            cheapest_registrar=cheapest_registrar,
            sales12m=sales12m,
            sales_median_12_m_usd=sales_median_12_m_usd,
            sales_trend=sales_trend,
            tracked=tracked,
            available=available,
            resell=resell,
            expiring90d=expiring90d,
            sales_monthly=sales_monthly,
        )

        get_tld_response_200_data_market_type_0.additional_properties = d
        return get_tld_response_200_data_market_type_0

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
