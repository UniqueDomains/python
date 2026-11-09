from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetMarketAuctionsResponse200DataByEndingItem")


@_attrs_define
class GetMarketAuctionsResponse200DataByEndingItem:
    """
    Attributes:
        ending (str):
        closing (int):
        with_bid (int):
        median_bid_usd (float | None):
    """

    ending: str
    closing: int
    with_bid: int
    median_bid_usd: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ending = self.ending

        closing = self.closing

        with_bid = self.with_bid

        median_bid_usd: float | None
        median_bid_usd = self.median_bid_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ending": ending,
                "closing": closing,
                "withBid": with_bid,
                "medianBidUsd": median_bid_usd,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ending = d.pop("ending")

        closing = d.pop("closing")

        with_bid = d.pop("withBid")

        def _parse_median_bid_usd(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        median_bid_usd = _parse_median_bid_usd(d.pop("medianBidUsd"))

        get_market_auctions_response_200_data_by_ending_item = cls(
            ending=ending,
            closing=closing,
            with_bid=with_bid,
            median_bid_usd=median_bid_usd,
        )

        get_market_auctions_response_200_data_by_ending_item.additional_properties = d
        return get_market_auctions_response_200_data_by_ending_item

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
