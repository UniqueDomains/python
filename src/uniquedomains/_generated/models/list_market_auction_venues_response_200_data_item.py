from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_market_auction_venues_response_200_data_item_currency import (
    ListMarketAuctionVenuesResponse200DataItemCurrency,
    check_list_market_auction_venues_response_200_data_item_currency,
)
from ..models.list_market_auction_venues_response_200_data_item_id import (
    ListMarketAuctionVenuesResponse200DataItemId,
    check_list_market_auction_venues_response_200_data_item_id,
)
from ..models.list_market_auction_venues_response_200_data_item_kinds_item import (
    ListMarketAuctionVenuesResponse200DataItemKindsItem,
    check_list_market_auction_venues_response_200_data_item_kinds_item,
)

if TYPE_CHECKING:
    from ..models.list_market_auction_venues_response_200_data_item_bidder_rule_type_0 import (
        ListMarketAuctionVenuesResponse200DataItemBidderRuleType0,
    )
    from ..models.list_market_auction_venues_response_200_data_item_close_rule_type_0 import (
        ListMarketAuctionVenuesResponse200DataItemCloseRuleType0,
    )
    from ..models.list_market_auction_venues_response_200_data_item_first_year import (
        ListMarketAuctionVenuesResponse200DataItemFirstYear,
    )
    from ..models.list_market_auction_venues_response_200_data_item_payment_rule_type_0 import (
        ListMarketAuctionVenuesResponse200DataItemPaymentRuleType0,
    )
    from ..models.list_market_auction_venues_response_200_data_item_today_type_0 import (
        ListMarketAuctionVenuesResponse200DataItemTodayType0,
    )


T = TypeVar("T", bound="ListMarketAuctionVenuesResponse200DataItem")


