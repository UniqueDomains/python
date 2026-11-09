from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetMarketAuctionsResponse200DataCounts")


@_attrs_define
class GetMarketAuctionsResponse200DataCounts:
    """
    Attributes:
        today (int):
        results (int):
        all_ (int):
    """

    today: int
    results: int
    all_: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        today = self.today

        results = self.results

        all_ = self.all_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "today": today,
                "results": results,
                "all": all_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        today = d.pop("today")

        results = d.pop("results")

        all_ = d.pop("all")

        get_market_auctions_response_200_data_counts = cls(
            today=today,
            results=results,
            all_=all_,
        )

        get_market_auctions_response_200_data_counts.additional_properties = d
        return get_market_auctions_response_200_data_counts

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
