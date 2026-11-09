from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.batch_names_response_200_data_item_type_0_verdict_type_0_confidence_type_1 import (
    BatchNamesResponse200DataItemType0VerdictType0ConfidenceType1,
    check_batch_names_response_200_data_item_type_0_verdict_type_0_confidence_type_1,
)
from ..models.batch_names_response_200_data_item_type_0_verdict_type_0_confidence_type_2_type_1 import (
    BatchNamesResponse200DataItemType0VerdictType0ConfidenceType2Type1,
    check_batch_names_response_200_data_item_type_0_verdict_type_0_confidence_type_2_type_1,
)
from ..models.batch_names_response_200_data_item_type_0_verdict_type_0_confidence_type_3_type_1 import (
    BatchNamesResponse200DataItemType0VerdictType0ConfidenceType3Type1,
    check_batch_names_response_200_data_item_type_0_verdict_type_0_confidence_type_3_type_1,
)
from ..models.batch_names_response_200_data_item_type_0_verdict_type_0_rating import (
    BatchNamesResponse200DataItemType0VerdictType0Rating,
    check_batch_names_response_200_data_item_type_0_verdict_type_0_rating,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchNamesResponse200DataItemType0VerdictType0")


@_attrs_define
class BatchNamesResponse200DataItemType0VerdictType0:
    """Keyed.

    Attributes:
        rating (BatchNamesResponse200DataItemType0VerdictType0Rating | Unset):
        confidence (BatchNamesResponse200DataItemType0VerdictType0ConfidenceType1 |
            BatchNamesResponse200DataItemType0VerdictType0ConfidenceType2Type1 |
            BatchNamesResponse200DataItemType0VerdictType0ConfidenceType3Type1 | None | Unset):
    """

    rating: BatchNamesResponse200DataItemType0VerdictType0Rating | Unset = UNSET
    confidence: (
        BatchNamesResponse200DataItemType0VerdictType0ConfidenceType1
        | BatchNamesResponse200DataItemType0VerdictType0ConfidenceType2Type1
        | BatchNamesResponse200DataItemType0VerdictType0ConfidenceType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rating: str | Unset = UNSET
        if not isinstance(self.rating, Unset):
            rating = self.rating

        confidence: None | str | Unset
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        elif (
            isinstance(self.confidence, str)
            or isinstance(self.confidence, str)
            or isinstance(self.confidence, str)
        ):
            confidence = self.confidence
        else:
            confidence = self.confidence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rating is not UNSET:
            field_dict["rating"] = rating
        if confidence is not UNSET:
            field_dict["confidence"] = confidence

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _rating = d.pop("rating", UNSET)
        rating: BatchNamesResponse200DataItemType0VerdictType0Rating | Unset
        if isinstance(_rating, Unset):
            rating = UNSET
        else:
            rating = (
                check_batch_names_response_200_data_item_type_0_verdict_type_0_rating(
                    _rating
                )
            )

        def _parse_confidence(
            data: object,
        ) -> (
            BatchNamesResponse200DataItemType0VerdictType0ConfidenceType1
            | BatchNamesResponse200DataItemType0VerdictType0ConfidenceType2Type1
            | BatchNamesResponse200DataItemType0VerdictType0ConfidenceType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confidence_type_1 = check_batch_names_response_200_data_item_type_0_verdict_type_0_confidence_type_1(
                    data
                )

                return confidence_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confidence_type_2_type_1 = check_batch_names_response_200_data_item_type_0_verdict_type_0_confidence_type_2_type_1(
                    data
                )

                return confidence_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confidence_type_3_type_1 = check_batch_names_response_200_data_item_type_0_verdict_type_0_confidence_type_3_type_1(
                    data
                )

                return confidence_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                BatchNamesResponse200DataItemType0VerdictType0ConfidenceType1
                | BatchNamesResponse200DataItemType0VerdictType0ConfidenceType2Type1
                | BatchNamesResponse200DataItemType0VerdictType0ConfidenceType3Type1
                | None
                | Unset,
                data,
            )

        confidence = _parse_confidence(d.pop("confidence", UNSET))

        batch_names_response_200_data_item_type_0_verdict_type_0 = cls(
            rating=rating,
            confidence=confidence,
        )

        batch_names_response_200_data_item_type_0_verdict_type_0.additional_properties = d
        return batch_names_response_200_data_item_type_0_verdict_type_0

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
