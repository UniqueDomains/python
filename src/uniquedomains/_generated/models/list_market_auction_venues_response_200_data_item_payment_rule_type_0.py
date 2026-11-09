from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListMarketAuctionVenuesResponse200DataItemPaymentRuleType0")


@_attrs_define
class ListMarketAuctionVenuesResponse200DataItemPaymentRuleType0:
    """
    Attributes:
        value (str | Unset):
        verified_on (datetime.date | Unset):
    """

    value: str | Unset = UNSET
    verified_on: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        verified_on: str | Unset = UNSET
        if not isinstance(self.verified_on, Unset):
            verified_on = self.verified_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if verified_on is not UNSET:
            field_dict["verifiedOn"] = verified_on

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        _verified_on = d.pop("verifiedOn", UNSET)
        verified_on: datetime.date | Unset
        if isinstance(_verified_on, Unset):
            verified_on = UNSET
        else:
            verified_on = datetime.date.fromisoformat(_verified_on)

        list_market_auction_venues_response_200_data_item_payment_rule_type_0 = cls(
            value=value,
            verified_on=verified_on,
        )

        list_market_auction_venues_response_200_data_item_payment_rule_type_0.additional_properties = d
        return list_market_auction_venues_response_200_data_item_payment_rule_type_0

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
