from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_name_response_200_data_rating_band_type_1 import (
    CheckNameResponse200DataRatingBandType1,
    check_check_name_response_200_data_rating_band_type_1,
)
from ..models.check_name_response_200_data_rating_band_type_2_type_1 import (
    CheckNameResponse200DataRatingBandType2Type1,
    check_check_name_response_200_data_rating_band_type_2_type_1,
)
from ..models.check_name_response_200_data_rating_band_type_3_type_1 import (
    CheckNameResponse200DataRatingBandType3Type1,
    check_check_name_response_200_data_rating_band_type_3_type_1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckNameResponse200DataRating")


@_attrs_define
class CheckNameResponse200DataRating:
    """
    Attributes:
        band (CheckNameResponse200DataRatingBandType1 | CheckNameResponse200DataRatingBandType2Type1 |
            CheckNameResponse200DataRatingBandType3Type1 | None | Unset):
        score (int | None | Unset): Keyed, on this endpoint only.
    """

    band: (
        CheckNameResponse200DataRatingBandType1
        | CheckNameResponse200DataRatingBandType2Type1
        | CheckNameResponse200DataRatingBandType3Type1
        | None
        | Unset
    ) = UNSET
    score: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        band: None | str | Unset
        if isinstance(self.band, Unset):
            band = UNSET
        elif (
            isinstance(self.band, str)
            or isinstance(self.band, str)
            or isinstance(self.band, str)
        ):
            band = self.band
        else:
            band = self.band

        score: int | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if band is not UNSET:
            field_dict["band"] = band
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_band(
            data: object,
        ) -> (
            CheckNameResponse200DataRatingBandType1
            | CheckNameResponse200DataRatingBandType2Type1
            | CheckNameResponse200DataRatingBandType3Type1
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
                band_type_1 = check_check_name_response_200_data_rating_band_type_1(
                    data
                )

                return band_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                band_type_2_type_1 = (
                    check_check_name_response_200_data_rating_band_type_2_type_1(data)
                )

                return band_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                band_type_3_type_1 = (
                    check_check_name_response_200_data_rating_band_type_3_type_1(data)
                )

                return band_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CheckNameResponse200DataRatingBandType1
                | CheckNameResponse200DataRatingBandType2Type1
                | CheckNameResponse200DataRatingBandType3Type1
                | None
                | Unset,
                data,
            )

        band = _parse_band(d.pop("band", UNSET))

        def _parse_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        check_name_response_200_data_rating = cls(
            band=band,
            score=score,
        )

        check_name_response_200_data_rating.additional_properties = d
        return check_name_response_200_data_rating

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
