from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_word_response_200_data_word_origin import (
    RequestWordResponse200DataWordOrigin,
    check_request_word_response_200_data_word_origin,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestWordResponse200DataWord")


@_attrs_define
class RequestWordResponse200DataWord:
    """On `in_catalog`.

    Attributes:
        id (str | Unset): `wrd_<id>`.
        slug (None | str | Unset):
        origin (RequestWordResponse200DataWordOrigin | Unset):
    """

    id: str | Unset = UNSET
    slug: None | str | Unset = UNSET
    origin: RequestWordResponse200DataWordOrigin | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        origin: str | Unset = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if origin is not UNSET:
            field_dict["origin"] = origin

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        _origin = d.pop("origin", UNSET)
        origin: RequestWordResponse200DataWordOrigin | Unset
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = check_request_word_response_200_data_word_origin(_origin)

        request_word_response_200_data_word = cls(
            id=id,
            slug=slug,
            origin=origin,
        )

        request_word_response_200_data_word.additional_properties = d
        return request_word_response_200_data_word

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
