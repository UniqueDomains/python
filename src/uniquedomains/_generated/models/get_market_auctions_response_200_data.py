from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_market_auctions_response_200_data_by_ending_item import (
        GetMarketAuctionsResponse200DataByEndingItem,
    )
    from ..models.get_market_auctions_response_200_data_by_length_item import (
        GetMarketAuctionsResponse200DataByLengthItem,
    )
    from ..models.get_market_auctions_response_200_data_by_venue_item import (
        GetMarketAuctionsResponse200DataByVenueItem,
    )
    from ..models.get_market_auctions_response_200_data_counts import (
        GetMarketAuctionsResponse200DataCounts,
    )
    from ..models.get_market_auctions_response_200_data_next_7_days_item import (
        GetMarketAuctionsResponse200DataNext7DaysItem,
    )


T = TypeVar("T", bound="GetMarketAuctionsResponse200Data")


@_attrs_define
class GetMarketAuctionsResponse200Data:
    """
    Attributes:
        day (datetime.date | None):
        closing (int | None):
        with_bid (int | None):
        counts (GetMarketAuctionsResponse200DataCounts):
        by_venue (list[GetMarketAuctionsResponse200DataByVenueItem]):
        by_ending (list[GetMarketAuctionsResponse200DataByEndingItem]):
        by_length (list[GetMarketAuctionsResponse200DataByLengthItem]):
        next_7_days (list[GetMarketAuctionsResponse200DataNext7DaysItem]):
    """

    day: datetime.date | None
    closing: int | None
    with_bid: int | None
    counts: GetMarketAuctionsResponse200DataCounts
    by_venue: list[GetMarketAuctionsResponse200DataByVenueItem]
    by_ending: list[GetMarketAuctionsResponse200DataByEndingItem]
    by_length: list[GetMarketAuctionsResponse200DataByLengthItem]
    next_7_days: list[GetMarketAuctionsResponse200DataNext7DaysItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day: None | str
        if isinstance(self.day, datetime.date):
            day = self.day.isoformat()
        else:
            day = self.day

        closing: int | None
        closing = self.closing

        with_bid: int | None
        with_bid = self.with_bid

        counts = self.counts.to_dict()

        by_venue = []
        for by_venue_item_data in self.by_venue:
            by_venue_item = by_venue_item_data.to_dict()
            by_venue.append(by_venue_item)

        by_ending = []
        for by_ending_item_data in self.by_ending:
            by_ending_item = by_ending_item_data.to_dict()
            by_ending.append(by_ending_item)

        by_length = []
        for by_length_item_data in self.by_length:
            by_length_item = by_length_item_data.to_dict()
            by_length.append(by_length_item)

        next_7_days = []
        for next_7_days_item_data in self.next_7_days:
            next_7_days_item = next_7_days_item_data.to_dict()
            next_7_days.append(next_7_days_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "closing": closing,
                "withBid": with_bid,
                "counts": counts,
                "byVenue": by_venue,
                "byEnding": by_ending,
                "byLength": by_length,
                "next7Days": next_7_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_market_auctions_response_200_data_by_ending_item import (
            GetMarketAuctionsResponse200DataByEndingItem,
        )
        from ..models.get_market_auctions_response_200_data_by_length_item import (
            GetMarketAuctionsResponse200DataByLengthItem,
        )
        from ..models.get_market_auctions_response_200_data_by_venue_item import (
            GetMarketAuctionsResponse200DataByVenueItem,
        )
        from ..models.get_market_auctions_response_200_data_counts import (
            GetMarketAuctionsResponse200DataCounts,
        )
        from ..models.get_market_auctions_response_200_data_next_7_days_item import (
            GetMarketAuctionsResponse200DataNext7DaysItem,
        )

        d = dict(src_dict)

        def _parse_day(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                day_type_0 = datetime.date.fromisoformat(data)

                return day_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        day = _parse_day(d.pop("day"))

        def _parse_closing(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        closing = _parse_closing(d.pop("closing"))

        def _parse_with_bid(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        with_bid = _parse_with_bid(d.pop("withBid"))

        counts = GetMarketAuctionsResponse200DataCounts.from_dict(d.pop("counts"))

        by_venue = []
        _by_venue = d.pop("byVenue")
        for by_venue_item_data in _by_venue:
            by_venue_item = GetMarketAuctionsResponse200DataByVenueItem.from_dict(
                by_venue_item_data
            )

            by_venue.append(by_venue_item)

        by_ending = []
        _by_ending = d.pop("byEnding")
        for by_ending_item_data in _by_ending:
            by_ending_item = GetMarketAuctionsResponse200DataByEndingItem.from_dict(
                by_ending_item_data
            )

            by_ending.append(by_ending_item)

        by_length = []
        _by_length = d.pop("byLength")
        for by_length_item_data in _by_length:
            by_length_item = GetMarketAuctionsResponse200DataByLengthItem.from_dict(
                by_length_item_data
            )

            by_length.append(by_length_item)

        next_7_days = []
        _next_7_days = d.pop("next7Days")
        for next_7_days_item_data in _next_7_days:
            next_7_days_item = GetMarketAuctionsResponse200DataNext7DaysItem.from_dict(
                next_7_days_item_data
            )

            next_7_days.append(next_7_days_item)

        get_market_auctions_response_200_data = cls(
            day=day,
            closing=closing,
            with_bid=with_bid,
            counts=counts,
            by_venue=by_venue,
            by_ending=by_ending,
            by_length=by_length,
            next_7_days=next_7_days,
        )

        get_market_auctions_response_200_data.additional_properties = d
        return get_market_auctions_response_200_data

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