@_attrs_define
class ListMarketAuctionVenuesResponse200DataItem:
    """
    Attributes:
        id (ListMarketAuctionVenuesResponse200DataItemId): Auction venue id (`GET /meta/enums` names each).
        label (str):
        currency (ListMarketAuctionVenuesResponse200DataItemCurrency):
        kinds (list[ListMarketAuctionVenuesResponse200DataItemKindsItem]):
        close_rule (ListMarketAuctionVenuesResponse200DataItemCloseRuleType0 | None):
        payment_rule (ListMarketAuctionVenuesResponse200DataItemPaymentRuleType0 | None):
        bidder_rule (ListMarketAuctionVenuesResponse200DataItemBidderRuleType0 | None):
        first_year (ListMarketAuctionVenuesResponse200DataItemFirstYear):
        today (ListMarketAuctionVenuesResponse200DataItemTodayType0 | None):
    """

    id: ListMarketAuctionVenuesResponse200DataItemId
    label: str
    currency: ListMarketAuctionVenuesResponse200DataItemCurrency
    kinds: list[ListMarketAuctionVenuesResponse200DataItemKindsItem]
    close_rule: ListMarketAuctionVenuesResponse200DataItemCloseRuleType0 | None
    payment_rule: ListMarketAuctionVenuesResponse200DataItemPaymentRuleType0 | None
    bidder_rule: ListMarketAuctionVenuesResponse200DataItemBidderRuleType0 | None
    first_year: ListMarketAuctionVenuesResponse200DataItemFirstYear
    today: ListMarketAuctionVenuesResponse200DataItemTodayType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_market_auction_venues_response_200_data_item_bidder_rule_type_0 import (
            ListMarketAuctionVenuesResponse200DataItemBidderRuleType0,
        )
        from ..models.list_market_auction_venues_response_200_data_item_close_rule_type_0 import (
            ListMarketAuctionVenuesResponse200DataItemCloseRuleType0,
        )
        from ..models.list_market_auction_venues_response_200_data_item_payment_rule_type_0 import (
            ListMarketAuctionVenuesResponse200DataItemPaymentRuleType0,
        )
        from ..models.list_market_auction_venues_response_200_data_item_today_type_0 import (
            ListMarketAuctionVenuesResponse200DataItemTodayType0,
        )

        id: str = self.id

        label = self.label

        currency: str = self.currency

        kinds = []
        for kinds_item_data in self.kinds:
            kinds_item: str = kinds_item_data
            kinds.append(kinds_item)

        close_rule: dict[str, Any] | None
        if isinstance(
            self.close_rule, ListMarketAuctionVenuesResponse200DataItemCloseRuleType0
        ):
            close_rule = self.close_rule.to_dict()
        else:
            close_rule = self.close_rule

        payment_rule: dict[str, Any] | None
        if isinstance(
            self.payment_rule,
            ListMarketAuctionVenuesResponse200DataItemPaymentRuleType0,
        ):
            payment_rule = self.payment_rule.to_dict()
        else:
            payment_rule = self.payment_rule

        bidder_rule: dict[str, Any] | None
        if isinstance(
            self.bidder_rule, ListMarketAuctionVenuesResponse200DataItemBidderRuleType0
        ):
            bidder_rule = self.bidder_rule.to_dict()
        else:
            bidder_rule = self.bidder_rule

        first_year = self.first_year.to_dict()

        today: dict[str, Any] | None
        if isinstance(self.today, ListMarketAuctionVenuesResponse200DataItemTodayType0):
            today = self.today.to_dict()
        else:
            today = self.today

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
                "currency": currency,
                "kinds": kinds,
                "closeRule": close_rule,
                "paymentRule": payment_rule,
                "bidderRule": bidder_rule,
                "firstYear": first_year,
                "today": today,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_market_auction_venues_response_200_data_item_bidder_rule_type_0 import (
            ListMarketAuctionVenuesResponse200DataItemBidderRuleType0,
        )
        from ..models.list_market_auction_venues_response_200_data_item_close_rule_type_0 import (
            ListMarketAuctionVenuesResponse200DataItemCloseRuleType0,
        )
        from ..models.list_market_auction_venues_response_200_data_item_first_year import (
            ListMarketAuctionVenuesResponse200DataItemFirstYear,
        )
        from ..models.list_market_auction_venues_response_200_data_item_payment_rule_type_0 import (
            ListMarketAuctionVenuesResponse200DataItemPaymentRuleType0,
        )
        from ..models.list_market_auction_venues_response_200_data_item_today_type_0 import (
            ListMarketAuctionVenuesResponse200DataItemTodayType0,
        )

        d = dict(src_dict)
        id = check_list_market_auction_venues_response_200_data_item_id(d.pop("id"))

        label = d.pop("label")

        currency = check_list_market_auction_venues_response_200_data_item_currency(
            d.pop("currency")
        )

        kinds = []
        _kinds = d.pop("kinds")
        for kinds_item_data in _kinds:
            kinds_item = (
                check_list_market_auction_venues_response_200_data_item_kinds_item(
                    kinds_item_data
                )
            )

            kinds.append(kinds_item)

        def _parse_close_rule(
            data: object,
        ) -> ListMarketAuctionVenuesResponse200DataItemCloseRuleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                close_rule_type_0 = (
                    ListMarketAuctionVenuesResponse200DataItemCloseRuleType0.from_dict(
                        data
                    )
                )

                return close_rule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListMarketAuctionVenuesResponse200DataItemCloseRuleType0 | None, data
            )

        close_rule = _parse_close_rule(d.pop("closeRule"))

        def _parse_payment_rule(
            data: object,
        ) -> ListMarketAuctionVenuesResponse200DataItemPaymentRuleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_rule_type_0 = ListMarketAuctionVenuesResponse200DataItemPaymentRuleType0.from_dict(
                    data
                )

                return payment_rule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListMarketAuctionVenuesResponse200DataItemPaymentRuleType0 | None, data
            )

        payment_rule = _parse_payment_rule(d.pop("paymentRule"))

        def _parse_bidder_rule(
            data: object,
        ) -> ListMarketAuctionVenuesResponse200DataItemBidderRuleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bidder_rule_type_0 = (
                    ListMarketAuctionVenuesResponse200DataItemBidderRuleType0.from_dict(
                        data
                    )
                )

                return bidder_rule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListMarketAuctionVenuesResponse200DataItemBidderRuleType0 | None, data
            )

        bidder_rule = _parse_bidder_rule(d.pop("bidderRule"))

        first_year = ListMarketAuctionVenuesResponse200DataItemFirstYear.from_dict(
            d.pop("firstYear")
        )

        def _parse_today(
            data: object,
        ) -> ListMarketAuctionVenuesResponse200DataItemTodayType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                today_type_0 = (
                    ListMarketAuctionVenuesResponse200DataItemTodayType0.from_dict(data)
                )

                return today_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListMarketAuctionVenuesResponse200DataItemTodayType0 | None, data
            )

        today = _parse_today(d.pop("today"))

        list_market_auction_venues_response_200_data_item = cls(
            id=id,
            label=label,
            currency=currency,
            kinds=kinds,
            close_rule=close_rule,
            payment_rule=payment_rule,
            bidder_rule=bidder_rule,
            first_year=first_year,
            today=today,
        )

        list_market_auction_venues_response_200_data_item.additional_properties = d
        return list_market_auction_venues_response_200_data_item

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
