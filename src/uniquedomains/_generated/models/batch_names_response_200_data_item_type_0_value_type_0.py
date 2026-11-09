from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.batch_names_response_200_data_item_type_0_value_type_0_liquidity_type_1 import (
    BatchNamesResponse200DataItemType0ValueType0LiquidityType1,
    check_batch_names_response_200_data_item_type_0_value_type_0_liquidity_type_1,
)
from ..models.batch_names_response_200_data_item_type_0_value_type_0_liquidity_type_2_type_1 import (
    BatchNamesResponse200DataItemType0ValueType0LiquidityType2Type1,
    check_batch_names_response_200_data_item_type_0_value_type_0_liquidity_type_2_type_1,
)
from ..models.batch_names_response_200_data_item_type_0_value_type_0_liquidity_type_3_type_1 import (
    BatchNamesResponse200DataItemType0ValueType0LiquidityType3Type1,
    check_batch_names_response_200_data_item_type_0_value_type_0_liquidity_type_3_type_1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchNamesResponse200DataItemType0ValueType0")


@_attrs_define
class BatchNamesResponse200DataItemType0ValueType0:
    """Keyed.

    Attributes:
        value (int | Unset):
        upside_percent (float | None | Unset):
        liquidity (BatchNamesResponse200DataItemType0ValueType0LiquidityType1 |
            BatchNamesResponse200DataItemType0ValueType0LiquidityType2Type1 |
            BatchNamesResponse200DataItemType0ValueType0LiquidityType3Type1 | None | Unset):
    """

    value: int | Unset = UNSET
    upside_percent: float | None | Unset = UNSET
    liquidity: (
        BatchNamesResponse200DataItemType0ValueType0LiquidityType1
        | BatchNamesResponse200DataItemType0ValueType0LiquidityType2Type1
        | BatchNamesResponse200DataItemType0ValueType0LiquidityType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        upside_percent: float | None | Unset
        if isinstance(self.upside_percent, Unset):
            upside_percent = UNSET
        else:
            upside_percent = self.upside_percent

        liquidity: None | str | Unset
        if isinstance(self.liquidity, Unset):
            liquidity = UNSET
        elif (
            isinstance(self.liquidity, str)
            or isinstance(self.liquidity, str)
            or isinstance(self.liquidity, str)
        ):
            liquidity = self.liquidity
        else:
            liquidity = self.liquidity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if upside_percent is not UNSET:
            field_dict["upsidePercent"] = upside_percent
        if liquidity is not UNSET:
            field_dict["liquidity"] = liquidity

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        def _parse_upside_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        upside_percent = _parse_upside_percent(d.pop("upsidePercent", UNSET))

        def _parse_liquidity(
            data: object,
        ) -> (
            BatchNamesResponse200DataItemType0ValueType0LiquidityType1
            | BatchNamesResponse200DataItemType0ValueType0LiquidityType2Type1
            | BatchNamesResponse200DataItemType0ValueType0LiquidityType3Type1
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
                liquidity_type_1 = check_batch_names_response_200_data_item_type_0_value_type_0_liquidity_type_1(
                    data
                )

                return liquidity_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                liquidity_type_2_type_1 = check_batch_names_response_200_data_item_type_0_value_type_0_liquidity_type_2_type_1(
                    data
                )

                return liquidity_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                liquidity_type_3_type_1 = check_batch_names_response_200_data_item_type_0_value_type_0_liquidity_type_3_type_1(
                    data
                )

                return liquidity_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                BatchNamesResponse200DataItemType0ValueType0LiquidityType1
                | BatchNamesResponse200DataItemType0ValueType0LiquidityType2Type1
                | BatchNamesResponse200DataItemType0ValueType0LiquidityType3Type1
                | None
                | Unset,
                data,
            )

        liquidity = _parse_liquidity(d.pop("liquidity", UNSET))

        batch_names_response_200_data_item_type_0_value_type_0 = cls(
            value=value,
            upside_percent=upside_percent,
            liquidity=liquidity,
        )

        batch_names_response_200_data_item_type_0_value_type_0.additional_properties = d
        return batch_names_response_200_data_item_type_0_value_type_0

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
