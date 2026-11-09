from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_name_auction_response_200_data_type_0_currency import (
    GetNameAuctionResponse200DataType0Currency,
    check_get_name_auction_response_200_data_type_0_currency,
)
from ..models.get_name_auction_response_200_data_type_0_venue import (
    GetNameAuctionResponse200DataType0Venue,
    check_get_name_auction_response_200_data_type_0_venue,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNameAuctionResponse200DataType0")


@_attrs_define
class GetNameAuctionResponse200DataType0:
    """
    Attributes:
        venue (GetNameAuctionResponse200DataType0Venue | Unset):
        venue_label (str | Unset):
        ends_at (datetime.datetime | Unset):
        bid (float | None | Unset):
        bid_count (int | None | Unset):
        currency (GetNameAuctionResponse200DataType0Currency | Unset):
        first_year (float | None | Unset):
        bids_jumped (bool | Unset):
    """

    venue: GetNameAuctionResponse200DataType0Venue | Unset = UNSET
    venue_label: str | Unset = UNSET
    ends_at: datetime.datetime | Unset = UNSET
    bid: float | None | Unset = UNSET
    bid_count: int | None | Unset = UNSET
    currency: GetNameAuctionResponse200DataType0Currency | Unset = UNSET
    first_year: float | None | Unset = UNSET
    bids_jumped: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        venue: str | Unset = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue

        venue_label = self.venue_label

        ends_at: str | Unset = UNSET
        if not isinstance(self.ends_at, Unset):
            ends_at = self.ends_at.isoformat()

        bid: float | None | Unset
        if isinstance(self.bid, Unset):
            bid = UNSET
        else:
            bid = self.bid

        bid_count: int | None | Unset
        if isinstance(self.bid_count, Unset):
            bid_count = UNSET
        else:
            bid_count = self.bid_count

        currency: str | Unset = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency

        first_year: float | None | Unset
        if isinstance(self.first_year, Unset):
            first_year = UNSET
        else:
            first_year = self.first_year

        bids_jumped = self.bids_jumped

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if venue is not UNSET:
            field_dict["venue"] = venue
        if venue_label is not UNSET:
            field_dict["venueLabel"] = venue_label
        if ends_at is not UNSET:
            field_dict["endsAt"] = ends_at
        if bid is not UNSET:
            field_dict["bid"] = bid
        if bid_count is not UNSET:
            field_dict["bidCount"] = bid_count
        if currency is not UNSET:
            field_dict["currency"] = currency
        if first_year is not UNSET:
            field_dict["firstYear"] = first_year
        if bids_jumped is not UNSET:
            field_dict["bidsJumped"] = bids_jumped

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _venue = d.pop("venue", UNSET)
        venue: GetNameAuctionResponse200DataType0Venue | Unset
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = check_get_name_auction_response_200_data_type_0_venue(_venue)

        venue_label = d.pop("venueLabel", UNSET)

        _ends_at = d.pop("endsAt", UNSET)
        ends_at: datetime.datetime | Unset
        if isinstance(_ends_at, Unset):
            ends_at = UNSET
        else:
            ends_at = datetime.datetime.fromisoformat(_ends_at)

        def _parse_bid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        bid = _parse_bid(d.pop("bid", UNSET))

        def _parse_bid_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bid_count = _parse_bid_count(d.pop("bidCount", UNSET))

        _currency = d.pop("currency", UNSET)
        currency: GetNameAuctionResponse200DataType0Currency | Unset
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = check_get_name_auction_response_200_data_type_0_currency(
                _currency
            )

        def _parse_first_year(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        first_year = _parse_first_year(d.pop("firstYear", UNSET))

        bids_jumped = d.pop("bidsJumped", UNSET)

        get_name_auction_response_200_data_type_0 = cls(
            venue=venue,
            venue_label=venue_label,
            ends_at=ends_at,
            bid=bid,
            bid_count=bid_count,
            currency=currency,
            first_year=first_year,
            bids_jumped=bids_jumped,
        )

        get_name_auction_response_200_data_type_0.additional_properties = d
        return get_name_auction_response_200_data_type_0

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
