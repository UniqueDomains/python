from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_meta_providers_response_200_data_auction_venues_item import (
        GetMetaProvidersResponse200DataAuctionVenuesItem,
    )
    from ..models.get_meta_providers_response_200_data_parking_services_item import (
        GetMetaProvidersResponse200DataParkingServicesItem,
    )
    from ..models.get_meta_providers_response_200_data_registrars_item import (
        GetMetaProvidersResponse200DataRegistrarsItem,
    )


T = TypeVar("T", bound="GetMetaProvidersResponse200Data")


@_attrs_define
class GetMetaProvidersResponse200Data:
    """
    Attributes:
        registrars (list[GetMetaProvidersResponse200DataRegistrarsItem]):
        auction_venues (list[GetMetaProvidersResponse200DataAuctionVenuesItem]):
        parking_services (list[GetMetaProvidersResponse200DataParkingServicesItem]):
    """

    registrars: list[GetMetaProvidersResponse200DataRegistrarsItem]
    auction_venues: list[GetMetaProvidersResponse200DataAuctionVenuesItem]
    parking_services: list[GetMetaProvidersResponse200DataParkingServicesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registrars = []
        for registrars_item_data in self.registrars:
            registrars_item = registrars_item_data.to_dict()
            registrars.append(registrars_item)

        auction_venues = []
        for auction_venues_item_data in self.auction_venues:
            auction_venues_item = auction_venues_item_data.to_dict()
            auction_venues.append(auction_venues_item)

        parking_services = []
        for parking_services_item_data in self.parking_services:
            parking_services_item = parking_services_item_data.to_dict()
            parking_services.append(parking_services_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registrars": registrars,
                "auctionVenues": auction_venues,
                "parkingServices": parking_services,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_meta_providers_response_200_data_auction_venues_item import (
            GetMetaProvidersResponse200DataAuctionVenuesItem,
        )
        from ..models.get_meta_providers_response_200_data_parking_services_item import (
            GetMetaProvidersResponse200DataParkingServicesItem,
        )
        from ..models.get_meta_providers_response_200_data_registrars_item import (
            GetMetaProvidersResponse200DataRegistrarsItem,
        )

        d = dict(src_dict)
        registrars = []
        _registrars = d.pop("registrars")
        for registrars_item_data in _registrars:
            registrars_item = GetMetaProvidersResponse200DataRegistrarsItem.from_dict(
                registrars_item_data
            )

            registrars.append(registrars_item)

        auction_venues = []
        _auction_venues = d.pop("auctionVenues")
        for auction_venues_item_data in _auction_venues:
            auction_venues_item = (
                GetMetaProvidersResponse200DataAuctionVenuesItem.from_dict(
                    auction_venues_item_data
                )
            )

            auction_venues.append(auction_venues_item)

        parking_services = []
        _parking_services = d.pop("parkingServices")
        for parking_services_item_data in _parking_services:
            parking_services_item = (
                GetMetaProvidersResponse200DataParkingServicesItem.from_dict(
                    parking_services_item_data
                )
            )

            parking_services.append(parking_services_item)

        get_meta_providers_response_200_data = cls(
            registrars=registrars,
            auction_venues=auction_venues,
            parking_services=parking_services,
        )

        get_meta_providers_response_200_data.additional_properties = d
        return get_meta_providers_response_200_data

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
