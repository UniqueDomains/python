from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_meta_freshness_response_200_data_lanes_item import (
        GetMetaFreshnessResponse200DataLanesItem,
    )


T = TypeVar("T", bound="GetMetaFreshnessResponse200Data")


@_attrs_define
class GetMetaFreshnessResponse200Data:
    """
    Attributes:
        as_of (datetime.datetime | None):
        scanned_today (int):
        checked_last_24_h (int):
        lanes (list[GetMetaFreshnessResponse200DataLanesItem]):
    """

    as_of: datetime.datetime | None
    scanned_today: int
    checked_last_24_h: int
    lanes: list[GetMetaFreshnessResponse200DataLanesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_of: None | str
        if isinstance(self.as_of, datetime.datetime):
            as_of = self.as_of.isoformat()
        else:
            as_of = self.as_of

        scanned_today = self.scanned_today

        checked_last_24_h = self.checked_last_24_h

        lanes = []
        for lanes_item_data in self.lanes:
            lanes_item = lanes_item_data.to_dict()
            lanes.append(lanes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asOf": as_of,
                "scannedToday": scanned_today,
                "checkedLast24h": checked_last_24_h,
                "lanes": lanes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_meta_freshness_response_200_data_lanes_item import (
            GetMetaFreshnessResponse200DataLanesItem,
        )

        d = dict(src_dict)

        def _parse_as_of(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_of_type_0 = datetime.datetime.fromisoformat(data)

                return as_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        as_of = _parse_as_of(d.pop("asOf"))

        scanned_today = d.pop("scannedToday")

        checked_last_24_h = d.pop("checkedLast24h")

        lanes = []
        _lanes = d.pop("lanes")
        for lanes_item_data in _lanes:
            lanes_item = GetMetaFreshnessResponse200DataLanesItem.from_dict(
                lanes_item_data
            )

            lanes.append(lanes_item)

        get_meta_freshness_response_200_data = cls(
            as_of=as_of,
            scanned_today=scanned_today,
            checked_last_24_h=checked_last_24_h,
            lanes=lanes,
        )

        get_meta_freshness_response_200_data.additional_properties = d
        return get_meta_freshness_response_200_data

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
