from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_word_trademarks_response_200_data_eu import (
        GetWordTrademarksResponse200DataEu,
    )
    from ..models.get_word_trademarks_response_200_data_marks_item import (
        GetWordTrademarksResponse200DataMarksItem,
    )
    from ..models.get_word_trademarks_response_200_data_us import (
        GetWordTrademarksResponse200DataUs,
    )


T = TypeVar("T", bound="GetWordTrademarksResponse200Data")


@_attrs_define
class GetWordTrademarksResponse200Data:
    """
    Attributes:
        us (GetWordTrademarksResponse200DataUs | Unset):
        eu (GetWordTrademarksResponse200DataEu | Unset):
        marks (list[GetWordTrademarksResponse200DataMarksItem] | Unset):
    """

    us: GetWordTrademarksResponse200DataUs | Unset = UNSET
    eu: GetWordTrademarksResponse200DataEu | Unset = UNSET
    marks: list[GetWordTrademarksResponse200DataMarksItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        us: dict[str, Any] | Unset = UNSET
        if not isinstance(self.us, Unset):
            us = self.us.to_dict()

        eu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eu, Unset):
            eu = self.eu.to_dict()

        marks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.marks, Unset):
            marks = []
            for marks_item_data in self.marks:
                marks_item = marks_item_data.to_dict()
                marks.append(marks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if us is not UNSET:
            field_dict["us"] = us
        if eu is not UNSET:
            field_dict["eu"] = eu
        if marks is not UNSET:
            field_dict["marks"] = marks

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_word_trademarks_response_200_data_eu import (
            GetWordTrademarksResponse200DataEu,
        )
        from ..models.get_word_trademarks_response_200_data_marks_item import (
            GetWordTrademarksResponse200DataMarksItem,
        )
        from ..models.get_word_trademarks_response_200_data_us import (
            GetWordTrademarksResponse200DataUs,
        )

        d = dict(src_dict)
        _us = d.pop("us", UNSET)
        us: GetWordTrademarksResponse200DataUs | Unset
        if isinstance(_us, Unset):
            us = UNSET
        else:
            us = GetWordTrademarksResponse200DataUs.from_dict(_us)

        _eu = d.pop("eu", UNSET)
        eu: GetWordTrademarksResponse200DataEu | Unset
        if isinstance(_eu, Unset):
            eu = UNSET
        else:
            eu = GetWordTrademarksResponse200DataEu.from_dict(_eu)

        _marks = d.pop("marks", UNSET)
        marks: list[GetWordTrademarksResponse200DataMarksItem] | Unset = UNSET
        if _marks is not UNSET:
            marks = []
            for marks_item_data in _marks:
                marks_item = GetWordTrademarksResponse200DataMarksItem.from_dict(
                    marks_item_data
                )

                marks.append(marks_item)

        get_word_trademarks_response_200_data = cls(
            us=us,
            eu=eu,
            marks=marks,
        )

        get_word_trademarks_response_200_data.additional_properties = d
        return get_word_trademarks_response_200_data

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
