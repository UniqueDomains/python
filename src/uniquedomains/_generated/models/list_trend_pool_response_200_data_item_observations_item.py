from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_trend_pool_response_200_data_item_observations_item_growth_window_type_1 import (
    ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType1,
    check_list_trend_pool_response_200_data_item_observations_item_growth_window_type_1,
)
from ..models.list_trend_pool_response_200_data_item_observations_item_growth_window_type_2_type_1 import (
    ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType2Type1,
    check_list_trend_pool_response_200_data_item_observations_item_growth_window_type_2_type_1,
)
from ..models.list_trend_pool_response_200_data_item_observations_item_growth_window_type_3_type_1 import (
    ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType3Type1,
    check_list_trend_pool_response_200_data_item_observations_item_growth_window_type_3_type_1,
)

T = TypeVar("T", bound="ListTrendPoolResponse200DataItemObservationsItem")


@_attrs_define
class ListTrendPoolResponse200DataItemObservationsItem:
    """
    Attributes:
        volume (int | None):
        growth (int | None):
        growth_window (ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType1 |
            ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType2Type1 |
            ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType3Type1 | None):
        observed_at (datetime.datetime):
    """

    volume: int | None
    growth: int | None
    growth_window: (
        ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType1
        | ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType2Type1
        | ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType3Type1
        | None
    )
    observed_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume: int | None
        volume = self.volume

        growth: int | None
        growth = self.growth

        growth_window: None | str
        if (
            isinstance(self.growth_window, str)
            or isinstance(self.growth_window, str)
            or isinstance(self.growth_window, str)
        ):
            growth_window = self.growth_window
        else:
            growth_window = self.growth_window

        observed_at = self.observed_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "volume": volume,
                "growth": growth,
                "growthWindow": growth_window,
                "observedAt": observed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_volume(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        volume = _parse_volume(d.pop("volume"))

        def _parse_growth(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        growth = _parse_growth(d.pop("growth"))

        def _parse_growth_window(
            data: object,
        ) -> (
            ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType1
            | ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType2Type1
            | ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                growth_window_type_1 = check_list_trend_pool_response_200_data_item_observations_item_growth_window_type_1(
                    data
                )

                return growth_window_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                growth_window_type_2_type_1 = check_list_trend_pool_response_200_data_item_observations_item_growth_window_type_2_type_1(
                    data
                )

                return growth_window_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                growth_window_type_3_type_1 = check_list_trend_pool_response_200_data_item_observations_item_growth_window_type_3_type_1(
                    data
                )

                return growth_window_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType1
                | ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType2Type1
                | ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType3Type1
                | None,
                data,
            )

        growth_window = _parse_growth_window(d.pop("growthWindow"))

        observed_at = datetime.datetime.fromisoformat(d.pop("observedAt"))

        list_trend_pool_response_200_data_item_observations_item = cls(
            volume=volume,
            growth=growth,
            growth_window=growth_window,
            observed_at=observed_at,
        )

        list_trend_pool_response_200_data_item_observations_item.additional_properties = d
        return list_trend_pool_response_200_data_item_observations_item

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
