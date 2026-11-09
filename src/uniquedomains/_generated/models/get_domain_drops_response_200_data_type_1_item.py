from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_domain_drops_response_200_data_type_1_item_status import (
    GetDomainDropsResponse200DataType1ItemStatus,
    check_get_domain_drops_response_200_data_type_1_item_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDomainDropsResponse200DataType1Item")


@_attrs_define
class GetDomainDropsResponse200DataType1Item:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        ending (str | Unset):
        drops_on (datetime.date | Unset):
        status (GetDomainDropsResponse200DataType1ItemStatus | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    ending: str | Unset = UNSET
    drops_on: datetime.date | Unset = UNSET
    status: GetDomainDropsResponse200DataType1ItemStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        ending = self.ending

        drops_on: str | Unset = UNSET
        if not isinstance(self.drops_on, Unset):
            drops_on = self.drops_on.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if ending is not UNSET:
            field_dict["ending"] = ending
        if drops_on is not UNSET:
            field_dict["dropsOn"] = drops_on
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        ending = d.pop("ending", UNSET)

        _drops_on = d.pop("dropsOn", UNSET)
        drops_on: datetime.date | Unset
        if isinstance(_drops_on, Unset):
            drops_on = UNSET
        else:
            drops_on = datetime.date.fromisoformat(_drops_on)

        _status = d.pop("status", UNSET)
        status: GetDomainDropsResponse200DataType1ItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_get_domain_drops_response_200_data_type_1_item_status(
                _status
            )

        get_domain_drops_response_200_data_type_1_item = cls(
            id=id,
            name=name,
            ending=ending,
            drops_on=drops_on,
            status=status,
        )

        get_domain_drops_response_200_data_type_1_item.additional_properties = d
        return get_domain_drops_response_200_data_type_1_item

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
