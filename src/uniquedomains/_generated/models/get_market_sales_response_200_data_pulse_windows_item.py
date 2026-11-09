from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_market_sales_response_200_data_pulse_windows_item_id import (
    GetMarketSalesResponse200DataPulseWindowsItemId,
    check_get_market_sales_response_200_data_pulse_windows_item_id,
)

T = TypeVar("T", bound="GetMarketSalesResponse200DataPulseWindowsItem")


@_attrs_define
class GetMarketSalesResponse200DataPulseWindowsItem:
    """
    Attributes:
        id (GetMarketSalesResponse200DataPulseWindowsItemId):
        count (int):
        prev_count (int):
        median_usd (int | None):
        prev_median_usd (int | None):
    """

    id: GetMarketSalesResponse200DataPulseWindowsItemId
    count: int
    prev_count: int
    median_usd: int | None
    prev_median_usd: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str = self.id

        count = self.count

        prev_count = self.prev_count

        median_usd: int | None
        median_usd = self.median_usd

        prev_median_usd: int | None
        prev_median_usd = self.prev_median_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "count": count,
                "prevCount": prev_count,
                "medianUsd": median_usd,
                "prevMedianUsd": prev_median_usd,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = check_get_market_sales_response_200_data_pulse_windows_item_id(d.pop("id"))

        count = d.pop("count")

        prev_count = d.pop("prevCount")

        def _parse_median_usd(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        median_usd = _parse_median_usd(d.pop("medianUsd"))

        def _parse_prev_median_usd(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        prev_median_usd = _parse_prev_median_usd(d.pop("prevMedianUsd"))

        get_market_sales_response_200_data_pulse_windows_item = cls(
            id=id,
            count=count,
            prev_count=prev_count,
            median_usd=median_usd,
            prev_median_usd=prev_median_usd,
        )

        get_market_sales_response_200_data_pulse_windows_item.additional_properties = d
        return get_market_sales_response_200_data_pulse_windows_item

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
