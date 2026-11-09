from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_venue_response_200_data_footprint_type_0 import (
        GetVenueResponse200DataFootprintType0,
    )
    from ..models.get_venue_response_200_data_listing_terms_type_0 import (
        GetVenueResponse200DataListingTermsType0,
    )


T = TypeVar("T", bound="GetVenueResponse200Data")


@_attrs_define
class GetVenueResponse200Data:
    """
    Attributes:
        slug (str): Catalog slug.
        name (str): Display name.
        kind (str): `registrar`, or a venue's kind (`marketplace`, `parking`, `dropcatch`).
        iana_id (int | None):
        accredited (bool): The IANA record says accredited.
        homepage_url (None | str):
        site_url (None | str):
        logo_url (None | str):
        footprint (GetVenueResponse200DataFootprintType0 | None):
        footprint_day (datetime.date | None):
        listing_terms (GetVenueResponse200DataListingTermsType0 | None):
    """

    slug: str
    name: str
    kind: str
    iana_id: int | None
    accredited: bool
    homepage_url: None | str
    site_url: None | str
    logo_url: None | str
    footprint: GetVenueResponse200DataFootprintType0 | None
    footprint_day: datetime.date | None
    listing_terms: GetVenueResponse200DataListingTermsType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_venue_response_200_data_footprint_type_0 import (
            GetVenueResponse200DataFootprintType0,
        )
        from ..models.get_venue_response_200_data_listing_terms_type_0 import (
            GetVenueResponse200DataListingTermsType0,
        )

        slug = self.slug

        name = self.name

        kind = self.kind

        iana_id: int | None
        iana_id = self.iana_id

        accredited = self.accredited

        homepage_url: None | str
        homepage_url = self.homepage_url

        site_url: None | str
        site_url = self.site_url

        logo_url: None | str
        logo_url = self.logo_url

        footprint: dict[str, Any] | None
        if isinstance(self.footprint, GetVenueResponse200DataFootprintType0):
            footprint = self.footprint.to_dict()
        else:
            footprint = self.footprint

        footprint_day: None | str
        if isinstance(self.footprint_day, datetime.date):
            footprint_day = self.footprint_day.isoformat()
        else:
            footprint_day = self.footprint_day

        listing_terms: dict[str, Any] | None
        if isinstance(self.listing_terms, GetVenueResponse200DataListingTermsType0):
            listing_terms = self.listing_terms.to_dict()
        else:
            listing_terms = self.listing_terms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "name": name,
                "kind": kind,
                "ianaId": iana_id,
                "accredited": accredited,
                "homepageUrl": homepage_url,
                "siteUrl": site_url,
                "logoUrl": logo_url,
                "footprint": footprint,
                "footprintDay": footprint_day,
                "listingTerms": listing_terms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_venue_response_200_data_footprint_type_0 import (
            GetVenueResponse200DataFootprintType0,
        )
        from ..models.get_venue_response_200_data_listing_terms_type_0 import (
            GetVenueResponse200DataListingTermsType0,
        )

        d = dict(src_dict)
        slug = d.pop("slug")

        name = d.pop("name")

        kind = d.pop("kind")

        def _parse_iana_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        iana_id = _parse_iana_id(d.pop("ianaId"))

        accredited = d.pop("accredited")

        def _parse_homepage_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        homepage_url = _parse_homepage_url(d.pop("homepageUrl"))

        def _parse_site_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        site_url = _parse_site_url(d.pop("siteUrl"))

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logoUrl"))

        def _parse_footprint(
            data: object,
        ) -> GetVenueResponse200DataFootprintType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                footprint_type_0 = GetVenueResponse200DataFootprintType0.from_dict(data)

                return footprint_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVenueResponse200DataFootprintType0 | None, data)

        footprint = _parse_footprint(d.pop("footprint"))

        def _parse_footprint_day(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                footprint_day_type_0 = datetime.date.fromisoformat(data)

                return footprint_day_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        footprint_day = _parse_footprint_day(d.pop("footprintDay"))

        def _parse_listing_terms(
            data: object,
        ) -> GetVenueResponse200DataListingTermsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                listing_terms_type_0 = (
                    GetVenueResponse200DataListingTermsType0.from_dict(data)
                )

                return listing_terms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVenueResponse200DataListingTermsType0 | None, data)

        listing_terms = _parse_listing_terms(d.pop("listingTerms"))

        get_venue_response_200_data = cls(
            slug=slug,
            name=name,
            kind=kind,
            iana_id=iana_id,
            accredited=accredited,
            homepage_url=homepage_url,
            site_url=site_url,
            logo_url=logo_url,
            footprint=footprint,
            footprint_day=footprint_day,
            listing_terms=listing_terms,
        )

        get_venue_response_200_data.additional_properties = d
        return get_venue_response_200_data

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
