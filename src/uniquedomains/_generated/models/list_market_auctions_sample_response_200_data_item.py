from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_market_auctions_sample_response_200_data_item_currency import (
    ListMarketAuctionsSampleResponse200DataItemCurrency,
    check_list_market_auctions_sample_response_200_data_item_currency,
)
from ..models.list_market_auctions_sample_response_200_data_item_tag_type_1 import (
    ListMarketAuctionsSampleResponse200DataItemTagType1,
    check_list_market_auctions_sample_response_200_data_item_tag_type_1,
)
from ..models.list_market_auctions_sample_response_200_data_item_tag_type_2_type_1 import (
    ListMarketAuctionsSampleResponse200DataItemTagType2Type1,
    check_list_market_auctions_sample_response_200_data_item_tag_type_2_type_1,
)
from ..models.list_market_auctions_sample_response_200_data_item_tag_type_3_type_1 import (
    ListMarketAuctionsSampleResponse200DataItemTagType3Type1,
    check_list_market_auctions_sample_response_200_data_item_tag_type_3_type_1,
)
from ..models.list_market_auctions_sample_response_200_data_item_venue import (
    ListMarketAuctionsSampleResponse200DataItemVenue,
    check_list_market_auctions_sample_response_200_data_item_venue,
)
from ..models.list_market_auctions_sample_response_200_data_item_verdict_type_1 import (
    ListMarketAuctionsSampleResponse200DataItemVerdictType1,
    check_list_market_auctions_sample_response_200_data_item_verdict_type_1,
)
from ..models.list_market_auctions_sample_response_200_data_item_verdict_type_2_type_1 import (
    ListMarketAuctionsSampleResponse200DataItemVerdictType2Type1,
    check_list_market_auctions_sample_response_200_data_item_verdict_type_2_type_1,
)
from ..models.list_market_auctions_sample_response_200_data_item_verdict_type_3_type_1 import (
    ListMarketAuctionsSampleResponse200DataItemVerdictType3Type1,
    check_list_market_auctions_sample_response_200_data_item_verdict_type_3_type_1,
)

T = TypeVar("T", bound="ListMarketAuctionsSampleResponse200DataItem")


