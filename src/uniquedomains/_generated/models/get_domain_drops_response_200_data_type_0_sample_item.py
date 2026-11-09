from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDomainDropsResponse200DataType0SampleItem")


@_attrs_define
class GetDomainDropsResponse200DataType0SampleItem:
    """
    Attributes:
        ending (str | Unset):
        drops_on (datetime.date | Unset):
    """

    ending: str | Unset = UNSET
    drops_on: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ending = self.ending

        drops_on: str | Unset = UNSET
        if not isinstance(self.drops_on, Unset):
            drops_on = self.drops_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ending is not UNSET:
            field_dict["ending"] = ending
        if drops_on is not UNSET:
            field_dict["dropsOn"] = drops_on

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ending = d.pop("ending", UNSET)

        _drops_on = d.pop("dropsOn", UNSET)
        drops_on: datetime.date | Unset
        if isinstance(_drops_on, Unset):
            drops_on = UNSET
        else:
            drops_on = datetime.date.fromisoformat(_drops_on)

        get_domain_drops_response_200_data_type_0_sample_item = cls(
            ending=ending,
            drops_on=drops_on,
        )

        get_domain_drops_response_200_data_type_0_sample_item.additional_properties = d
        return get_domain_drops_response_200_data_type_0_sample_item

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
