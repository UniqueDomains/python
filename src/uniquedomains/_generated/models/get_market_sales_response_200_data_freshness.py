from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetMarketSalesResponse200DataFreshness")


@_attrs_define
class GetMarketSalesResponse200DataFreshness:
    """
    Attributes:
        today (datetime.date):
        yesterday (datetime.date):
        rollup_at (datetime.datetime):
    """

    today: datetime.date
    yesterday: datetime.date
    rollup_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        today = self.today.isoformat()

        yesterday = self.yesterday.isoformat()

        rollup_at = self.rollup_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "today": today,
                "yesterday": yesterday,
                "rollupAt": rollup_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        today = datetime.date.fromisoformat(d.pop("today"))

        yesterday = datetime.date.fromisoformat(d.pop("yesterday"))

        rollup_at = datetime.datetime.fromisoformat(d.pop("rollupAt"))

        get_market_sales_response_200_data_freshness = cls(
            today=today,
            yesterday=yesterday,
            rollup_at=rollup_at,
        )

        get_market_sales_response_200_data_freshness.additional_properties = d
        return get_market_sales_response_200_data_freshness

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
