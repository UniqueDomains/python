from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_market_auction_outcomes_response_200_data_item_currency import (
    ListMarketAuctionOutcomesResponse200DataItemCurrency,
    check_list_market_auction_outcomes_response_200_data_item_currency,
)
from ..models.list_market_auction_outcomes_response_200_data_item_venue import (
    ListMarketAuctionOutcomesResponse200DataItemVenue,
    check_list_market_auction_outcomes_response_200_data_item_venue,
)

T = TypeVar("T", bound="ListMarketAuctionOutcomesResponse200DataItem")


@_attrs_define
class ListMarketAuctionOutcomesResponse200DataItem:
    """
    Attributes:
        venue (ListMarketAuctionOutcomesResponse200DataItemVenue): Auction venue id (`GET /meta/enums` names each).
        venue_label (str):
        day (datetime.date):
        currency (ListMarketAuctionOutcomesResponse200DataItemCurrency):
        count (int):
        median (float | None):
    """

    venue: ListMarketAuctionOutcomesResponse200DataItemVenue
    venue_label: str
    day: datetime.date
    currency: ListMarketAuctionOutcomesResponse200DataItemCurrency
    count: int
    median: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        venue: str = self.venue

        venue_label = self.venue_label

        day = self.day.isoformat()

        currency: str = self.currency

        count = self.count

        median: float | None
        median = self.median

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "venue": venue,
                "venueLabel": venue_label,
                "day": day,
                "currency": currency,
                "count": count,
                "median": median,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        venue = check_list_market_auction_outcomes_response_200_data_item_venue(
            d.pop("venue")
        )

        venue_label = d.pop("venueLabel")

        day = datetime.date.fromisoformat(d.pop("day"))

        currency = check_list_market_auction_outcomes_response_200_data_item_currency(
            d.pop("currency")
        )

        count = d.pop("count")

        def _parse_median(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        median = _parse_median(d.pop("median"))

        list_market_auction_outcomes_response_200_data_item = cls(
            venue=venue,
            venue_label=venue_label,
            day=day,
            currency=currency,
            count=count,
            median=median,
        )

        list_market_auction_outcomes_response_200_data_item.additional_properties = d
        return list_market_auction_outcomes_response_200_data_item

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
