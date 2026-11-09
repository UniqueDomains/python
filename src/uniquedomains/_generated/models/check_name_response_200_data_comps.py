from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_name_response_200_data_comps_tier_type_1 import (
    CheckNameResponse200DataCompsTierType1,
    check_check_name_response_200_data_comps_tier_type_1,
)
from ..models.check_name_response_200_data_comps_tier_type_2_type_1 import (
    CheckNameResponse200DataCompsTierType2Type1,
    check_check_name_response_200_data_comps_tier_type_2_type_1,
)
from ..models.check_name_response_200_data_comps_tier_type_3_type_1 import (
    CheckNameResponse200DataCompsTierType3Type1,
    check_check_name_response_200_data_comps_tier_type_3_type_1,
)

T = TypeVar("T", bound="CheckNameResponse200DataComps")


@_attrs_define
class CheckNameResponse200DataComps:
    """
    Attributes:
        tier (CheckNameResponse200DataCompsTierType1 | CheckNameResponse200DataCompsTierType2Type1 |
            CheckNameResponse200DataCompsTierType3Type1 | None): `sold_before` (this exact name sold before) on keyed
            answers only.
        count (int):
        median_usd (float | None):
        endings_sold_on (int): Endings the word sold on in 12 months.
    """

    tier: (
        CheckNameResponse200DataCompsTierType1
        | CheckNameResponse200DataCompsTierType2Type1
        | CheckNameResponse200DataCompsTierType3Type1
        | None
    )
    count: int
    median_usd: float | None
    endings_sold_on: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tier: None | str
        if (
            isinstance(self.tier, str)
            or isinstance(self.tier, str)
            or isinstance(self.tier, str)
        ):
            tier = self.tier
        else:
            tier = self.tier

        count = self.count

        median_usd: float | None
        median_usd = self.median_usd

        endings_sold_on = self.endings_sold_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tier": tier,
                "count": count,
                "medianUsd": median_usd,
                "endingsSoldOn": endings_sold_on,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_tier(
            data: object,
        ) -> (
            CheckNameResponse200DataCompsTierType1
            | CheckNameResponse200DataCompsTierType2Type1
            | CheckNameResponse200DataCompsTierType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tier_type_1 = check_check_name_response_200_data_comps_tier_type_1(data)

                return tier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tier_type_2_type_1 = (
                    check_check_name_response_200_data_comps_tier_type_2_type_1(data)
                )

                return tier_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tier_type_3_type_1 = (
                    check_check_name_response_200_data_comps_tier_type_3_type_1(data)
                )

                return tier_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CheckNameResponse200DataCompsTierType1
                | CheckNameResponse200DataCompsTierType2Type1
                | CheckNameResponse200DataCompsTierType3Type1
                | None,
                data,
            )

        tier = _parse_tier(d.pop("tier"))

        count = d.pop("count")

        def _parse_median_usd(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        median_usd = _parse_median_usd(d.pop("medianUsd"))

        endings_sold_on = d.pop("endingsSoldOn")

        check_name_response_200_data_comps = cls(
            tier=tier,
            count=count,
            median_usd=median_usd,
            endings_sold_on=endings_sold_on,
        )

        check_name_response_200_data_comps.additional_properties = d
        return check_name_response_200_data_comps

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
