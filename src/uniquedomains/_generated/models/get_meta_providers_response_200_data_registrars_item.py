from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetMetaProvidersResponse200DataRegistrarsItem")


@_attrs_define
class GetMetaProvidersResponse200DataRegistrarsItem:
    """
    Attributes:
        slug (str):
        name (str):
        iana_id (int | None):
        homepage_url (None | str):
    """

    slug: str
    name: str
    iana_id: int | None
    homepage_url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        iana_id: int | None
        iana_id = self.iana_id

        homepage_url: None | str
        homepage_url = self.homepage_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "name": name,
                "ianaId": iana_id,
                "homepageUrl": homepage_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        slug = d.pop("slug")

        name = d.pop("name")

        def _parse_iana_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        iana_id = _parse_iana_id(d.pop("ianaId"))

        def _parse_homepage_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        homepage_url = _parse_homepage_url(d.pop("homepageUrl"))

        get_meta_providers_response_200_data_registrars_item = cls(
            slug=slug,
            name=name,
            iana_id=iana_id,
            homepage_url=homepage_url,
        )

        get_meta_providers_response_200_data_registrars_item.additional_properties = d
        return get_meta_providers_response_200_data_registrars_item

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
