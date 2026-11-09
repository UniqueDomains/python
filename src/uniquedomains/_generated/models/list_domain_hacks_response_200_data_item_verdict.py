from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_domain_hacks_response_200_data_item_verdict_confidence_type_1 import (
    ListDomainHacksResponse200DataItemVerdictConfidenceType1,
    check_list_domain_hacks_response_200_data_item_verdict_confidence_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_verdict_confidence_type_2_type_1 import (
    ListDomainHacksResponse200DataItemVerdictConfidenceType2Type1,
    check_list_domain_hacks_response_200_data_item_verdict_confidence_type_2_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_verdict_confidence_type_3_type_1 import (
    ListDomainHacksResponse200DataItemVerdictConfidenceType3Type1,
    check_list_domain_hacks_response_200_data_item_verdict_confidence_type_3_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_verdict_rating import (
    ListDomainHacksResponse200DataItemVerdictRating,
    check_list_domain_hacks_response_200_data_item_verdict_rating,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListDomainHacksResponse200DataItemVerdict")


@_attrs_define
class ListDomainHacksResponse200DataItemVerdict:
    """Keyed.

    Attributes:
        rating (ListDomainHacksResponse200DataItemVerdictRating | Unset):
        confidence (ListDomainHacksResponse200DataItemVerdictConfidenceType1 |
            ListDomainHacksResponse200DataItemVerdictConfidenceType2Type1 |
            ListDomainHacksResponse200DataItemVerdictConfidenceType3Type1 | None | Unset):
    """

    rating: ListDomainHacksResponse200DataItemVerdictRating | Unset = UNSET
    confidence: (
        ListDomainHacksResponse200DataItemVerdictConfidenceType1
        | ListDomainHacksResponse200DataItemVerdictConfidenceType2Type1
        | ListDomainHacksResponse200DataItemVerdictConfidenceType3Type1
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
        rating: ListDomainHacksResponse200DataItemVerdictRating | Unset
        if isinstance(_rating, Unset):
            rating = UNSET
        else:
            rating = check_list_domain_hacks_response_200_data_item_verdict_rating(
                _rating
            )

        def _parse_confidence(
            data: object,
        ) -> (
            ListDomainHacksResponse200DataItemVerdictConfidenceType1
            | ListDomainHacksResponse200DataItemVerdictConfidenceType2Type1
            | ListDomainHacksResponse200DataItemVerdictConfidenceType3Type1
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
                confidence_type_1 = check_list_domain_hacks_response_200_data_item_verdict_confidence_type_1(
                    data
                )

                return confidence_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confidence_type_2_type_1 = check_list_domain_hacks_response_200_data_item_verdict_confidence_type_2_type_1(
                    data
                )

                return confidence_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confidence_type_3_type_1 = check_list_domain_hacks_response_200_data_item_verdict_confidence_type_3_type_1(
                    data
                )

                return confidence_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListDomainHacksResponse200DataItemVerdictConfidenceType1
                | ListDomainHacksResponse200DataItemVerdictConfidenceType2Type1
                | ListDomainHacksResponse200DataItemVerdictConfidenceType3Type1
                | None
                | Unset,
                data,
            )

        confidence = _parse_confidence(d.pop("confidence", UNSET))

        list_domain_hacks_response_200_data_item_verdict = cls(
            rating=rating,
            confidence=confidence,
        )

        list_domain_hacks_response_200_data_item_verdict.additional_properties = d
        return list_domain_hacks_response_200_data_item_verdict

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
