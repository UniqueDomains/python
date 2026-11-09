from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_meta_freshness_response_200_data_lanes_item_state import (
    GetMetaFreshnessResponse200DataLanesItemState,
    check_get_meta_freshness_response_200_data_lanes_item_state,
)

T = TypeVar("T", bound="GetMetaFreshnessResponse200DataLanesItem")


@_attrs_define
class GetMetaFreshnessResponse200DataLanesItem:
    """
    Attributes:
        lane (str):
        scanned (int | None):
        state (GetMetaFreshnessResponse200DataLanesItemState):
    """

    lane: str
    scanned: int | None
    state: GetMetaFreshnessResponse200DataLanesItemState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lane = self.lane

        scanned: int | None
        scanned = self.scanned

        state: str = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lane": lane,
                "scanned": scanned,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lane = d.pop("lane")

        def _parse_scanned(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        scanned = _parse_scanned(d.pop("scanned"))

        state = check_get_meta_freshness_response_200_data_lanes_item_state(
            d.pop("state")
        )

        get_meta_freshness_response_200_data_lanes_item = cls(
            lane=lane,
            scanned=scanned,
            state=state,
        )

        get_meta_freshness_response_200_data_lanes_item.additional_properties = d
        return get_meta_freshness_response_200_data_lanes_item

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
