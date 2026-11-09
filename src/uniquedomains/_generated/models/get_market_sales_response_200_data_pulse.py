from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_market_sales_response_200_data_pulse_price_band_mix_12m_item import (
        GetMarketSalesResponse200DataPulsePriceBandMix12MItem,
    )
    from ..models.get_market_sales_response_200_data_pulse_price_band_mix_30d_item import (
        GetMarketSalesResponse200DataPulsePriceBandMix30DItem,
    )
    from ..models.get_market_sales_response_200_data_pulse_windows_item import (
        GetMarketSalesResponse200DataPulseWindowsItem,
    )


T = TypeVar("T", bound="GetMarketSalesResponse200DataPulse")


@_attrs_define
class GetMarketSalesResponse200DataPulse:
    """
    Attributes:
        windows (list[GetMarketSalesResponse200DataPulseWindowsItem]):
        price_band_mix_30_d (list[GetMarketSalesResponse200DataPulsePriceBandMix30DItem]):
        price_band_mix_12_m (list[GetMarketSalesResponse200DataPulsePriceBandMix12MItem]):
    """

    windows: list[GetMarketSalesResponse200DataPulseWindowsItem]
    price_band_mix_30_d: list[GetMarketSalesResponse200DataPulsePriceBandMix30DItem]
    price_band_mix_12_m: list[GetMarketSalesResponse200DataPulsePriceBandMix12MItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        windows = []
        for windows_item_data in self.windows:
            windows_item = windows_item_data.to_dict()
            windows.append(windows_item)

        price_band_mix_30_d = []
        for price_band_mix_30_d_item_data in self.price_band_mix_30_d:
            price_band_mix_30_d_item = price_band_mix_30_d_item_data.to_dict()
            price_band_mix_30_d.append(price_band_mix_30_d_item)

        price_band_mix_12_m = []
        for price_band_mix_12_m_item_data in self.price_band_mix_12_m:
            price_band_mix_12_m_item = price_band_mix_12_m_item_data.to_dict()
            price_band_mix_12_m.append(price_band_mix_12_m_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "windows": windows,
                "priceBandMix30d": price_band_mix_30_d,
                "priceBandMix12m": price_band_mix_12_m,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_market_sales_response_200_data_pulse_price_band_mix_12m_item import (
            GetMarketSalesResponse200DataPulsePriceBandMix12MItem,
        )
        from ..models.get_market_sales_response_200_data_pulse_price_band_mix_30d_item import (
            GetMarketSalesResponse200DataPulsePriceBandMix30DItem,
        )
        from ..models.get_market_sales_response_200_data_pulse_windows_item import (
            GetMarketSalesResponse200DataPulseWindowsItem,
        )

        d = dict(src_dict)
        windows = []
        _windows = d.pop("windows")
        for windows_item_data in _windows:
            windows_item = GetMarketSalesResponse200DataPulseWindowsItem.from_dict(
                windows_item_data
            )

            windows.append(windows_item)

        price_band_mix_30_d = []
        _price_band_mix_30_d = d.pop("priceBandMix30d")
        for price_band_mix_30_d_item_data in _price_band_mix_30_d:
            price_band_mix_30_d_item = (
                GetMarketSalesResponse200DataPulsePriceBandMix30DItem.from_dict(
                    price_band_mix_30_d_item_data
                )
            )

            price_band_mix_30_d.append(price_band_mix_30_d_item)

        price_band_mix_12_m = []
        _price_band_mix_12_m = d.pop("priceBandMix12m")
        for price_band_mix_12_m_item_data in _price_band_mix_12_m:
            price_band_mix_12_m_item = (
                GetMarketSalesResponse200DataPulsePriceBandMix12MItem.from_dict(
                    price_band_mix_12_m_item_data
                )
            )

            price_band_mix_12_m.append(price_band_mix_12_m_item)

        get_market_sales_response_200_data_pulse = cls(
            windows=windows,
            price_band_mix_30_d=price_band_mix_30_d,
            price_band_mix_12_m=price_band_mix_12_m,
        )

        get_market_sales_response_200_data_pulse.additional_properties = d
        return get_market_sales_response_200_data_pulse

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
