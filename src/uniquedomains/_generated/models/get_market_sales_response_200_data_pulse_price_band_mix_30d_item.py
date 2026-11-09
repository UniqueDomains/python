from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_market_sales_response_200_data_pulse_price_band_mix_30d_item_band import (
    GetMarketSalesResponse200DataPulsePriceBandMix30DItemBand,
    check_get_market_sales_response_200_data_pulse_price_band_mix_30d_item_band,
)

T = TypeVar("T", bound="GetMarketSalesResponse200DataPulsePriceBandMix30DItem")


@_attrs_define
class GetMarketSalesResponse200DataPulsePriceBandMix30DItem:
    """
    Attributes:
        band (GetMarketSalesResponse200DataPulsePriceBandMix30DItemBand):
        count (int):
    """

    band: GetMarketSalesResponse200DataPulsePriceBandMix30DItemBand
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        band: str = self.band

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "band": band,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        band = (
            check_get_market_sales_response_200_data_pulse_price_band_mix_30d_item_band(
                d.pop("band")
            )
        )

        count = d.pop("count")

        get_market_sales_response_200_data_pulse_price_band_mix_30d_item = cls(
            band=band,
            count=count,
        )

        get_market_sales_response_200_data_pulse_price_band_mix_30d_item.additional_properties = d
        return get_market_sales_response_200_data_pulse_price_band_mix_30d_item

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
