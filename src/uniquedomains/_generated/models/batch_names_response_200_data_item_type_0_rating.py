from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.batch_names_response_200_data_item_type_0_rating_band_type_1 import (
    BatchNamesResponse200DataItemType0RatingBandType1,
    check_batch_names_response_200_data_item_type_0_rating_band_type_1,
)
from ..models.batch_names_response_200_data_item_type_0_rating_band_type_2_type_1 import (
    BatchNamesResponse200DataItemType0RatingBandType2Type1,
    check_batch_names_response_200_data_item_type_0_rating_band_type_2_type_1,
)
from ..models.batch_names_response_200_data_item_type_0_rating_band_type_3_type_1 import (
    BatchNamesResponse200DataItemType0RatingBandType3Type1,
    check_batch_names_response_200_data_item_type_0_rating_band_type_3_type_1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchNamesResponse200DataItemType0Rating")


@_attrs_define
class BatchNamesResponse200DataItemType0Rating:
    """
    Attributes:
        band (BatchNamesResponse200DataItemType0RatingBandType1 | BatchNamesResponse200DataItemType0RatingBandType2Type1
            | BatchNamesResponse200DataItemType0RatingBandType3Type1 | None | Unset):
        score (int | None | Unset): Keyed, on this endpoint only.
    """

    band: (
        BatchNamesResponse200DataItemType0RatingBandType1
        | BatchNamesResponse200DataItemType0RatingBandType2Type1
        | BatchNamesResponse200DataItemType0RatingBandType3Type1
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
            BatchNamesResponse200DataItemType0RatingBandType1
            | BatchNamesResponse200DataItemType0RatingBandType2Type1
            | BatchNamesResponse200DataItemType0RatingBandType3Type1
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
                band_type_1 = (
                    check_batch_names_response_200_data_item_type_0_rating_band_type_1(
                        data
                    )
                )

                return band_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                band_type_2_type_1 = check_batch_names_response_200_data_item_type_0_rating_band_type_2_type_1(
                    data
                )

                return band_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                band_type_3_type_1 = check_batch_names_response_200_data_item_type_0_rating_band_type_3_type_1(
                    data
                )

                return band_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                BatchNamesResponse200DataItemType0RatingBandType1
                | BatchNamesResponse200DataItemType0RatingBandType2Type1
                | BatchNamesResponse200DataItemType0RatingBandType3Type1
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

        batch_names_response_200_data_item_type_0_rating = cls(
            band=band,
            score=score,
        )

        batch_names_response_200_data_item_type_0_rating.additional_properties = d
        return batch_names_response_200_data_item_type_0_rating

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
