from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListMarketSalesSeriesResponse200DataItem")


@_attrs_define
class ListMarketSalesSeriesResponse200DataItem:
    """
    Attributes:
        period_start (datetime.date):
        count (int):
        mean_usd (int | None):
        median_usd (int | None):
        com_count (int):
        ai_count (int):
    """

    period_start: datetime.date
    count: int
    mean_usd: int | None
    median_usd: int | None
    com_count: int
    ai_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_start = self.period_start.isoformat()

        count = self.count

        mean_usd: int | None
        mean_usd = self.mean_usd

        median_usd: int | None
        median_usd = self.median_usd

        com_count = self.com_count

        ai_count = self.ai_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "periodStart": period_start,
                "count": count,
                "meanUsd": mean_usd,
                "medianUsd": median_usd,
                "comCount": com_count,
                "aiCount": ai_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        period_start = datetime.date.fromisoformat(d.pop("periodStart"))

        count = d.pop("count")

        def _parse_mean_usd(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        mean_usd = _parse_mean_usd(d.pop("meanUsd"))

        def _parse_median_usd(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        median_usd = _parse_median_usd(d.pop("medianUsd"))

        com_count = d.pop("comCount")

        ai_count = d.pop("aiCount")

        list_market_sales_series_response_200_data_item = cls(
            period_start=period_start,
            count=count,
            mean_usd=mean_usd,
            median_usd=median_usd,
            com_count=com_count,
            ai_count=ai_count,
        )

        list_market_sales_series_response_200_data_item.additional_properties = d
        return list_market_sales_series_response_200_data_item

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
