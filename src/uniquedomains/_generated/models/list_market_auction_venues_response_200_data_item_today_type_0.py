from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListMarketAuctionVenuesResponse200DataItemTodayType0")


@_attrs_define
class ListMarketAuctionVenuesResponse200DataItemTodayType0:
    """
    Attributes:
        closing (int | Unset):
        with_bid (int | Unset):
        median_bid_usd (float | None | Unset):
    """

    closing: int | Unset = UNSET
    with_bid: int | Unset = UNSET
    median_bid_usd: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        closing = self.closing

        with_bid = self.with_bid

        median_bid_usd: float | None | Unset
        if isinstance(self.median_bid_usd, Unset):
            median_bid_usd = UNSET
        else:
            median_bid_usd = self.median_bid_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if closing is not UNSET:
            field_dict["closing"] = closing
        if with_bid is not UNSET:
            field_dict["withBid"] = with_bid
        if median_bid_usd is not UNSET:
            field_dict["medianBidUsd"] = median_bid_usd

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        closing = d.pop("closing", UNSET)

        with_bid = d.pop("withBid", UNSET)

        def _parse_median_bid_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        median_bid_usd = _parse_median_bid_usd(d.pop("medianBidUsd", UNSET))

        list_market_auction_venues_response_200_data_item_today_type_0 = cls(
            closing=closing,
            with_bid=with_bid,
            median_bid_usd=median_bid_usd,
        )

        list_market_auction_venues_response_200_data_item_today_type_0.additional_properties = d
        return list_market_auction_venues_response_200_data_item_today_type_0

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
