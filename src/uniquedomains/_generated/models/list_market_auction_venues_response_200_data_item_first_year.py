from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_market_auction_venues_response_200_data_item_first_year_additional_property_type_0 import (
        ListMarketAuctionVenuesResponse200DataItemFirstYearAdditionalPropertyType0,
    )


T = TypeVar("T", bound="ListMarketAuctionVenuesResponse200DataItemFirstYear")


@_attrs_define
class ListMarketAuctionVenuesResponse200DataItemFirstYear:
    additional_properties: dict[
        str,
        ListMarketAuctionVenuesResponse200DataItemFirstYearAdditionalPropertyType0
        | None,
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_market_auction_venues_response_200_data_item_first_year_additional_property_type_0 import (
            ListMarketAuctionVenuesResponse200DataItemFirstYearAdditionalPropertyType0,
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(
                prop,
                ListMarketAuctionVenuesResponse200DataItemFirstYearAdditionalPropertyType0,
            ):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_market_auction_venues_response_200_data_item_first_year_additional_property_type_0 import (
            ListMarketAuctionVenuesResponse200DataItemFirstYearAdditionalPropertyType0,
        )

        d = dict(src_dict)
        list_market_auction_venues_response_200_data_item_first_year = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> (
                ListMarketAuctionVenuesResponse200DataItemFirstYearAdditionalPropertyType0
                | None
            ):
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = ListMarketAuctionVenuesResponse200DataItemFirstYearAdditionalPropertyType0.from_dict(
                        data
                    )

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(
                    ListMarketAuctionVenuesResponse200DataItemFirstYearAdditionalPropertyType0
                    | None,
                    data,
                )

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        list_market_auction_venues_response_200_data_item_first_year.additional_properties = additional_properties
        return list_market_auction_venues_response_200_data_item_first_year

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> (
        ListMarketAuctionVenuesResponse200DataItemFirstYearAdditionalPropertyType0
        | None
    ):
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: ListMarketAuctionVenuesResponse200DataItemFirstYearAdditionalPropertyType0
        | None,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
