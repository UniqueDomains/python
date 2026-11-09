from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWordTrademarksResponse200DataEu")


@_attrs_define
class GetWordTrademarksResponse200DataEu:
    """
    Attributes:
        live_count (int | None | Unset):
        classes (list[str] | Unset):
    """

    live_count: int | None | Unset = UNSET
    classes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        live_count: int | None | Unset
        if isinstance(self.live_count, Unset):
            live_count = UNSET
        else:
            live_count = self.live_count

        classes: list[str] | Unset = UNSET
        if not isinstance(self.classes, Unset):
            classes = self.classes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if live_count is not UNSET:
            field_dict["liveCount"] = live_count
        if classes is not UNSET:
            field_dict["classes"] = classes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_live_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        live_count = _parse_live_count(d.pop("liveCount", UNSET))

        classes = cast(list[str], d.pop("classes", UNSET))

        get_word_trademarks_response_200_data_eu = cls(
            live_count=live_count,
            classes=classes,
        )

        get_word_trademarks_response_200_data_eu.additional_properties = d
        return get_word_trademarks_response_200_data_eu

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
