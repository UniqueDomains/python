from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.batch_names_response_200_data_item_type_0 import (
        BatchNamesResponse200DataItemType0,
    )
    from ..models.batch_names_response_200_data_item_type_1 import (
        BatchNamesResponse200DataItemType1,
    )
    from ..models.batch_names_response_200_data_item_type_2 import (
        BatchNamesResponse200DataItemType2,
    )
    from ..models.links import Links
    from ..models.meta import Meta


T = TypeVar("T", bound="BatchNamesResponse200")


@_attrs_define
class BatchNamesResponse200:
    """
    Attributes:
        data (list[BatchNamesResponse200DataItemType0 | BatchNamesResponse200DataItemType1 |
            BatchNamesResponse200DataItemType2]):
        meta (Meta):
        links (Links):
    """

    data: list[
        BatchNamesResponse200DataItemType0
        | BatchNamesResponse200DataItemType1
        | BatchNamesResponse200DataItemType2
    ]
    meta: Meta
    links: Links
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_names_response_200_data_item_type_0 import (
            BatchNamesResponse200DataItemType0,
        )
        from ..models.batch_names_response_200_data_item_type_1 import (
            BatchNamesResponse200DataItemType1,
        )

        data = []
        for data_item_data in self.data:
            data_item: dict[str, Any]
            if isinstance(
                data_item_data, BatchNamesResponse200DataItemType0
            ) or isinstance(data_item_data, BatchNamesResponse200DataItemType1):
                data_item = data_item_data.to_dict()
            else:
                data_item = data_item_data.to_dict()

            data.append(data_item)

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
        from ..models.batch_names_response_200_data_item_type_0 import (
            BatchNamesResponse200DataItemType0,
        )
        from ..models.batch_names_response_200_data_item_type_1 import (
            BatchNamesResponse200DataItemType1,
        )
        from ..models.batch_names_response_200_data_item_type_2 import (
            BatchNamesResponse200DataItemType2,
        )
        from ..models.links import Links
        from ..models.meta import Meta

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:

            def _parse_data_item(
                data: object,
            ) -> (
                BatchNamesResponse200DataItemType0
                | BatchNamesResponse200DataItemType1
                | BatchNamesResponse200DataItemType2
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_0 = BatchNamesResponse200DataItemType0.from_dict(
                        data
                    )

                    return data_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_1 = BatchNamesResponse200DataItemType1.from_dict(
                        data
                    )

                    return data_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                data_item_type_2 = BatchNamesResponse200DataItemType2.from_dict(data)

                return data_item_type_2

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)

        meta = Meta.from_dict(d.pop("meta"))

        links = Links.from_dict(d.pop("links"))

        batch_names_response_200 = cls(
            data=data,
            meta=meta,
            links=links,
        )

        batch_names_response_200.additional_properties = d
        return batch_names_response_200

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
