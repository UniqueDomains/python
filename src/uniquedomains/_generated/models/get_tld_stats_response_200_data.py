from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_tld_stats_response_200_data_sales_trend_type_0 import (
    GetTldStatsResponse200DataSalesTrendType0,
    check_get_tld_stats_response_200_data_sales_trend_type_0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_tld_stats_response_200_data_history_item import (
        GetTldStatsResponse200DataHistoryItem,
    )
    from ..models.get_tld_stats_response_200_data_panel_type_0 import (
        GetTldStatsResponse200DataPanelType0,
    )
    from ..models.get_tld_stats_response_200_data_sales_monthly_type_0 import (
        GetTldStatsResponse200DataSalesMonthlyType0,
    )


T = TypeVar("T", bound="GetTldStatsResponse200Data")


@_attrs_define
class GetTldStatsResponse200Data:
    """
    Attributes:
        tld (str): Bare ending.
        day (datetime.date): The day of these figures.
        computed_at (datetime.datetime | None):
        tracked (int):
        available (int):
        available_one_word (int):
        resell (int):
        expiring90d (int):
        registrations90d (int):
        median_buy (float | None):
        median_renew (float | None):
        cheapest_registrar (None | str):
        sales12m (int): Usable sales, 365 days.
        sales_prev_12_m (int): The 365 days before.
        sales_median_12_m (int | None):
        sales_trend (GetTldStatsResponse200DataSalesTrendType0 | None):
        sales_monthly (GetTldStatsResponse200DataSalesMonthlyType0 | None):
        sales30d (int): Usable sales, 30 days.
        sales_median_30_d (int | None):
        sales_median_prev_12_m (int | None):
        panel (GetTldStatsResponse200DataPanelType0 | None):
        history (list[GetTldStatsResponse200DataHistoryItem] | Unset):
    """

    tld: str
    day: datetime.date
    computed_at: datetime.datetime | None
    tracked: int
    available: int
    available_one_word: int
    resell: int
    expiring90d: int
    registrations90d: int
    median_buy: float | None
    median_renew: float | None
    cheapest_registrar: None | str
    sales12m: int
    sales_prev_12_m: int
    sales_median_12_m: int | None
    sales_trend: GetTldStatsResponse200DataSalesTrendType0 | None
    sales_monthly: GetTldStatsResponse200DataSalesMonthlyType0 | None
    sales30d: int
    sales_median_30_d: int | None
    sales_median_prev_12_m: int | None
    panel: GetTldStatsResponse200DataPanelType0 | None
    history: list[GetTldStatsResponse200DataHistoryItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_tld_stats_response_200_data_panel_type_0 import (
            GetTldStatsResponse200DataPanelType0,
        )
        from ..models.get_tld_stats_response_200_data_sales_monthly_type_0 import (
            GetTldStatsResponse200DataSalesMonthlyType0,
        )

        tld = self.tld

        day = self.day.isoformat()

        computed_at: None | str
        if isinstance(self.computed_at, datetime.datetime):
            computed_at = self.computed_at.isoformat()
        else:
            computed_at = self.computed_at

        tracked = self.tracked

        available = self.available

        available_one_word = self.available_one_word

        resell = self.resell

        expiring90d = self.expiring90d

        registrations90d = self.registrations90d

        median_buy: float | None
        median_buy = self.median_buy

        median_renew: float | None
        median_renew = self.median_renew

        cheapest_registrar: None | str
        cheapest_registrar = self.cheapest_registrar

        sales12m = self.sales12m

        sales_prev_12_m = self.sales_prev_12_m

        sales_median_12_m: int | None
        sales_median_12_m = self.sales_median_12_m

        sales_trend: None | str
        if isinstance(self.sales_trend, str):
            sales_trend = self.sales_trend
        else:
            sales_trend = self.sales_trend

        sales_monthly: dict[str, Any] | None
        if isinstance(self.sales_monthly, GetTldStatsResponse200DataSalesMonthlyType0):
            sales_monthly = self.sales_monthly.to_dict()
        else:
            sales_monthly = self.sales_monthly

        sales30d = self.sales30d

        sales_median_30_d: int | None
        sales_median_30_d = self.sales_median_30_d

        sales_median_prev_12_m: int | None
        sales_median_prev_12_m = self.sales_median_prev_12_m

        panel: dict[str, Any] | None
        if isinstance(self.panel, GetTldStatsResponse200DataPanelType0):
            panel = self.panel.to_dict()
        else:
            panel = self.panel

        history: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tld": tld,
                "day": day,
                "computedAt": computed_at,
                "tracked": tracked,
                "available": available,
                "availableOneWord": available_one_word,
                "resell": resell,
                "expiring90d": expiring90d,
                "registrations90d": registrations90d,
                "medianBuy": median_buy,
                "medianRenew": median_renew,
                "cheapestRegistrar": cheapest_registrar,
                "sales12m": sales12m,
                "salesPrev12m": sales_prev_12_m,
                "salesMedian12m": sales_median_12_m,
                "salesTrend": sales_trend,
                "salesMonthly": sales_monthly,
                "sales30d": sales30d,
                "salesMedian30d": sales_median_30_d,
                "salesMedianPrev12m": sales_median_prev_12_m,
                "panel": panel,
            }
        )
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_tld_stats_response_200_data_history_item import (
            GetTldStatsResponse200DataHistoryItem,
        )
        from ..models.get_tld_stats_response_200_data_panel_type_0 import (
            GetTldStatsResponse200DataPanelType0,
        )
        from ..models.get_tld_stats_response_200_data_sales_monthly_type_0 import (
            GetTldStatsResponse200DataSalesMonthlyType0,
        )

        d = dict(src_dict)
        tld = d.pop("tld")

        day = datetime.date.fromisoformat(d.pop("day"))

        def _parse_computed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                computed_at_type_0 = datetime.datetime.fromisoformat(data)

                return computed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        computed_at = _parse_computed_at(d.pop("computedAt"))

        tracked = d.pop("tracked")

        available = d.pop("available")

        available_one_word = d.pop("availableOneWord")

        resell = d.pop("resell")

        expiring90d = d.pop("expiring90d")

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

        sales_prev_12_m = d.pop("salesPrev12m")

        def _parse_sales_median_12_m(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sales_median_12_m = _parse_sales_median_12_m(d.pop("salesMedian12m"))

        def _parse_sales_trend(
            data: object,
        ) -> GetTldStatsResponse200DataSalesTrendType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sales_trend_type_0 = (
                    check_get_tld_stats_response_200_data_sales_trend_type_0(data)
                )

                return sales_trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetTldStatsResponse200DataSalesTrendType0 | None, data)

        sales_trend = _parse_sales_trend(d.pop("salesTrend"))

        def _parse_sales_monthly(
            data: object,
        ) -> GetTldStatsResponse200DataSalesMonthlyType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sales_monthly_type_0 = (
                    GetTldStatsResponse200DataSalesMonthlyType0.from_dict(data)
                )

                return sales_monthly_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetTldStatsResponse200DataSalesMonthlyType0 | None, data)

        sales_monthly = _parse_sales_monthly(d.pop("salesMonthly"))

        sales30d = d.pop("sales30d")

        def _parse_sales_median_30_d(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sales_median_30_d = _parse_sales_median_30_d(d.pop("salesMedian30d"))

        def _parse_sales_median_prev_12_m(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sales_median_prev_12_m = _parse_sales_median_prev_12_m(
            d.pop("salesMedianPrev12m")
        )

        def _parse_panel(data: object) -> GetTldStatsResponse200DataPanelType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                panel_type_0 = GetTldStatsResponse200DataPanelType0.from_dict(data)

                return panel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetTldStatsResponse200DataPanelType0 | None, data)

        panel = _parse_panel(d.pop("panel"))

        _history = d.pop("history", UNSET)
        history: list[GetTldStatsResponse200DataHistoryItem] | Unset = UNSET
        if _history is not UNSET:
            history = []
            for history_item_data in _history:
                history_item = GetTldStatsResponse200DataHistoryItem.from_dict(
                    history_item_data
                )

                history.append(history_item)

        get_tld_stats_response_200_data = cls(
            tld=tld,
            day=day,
            computed_at=computed_at,
            tracked=tracked,
            available=available,
            available_one_word=available_one_word,
            resell=resell,
            expiring90d=expiring90d,
            registrations90d=registrations90d,
            median_buy=median_buy,
            median_renew=median_renew,
            cheapest_registrar=cheapest_registrar,
            sales12m=sales12m,
            sales_prev_12_m=sales_prev_12_m,
            sales_median_12_m=sales_median_12_m,
            sales_trend=sales_trend,
            sales_monthly=sales_monthly,
            sales30d=sales30d,
            sales_median_30_d=sales_median_30_d,
            sales_median_prev_12_m=sales_median_prev_12_m,
            panel=panel,
            history=history,
        )

        get_tld_stats_response_200_data.additional_properties = d
        return get_tld_stats_response_200_data

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
