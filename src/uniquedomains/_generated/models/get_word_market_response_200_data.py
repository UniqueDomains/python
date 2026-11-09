from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_word_market_response_200_data_open_auctions_by_ending import (
        GetWordMarketResponse200DataOpenAuctionsByEnding,
    )


T = TypeVar("T", bound="GetWordMarketResponse200Data")


@_attrs_define
class GetWordMarketResponse200Data:
    """
    Attributes:
        sales12m (int | Unset):
        sales30d (int | Unset):
        median_from_three (int | None | Unset): USD, only from 3 sales.
        endings_sold_on (int | Unset):
        open_auctions_by_ending (GetWordMarketResponse200DataOpenAuctionsByEnding | Unset): `{ ending: count }`.
    """

    sales12m: int | Unset = UNSET
    sales30d: int | Unset = UNSET
    median_from_three: int | None | Unset = UNSET
    endings_sold_on: int | Unset = UNSET
    open_auctions_by_ending: (
        GetWordMarketResponse200DataOpenAuctionsByEnding | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sales12m = self.sales12m

        sales30d = self.sales30d

        median_from_three: int | None | Unset
        if isinstance(self.median_from_three, Unset):
            median_from_three = UNSET
        else:
            median_from_three = self.median_from_three

        endings_sold_on = self.endings_sold_on

        open_auctions_by_ending: dict[str, Any] | Unset = UNSET
        if not isinstance(self.open_auctions_by_ending, Unset):
            open_auctions_by_ending = self.open_auctions_by_ending.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sales12m is not UNSET:
            field_dict["sales12m"] = sales12m
        if sales30d is not UNSET:
            field_dict["sales30d"] = sales30d
        if median_from_three is not UNSET:
            field_dict["medianFromThree"] = median_from_three
        if endings_sold_on is not UNSET:
            field_dict["endingsSoldOn"] = endings_sold_on
        if open_auctions_by_ending is not UNSET:
            field_dict["openAuctionsByEnding"] = open_auctions_by_ending

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_word_market_response_200_data_open_auctions_by_ending import (
            GetWordMarketResponse200DataOpenAuctionsByEnding,
        )

        d = dict(src_dict)
        sales12m = d.pop("sales12m", UNSET)

        sales30d = d.pop("sales30d", UNSET)

        def _parse_median_from_three(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        median_from_three = _parse_median_from_three(d.pop("medianFromThree", UNSET))

        endings_sold_on = d.pop("endingsSoldOn", UNSET)

        _open_auctions_by_ending = d.pop("openAuctionsByEnding", UNSET)
        open_auctions_by_ending: (
            GetWordMarketResponse200DataOpenAuctionsByEnding | Unset
        )
        if isinstance(_open_auctions_by_ending, Unset):
            open_auctions_by_ending = UNSET
        else:
            open_auctions_by_ending = (
                GetWordMarketResponse200DataOpenAuctionsByEnding.from_dict(
                    _open_auctions_by_ending
                )
            )

        get_word_market_response_200_data = cls(
            sales12m=sales12m,
            sales30d=sales30d,
            median_from_three=median_from_three,
            endings_sold_on=endings_sold_on,
            open_auctions_by_ending=open_auctions_by_ending,
        )

        get_word_market_response_200_data.additional_properties = d
        return get_word_market_response_200_data

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
