from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_meta_enums_response_200_data_auction_venues_item import (
        GetMetaEnumsResponse200DataAuctionVenuesItem,
    )
    from ..models.get_meta_enums_response_200_data_parking_services_item import (
        GetMetaEnumsResponse200DataParkingServicesItem,
    )


T = TypeVar("T", bound="GetMetaEnumsResponse200Data")


@_attrs_define
class GetMetaEnumsResponse200Data:
    """
    Attributes:
        statuses (list[str]):
        lifecycles (list[str]):
        epp_statuses (list[str]):
        lookup_states (list[str]):
        word_shapes (list[str]):
        word_origins (list[str]):
        tld_kinds (list[str]):
        agenda_categories (list[str]):
        event_categories (list[str]):
        edition_lanes (list[str]):
        change_event_types (list[str]):
        change_event_subjects (list[str]):
        auction_venues (list[GetMetaEnumsResponse200DataAuctionVenuesItem]):
        parking_services (list[GetMetaEnumsResponse200DataParkingServicesItem]):
    """

    statuses: list[str]
    lifecycles: list[str]
    epp_statuses: list[str]
    lookup_states: list[str]
    word_shapes: list[str]
    word_origins: list[str]
    tld_kinds: list[str]
    agenda_categories: list[str]
    event_categories: list[str]
    edition_lanes: list[str]
    change_event_types: list[str]
    change_event_subjects: list[str]
    auction_venues: list[GetMetaEnumsResponse200DataAuctionVenuesItem]
    parking_services: list[GetMetaEnumsResponse200DataParkingServicesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statuses = self.statuses

        lifecycles = self.lifecycles

        epp_statuses = self.epp_statuses

        lookup_states = self.lookup_states

        word_shapes = self.word_shapes

        word_origins = self.word_origins

        tld_kinds = self.tld_kinds

        agenda_categories = self.agenda_categories

        event_categories = self.event_categories

        edition_lanes = self.edition_lanes

        change_event_types = self.change_event_types

        change_event_subjects = self.change_event_subjects

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
                "statuses": statuses,
                "lifecycles": lifecycles,
                "eppStatuses": epp_statuses,
                "lookupStates": lookup_states,
                "wordShapes": word_shapes,
                "wordOrigins": word_origins,
                "tldKinds": tld_kinds,
                "agendaCategories": agenda_categories,
                "eventCategories": event_categories,
                "editionLanes": edition_lanes,
                "changeEventTypes": change_event_types,
                "changeEventSubjects": change_event_subjects,
                "auctionVenues": auction_venues,
                "parkingServices": parking_services,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_meta_enums_response_200_data_auction_venues_item import (
            GetMetaEnumsResponse200DataAuctionVenuesItem,
        )
        from ..models.get_meta_enums_response_200_data_parking_services_item import (
            GetMetaEnumsResponse200DataParkingServicesItem,
        )

        d = dict(src_dict)
        statuses = cast(list[str], d.pop("statuses"))

        lifecycles = cast(list[str], d.pop("lifecycles"))

        epp_statuses = cast(list[str], d.pop("eppStatuses"))

        lookup_states = cast(list[str], d.pop("lookupStates"))

        word_shapes = cast(list[str], d.pop("wordShapes"))

        word_origins = cast(list[str], d.pop("wordOrigins"))

        tld_kinds = cast(list[str], d.pop("tldKinds"))

        agenda_categories = cast(list[str], d.pop("agendaCategories"))

        event_categories = cast(list[str], d.pop("eventCategories"))

        edition_lanes = cast(list[str], d.pop("editionLanes"))

        change_event_types = cast(list[str], d.pop("changeEventTypes"))

        change_event_subjects = cast(list[str], d.pop("changeEventSubjects"))

        auction_venues = []
        _auction_venues = d.pop("auctionVenues")
        for auction_venues_item_data in _auction_venues:
            auction_venues_item = (
                GetMetaEnumsResponse200DataAuctionVenuesItem.from_dict(
                    auction_venues_item_data
                )
            )

            auction_venues.append(auction_venues_item)

        parking_services = []
        _parking_services = d.pop("parkingServices")
        for parking_services_item_data in _parking_services:
            parking_services_item = (
                GetMetaEnumsResponse200DataParkingServicesItem.from_dict(
                    parking_services_item_data
                )
            )

            parking_services.append(parking_services_item)

        get_meta_enums_response_200_data = cls(
            statuses=statuses,
            lifecycles=lifecycles,
            epp_statuses=epp_statuses,
            lookup_states=lookup_states,
            word_shapes=word_shapes,
            word_origins=word_origins,
            tld_kinds=tld_kinds,
            agenda_categories=agenda_categories,
            event_categories=event_categories,
            edition_lanes=edition_lanes,
            change_event_types=change_event_types,
            change_event_subjects=change_event_subjects,
            auction_venues=auction_venues,
            parking_services=parking_services,
        )

        get_meta_enums_response_200_data.additional_properties = d
        return get_meta_enums_response_200_data

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