@_attrs_define
class ListMarketAuctionsSampleResponse200DataItem:
    """
    Attributes:
        name (str):
        ending (str):
        venue (ListMarketAuctionsSampleResponse200DataItemVenue): Auction venue id (`GET /meta/enums` names each).
        venue_label (str):
        ends_at (datetime.datetime):
        currency (ListMarketAuctionsSampleResponse200DataItemCurrency):
        bid (float | None):
        bid_count (int | None):
        verdict (ListMarketAuctionsSampleResponse200DataItemVerdictType1 |
            ListMarketAuctionsSampleResponse200DataItemVerdictType2Type1 |
            ListMarketAuctionsSampleResponse200DataItemVerdictType3Type1 | None):
        first_year (float | None):
        tag (ListMarketAuctionsSampleResponse200DataItemTagType1 |
            ListMarketAuctionsSampleResponse200DataItemTagType2Type1 |
            ListMarketAuctionsSampleResponse200DataItemTagType3Type1 | None):
    """

    name: str
    ending: str
    venue: ListMarketAuctionsSampleResponse200DataItemVenue
    venue_label: str
    ends_at: datetime.datetime
    currency: ListMarketAuctionsSampleResponse200DataItemCurrency
    bid: float | None
    bid_count: int | None
    verdict: (
        ListMarketAuctionsSampleResponse200DataItemVerdictType1
        | ListMarketAuctionsSampleResponse200DataItemVerdictType2Type1
        | ListMarketAuctionsSampleResponse200DataItemVerdictType3Type1
        | None
    )
    first_year: float | None
    tag: (
        ListMarketAuctionsSampleResponse200DataItemTagType1
        | ListMarketAuctionsSampleResponse200DataItemTagType2Type1
        | ListMarketAuctionsSampleResponse200DataItemTagType3Type1
        | None
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        ending = self.ending

        venue: str = self.venue

        venue_label = self.venue_label

        ends_at = self.ends_at.isoformat()

        currency: str = self.currency

        bid: float | None
        bid = self.bid

        bid_count: int | None
        bid_count = self.bid_count

        verdict: None | str
        if (
            isinstance(self.verdict, str)
            or isinstance(self.verdict, str)
            or isinstance(self.verdict, str)
        ):
            verdict = self.verdict
        else:
            verdict = self.verdict

        first_year: float | None
        first_year = self.first_year

        tag: None | str
        if (
            isinstance(self.tag, str)
            or isinstance(self.tag, str)
            or isinstance(self.tag, str)
        ):
            tag = self.tag
        else:
            tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "ending": ending,
                "venue": venue,
                "venueLabel": venue_label,
                "endsAt": ends_at,
                "currency": currency,
                "bid": bid,
                "bidCount": bid_count,
                "verdict": verdict,
                "firstYear": first_year,
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        ending = d.pop("ending")

        venue = check_list_market_auctions_sample_response_200_data_item_venue(
            d.pop("venue")
        )

        venue_label = d.pop("venueLabel")

        ends_at = datetime.datetime.fromisoformat(d.pop("endsAt"))

        currency = check_list_market_auctions_sample_response_200_data_item_currency(
            d.pop("currency")
        )

        def _parse_bid(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        bid = _parse_bid(d.pop("bid"))

        def _parse_bid_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        bid_count = _parse_bid_count(d.pop("bidCount"))

        def _parse_verdict(
            data: object,
        ) -> (
            ListMarketAuctionsSampleResponse200DataItemVerdictType1
            | ListMarketAuctionsSampleResponse200DataItemVerdictType2Type1
            | ListMarketAuctionsSampleResponse200DataItemVerdictType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verdict_type_1 = check_list_market_auctions_sample_response_200_data_item_verdict_type_1(
                    data
                )

                return verdict_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verdict_type_2_type_1 = check_list_market_auctions_sample_response_200_data_item_verdict_type_2_type_1(
                    data
                )

                return verdict_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verdict_type_3_type_1 = check_list_market_auctions_sample_response_200_data_item_verdict_type_3_type_1(
                    data
                )

                return verdict_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListMarketAuctionsSampleResponse200DataItemVerdictType1
                | ListMarketAuctionsSampleResponse200DataItemVerdictType2Type1
                | ListMarketAuctionsSampleResponse200DataItemVerdictType3Type1
                | None,
                data,
            )

        verdict = _parse_verdict(d.pop("verdict"))

        def _parse_first_year(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        first_year = _parse_first_year(d.pop("firstYear"))

        def _parse_tag(
            data: object,
        ) -> (
            ListMarketAuctionsSampleResponse200DataItemTagType1
            | ListMarketAuctionsSampleResponse200DataItemTagType2Type1
            | ListMarketAuctionsSampleResponse200DataItemTagType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tag_type_1 = (
                    check_list_market_auctions_sample_response_200_data_item_tag_type_1(
                        data
                    )
                )

                return tag_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tag_type_2_type_1 = check_list_market_auctions_sample_response_200_data_item_tag_type_2_type_1(
                    data
                )

                return tag_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tag_type_3_type_1 = check_list_market_auctions_sample_response_200_data_item_tag_type_3_type_1(
                    data
                )

                return tag_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListMarketAuctionsSampleResponse200DataItemTagType1
                | ListMarketAuctionsSampleResponse200DataItemTagType2Type1
                | ListMarketAuctionsSampleResponse200DataItemTagType3Type1
                | None,
                data,
            )

        tag = _parse_tag(d.pop("tag"))

        list_market_auctions_sample_response_200_data_item = cls(
            name=name,
            ending=ending,
            venue=venue,
            venue_label=venue_label,
            ends_at=ends_at,
            currency=currency,
            bid=bid,
            bid_count=bid_count,
            verdict=verdict,
            first_year=first_year,
            tag=tag,
        )

        list_market_auctions_sample_response_200_data_item.additional_properties = d
        return list_market_auctions_sample_response_200_data_item

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
