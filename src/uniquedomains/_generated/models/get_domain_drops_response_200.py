from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_domain_drops_response_200_data_type_0 import (
        GetDomainDropsResponse200DataType0,
    )
    from ..models.get_domain_drops_response_200_data_type_1_item import (
        GetDomainDropsResponse200DataType1Item,
    )
    from ..models.links import Links
    from ..models.meta import Meta


T = TypeVar("T", bound="GetDomainDropsResponse200")


@_attrs_define
class GetDomainDropsResponse200:
    """
    Attributes:
        data (GetDomainDropsResponse200DataType0 | list[GetDomainDropsResponse200DataType1Item]): Free: the summary
            object. Keyed: the list of names.
        meta (Meta):
        links (Links):
    """

    data: (
        GetDomainDropsResponse200DataType0
        | list[GetDomainDropsResponse200DataType1Item]
    )
    meta: Meta
    links: Links
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_domain_drops_response_200_data_type_0 import (
            GetDomainDropsResponse200DataType0,
        )

        data: dict[str, Any] | list[dict[str, Any]]
        if isinstance(self.data, GetDomainDropsResponse200DataType0):
            data = self.data.to_dict()
        else:
            data = []
            for data_type_1_item_data in self.data:
                data_type_1_item = data_type_1_item_data.to_dict()
                data.append(data_type_1_item)

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
        from ..models.get_domain_drops_response_200_data_type_0 import (
            GetDomainDropsResponse200DataType0,
        )
        from ..models.get_domain_drops_response_200_data_type_1_item import (
            GetDomainDropsResponse200DataType1Item,
        )
        from ..models.links import Links
        from ..models.meta import Meta

        d = dict(src_dict)

        def _parse_data(
            data: object,
        ) -> (
            GetDomainDropsResponse200DataType0
            | list[GetDomainDropsResponse200DataType1Item]
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = GetDomainDropsResponse200DataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            data_type_1 = []
            _data_type_1 = data
            for data_type_1_item_data in _data_type_1:
                data_type_1_item = GetDomainDropsResponse200DataType1Item.from_dict(
                    data_type_1_item_data
                )

                data_type_1.append(data_type_1_item)

            return data_type_1

        data = _parse_data(d.pop("data"))

        meta = Meta.from_dict(d.pop("meta"))

        links = Links.from_dict(d.pop("links"))

        get_domain_drops_response_200 = cls(
            data=data,
            meta=meta,
            links=links,
        )

        get_domain_drops_response_200.additional_properties = d
        return get_domain_drops_response_200

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
