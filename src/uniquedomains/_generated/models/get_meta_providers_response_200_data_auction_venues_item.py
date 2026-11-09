from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_meta_providers_response_200_data_auction_venues_item_id import (
    GetMetaProvidersResponse200DataAuctionVenuesItemId,
    check_get_meta_providers_response_200_data_auction_venues_item_id,
)

T = TypeVar("T", bound="GetMetaProvidersResponse200DataAuctionVenuesItem")


@_attrs_define
class GetMetaProvidersResponse200DataAuctionVenuesItem:
    """
    Attributes:
        id (GetMetaProvidersResponse200DataAuctionVenuesItemId):
        label (str):
    """

    id: GetMetaProvidersResponse200DataAuctionVenuesItemId
    label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str = self.id

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = check_get_meta_providers_response_200_data_auction_venues_item_id(
            d.pop("id")
        )

        label = d.pop("label")

        get_meta_providers_response_200_data_auction_venues_item = cls(
            id=id,
            label=label,
        )

        get_meta_providers_response_200_data_auction_venues_item.additional_properties = d
        return get_meta_providers_response_200_data_auction_venues_item

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
