from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_latest_edition_response_200_data_trends_item_rows_item_verdict_type_0_confidence import (
    GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0Confidence,
    check_get_latest_edition_response_200_data_trends_item_rows_item_verdict_type_0_confidence,
)
from ..models.get_latest_edition_response_200_data_trends_item_rows_item_verdict_type_0_label import (
    GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0Label,
    check_get_latest_edition_response_200_data_trends_item_rows_item_verdict_type_0_label,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0")


@_attrs_define
class GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0:
    """
    Attributes:
        label (GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0Label | Unset):
        confidence (GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0Confidence | Unset):
    """

    label: (
        GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0Label | Unset
    ) = UNSET
    confidence: (
        GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0Confidence | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label: str | Unset = UNSET
        if not isinstance(self.label, Unset):
            label = self.label

        confidence: str | Unset = UNSET
        if not isinstance(self.confidence, Unset):
            confidence = self.confidence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if confidence is not UNSET:
            field_dict["confidence"] = confidence

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _label = d.pop("label", UNSET)
        label: (
            GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0Label | Unset
        )
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = check_get_latest_edition_response_200_data_trends_item_rows_item_verdict_type_0_label(
                _label
            )

        _confidence = d.pop("confidence", UNSET)
        confidence: (
            GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0Confidence
            | Unset
        )
        if isinstance(_confidence, Unset):
            confidence = UNSET
        else:
            confidence = check_get_latest_edition_response_200_data_trends_item_rows_item_verdict_type_0_confidence(
                _confidence
            )

        get_latest_edition_response_200_data_trends_item_rows_item_verdict_type_0 = cls(
            label=label,
            confidence=confidence,
        )

        get_latest_edition_response_200_data_trends_item_rows_item_verdict_type_0.additional_properties = d
        return get_latest_edition_response_200_data_trends_item_rows_item_verdict_type_0

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
