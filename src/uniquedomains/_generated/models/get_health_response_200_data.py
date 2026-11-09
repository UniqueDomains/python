from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_health_response_200_data_status import (
    GetHealthResponse200DataStatus,
    check_get_health_response_200_data_status,
)

T = TypeVar("T", bound="GetHealthResponse200Data")


@_attrs_define
class GetHealthResponse200Data:
    """
    Attributes:
        status (GetHealthResponse200DataStatus):
        as_of (datetime.datetime):
    """

    status: GetHealthResponse200DataStatus
    as_of: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        as_of = self.as_of.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "asOf": as_of,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = check_get_health_response_200_data_status(d.pop("status"))

        as_of = datetime.datetime.fromisoformat(d.pop("asOf"))

        get_health_response_200_data = cls(
            status=status,
            as_of=as_of,
        )

        get_health_response_200_data.additional_properties = d
        return get_health_response_200_data

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
