from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="ListMarketAuctionVenuesResponse200DataItemFirstYearAdditionalPropertyType0Value",
)


@_attrs_define
class ListMarketAuctionVenuesResponse200DataItemFirstYearAdditionalPropertyType0Value:
    """
    Attributes:
        registration_included (bool):
        flat_fee (float):
    """

    registration_included: bool
    flat_fee: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registration_included = self.registration_included

        flat_fee = self.flat_fee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registrationIncluded": registration_included,
                "flatFee": flat_fee,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        registration_included = d.pop("registrationIncluded")

        flat_fee = d.pop("flatFee")

        list_market_auction_venues_response_200_data_item_first_year_additional_property_type_0_value = cls(
            registration_included=registration_included,
            flat_fee=flat_fee,
        )

        list_market_auction_venues_response_200_data_item_first_year_additional_property_type_0_value.additional_properties = d
        return list_market_auction_venues_response_200_data_item_first_year_additional_property_type_0_value

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
