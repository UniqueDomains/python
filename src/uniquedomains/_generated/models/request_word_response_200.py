from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.links import Links
    from ..models.meta import Meta
    from ..models.request_word_response_200_data import RequestWordResponse200Data


T = TypeVar("T", bound="RequestWordResponse200")


@_attrs_define
class RequestWordResponse200:
    """
    Attributes:
        data (RequestWordResponse200Data):
        meta (Meta):
        links (Links):
    """

    data: RequestWordResponse200Data
    meta: Meta
    links: Links
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        meta = self.meta.to_dict()

        links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "meta": meta,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.links import Links
        from ..models.meta import Meta
        from ..models.request_word_response_200_data import RequestWordResponse200Data

        d = dict(src_dict)
        data = RequestWordResponse200Data.from_dict(d.pop("data"))

        meta = Meta.from_dict(d.pop("meta"))

        links = Links.from_dict(d.pop("links"))

        request_word_response_200 = cls(
            data=data,
            meta=meta,
            links=links,
        )

        request_word_response_200.additional_properties = d
        return request_word_response_200

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
