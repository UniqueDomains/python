from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_venues_response_200_data_item_footprint_type_0 import (
        ListVenuesResponse200DataItemFootprintType0,
    )


T = TypeVar("T", bound="ListVenuesResponse200DataItem")


@_attrs_define
class ListVenuesResponse200DataItem:
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
        footprint (ListVenuesResponse200DataItemFootprintType0 | None):
    """

    slug: str
    name: str
    kind: str
    iana_id: int | None
    accredited: bool
    homepage_url: None | str
    site_url: None | str
    logo_url: None | str
    footprint: ListVenuesResponse200DataItemFootprintType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_venues_response_200_data_item_footprint_type_0 import (
            ListVenuesResponse200DataItemFootprintType0,
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
        if isinstance(self.footprint, ListVenuesResponse200DataItemFootprintType0):
            footprint = self.footprint.to_dict()
        else:
            footprint = self.footprint

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
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_venues_response_200_data_item_footprint_type_0 import (
            ListVenuesResponse200DataItemFootprintType0,
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
        ) -> ListVenuesResponse200DataItemFootprintType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                footprint_type_0 = (
                    ListVenuesResponse200DataItemFootprintType0.from_dict(data)
                )

                return footprint_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListVenuesResponse200DataItemFootprintType0 | None, data)

        footprint = _parse_footprint(d.pop("footprint"))

        list_venues_response_200_data_item = cls(
            slug=slug,
            name=name,
            kind=kind,
            iana_id=iana_id,
            accredited=accredited,
            homepage_url=homepage_url,
            site_url=site_url,
            logo_url=logo_url,
            footprint=footprint,
        )

        list_venues_response_200_data_item.additional_properties = d
        return list_venues_response_200_data_item

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
