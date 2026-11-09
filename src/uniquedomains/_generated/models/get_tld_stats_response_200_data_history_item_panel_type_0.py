from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetTldStatsResponse200DataHistoryItemPanelType0")


@_attrs_define
class GetTldStatsResponse200DataHistoryItemPanelType0:
    """
    Attributes:
        names (int):
        available (int):
        resell (int):
        expiring90d (int):
    """

    names: int
    available: int
    resell: int
    expiring90d: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        names = self.names

        available = self.available

        resell = self.resell

        expiring90d = self.expiring90d

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "names": names,
                "available": available,
                "resell": resell,
                "expiring90d": expiring90d,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        names = d.pop("names")

        available = d.pop("available")

        resell = d.pop("resell")

        expiring90d = d.pop("expiring90d")

        get_tld_stats_response_200_data_history_item_panel_type_0 = cls(
            names=names,
            available=available,
            resell=resell,
            expiring90d=expiring90d,
        )

        get_tld_stats_response_200_data_history_item_panel_type_0.additional_properties = d
        return get_tld_stats_response_200_data_history_item_panel_type_0

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
