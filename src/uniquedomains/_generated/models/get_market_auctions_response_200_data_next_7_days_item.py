from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetMarketAuctionsResponse200DataNext7DaysItem")


@_attrs_define
class GetMarketAuctionsResponse200DataNext7DaysItem:
    """
    Attributes:
        day (datetime.date):
        closing (int):
    """

    day: datetime.date
    closing: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day.isoformat()

        closing = self.closing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "closing": closing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        day = datetime.date.fromisoformat(d.pop("day"))

        closing = d.pop("closing")

        get_market_auctions_response_200_data_next_7_days_item = cls(
            day=day,
            closing=closing,
        )

        get_market_auctions_response_200_data_next_7_days_item.additional_properties = d
        return get_market_auctions_response_200_data_next_7_days_item

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
