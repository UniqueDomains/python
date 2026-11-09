from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_registrar_footprint_response_200_data_top_endings_item import (
        GetRegistrarFootprintResponse200DataTopEndingsItem,
    )


T = TypeVar("T", bound="GetRegistrarFootprintResponse200Data")


@_attrs_define
class GetRegistrarFootprintResponse200Data:
    """
    Attributes:
        registrar (str):
        day (datetime.date):
        names (int | None):
        top_endings (list[GetRegistrarFootprintResponse200DataTopEndingsItem]):
    """

    registrar: str
    day: datetime.date
    names: int | None
    top_endings: list[GetRegistrarFootprintResponse200DataTopEndingsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registrar = self.registrar

        day = self.day.isoformat()

        names: int | None
        names = self.names

        top_endings = []
        for top_endings_item_data in self.top_endings:
            top_endings_item = top_endings_item_data.to_dict()
            top_endings.append(top_endings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registrar": registrar,
                "day": day,
                "names": names,
                "topEndings": top_endings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_registrar_footprint_response_200_data_top_endings_item import (
            GetRegistrarFootprintResponse200DataTopEndingsItem,
        )

        d = dict(src_dict)
        registrar = d.pop("registrar")

        day = datetime.date.fromisoformat(d.pop("day"))

        def _parse_names(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        names = _parse_names(d.pop("names"))

        top_endings = []
        _top_endings = d.pop("topEndings")
        for top_endings_item_data in _top_endings:
            top_endings_item = (
                GetRegistrarFootprintResponse200DataTopEndingsItem.from_dict(
                    top_endings_item_data
                )
            )

            top_endings.append(top_endings_item)

        get_registrar_footprint_response_200_data = cls(
            registrar=registrar,
            day=day,
            names=names,
            top_endings=top_endings,
        )

        get_registrar_footprint_response_200_data.additional_properties = d
        return get_registrar_footprint_response_200_data

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
