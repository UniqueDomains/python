from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_market_sales_response_200_data_freshness import (
        GetMarketSalesResponse200DataFreshness,
    )
    from ..models.get_market_sales_response_200_data_pulse import (
        GetMarketSalesResponse200DataPulse,
    )
    from ..models.get_market_sales_response_200_data_sold_before import (
        GetMarketSalesResponse200DataSoldBefore,
    )


T = TypeVar("T", bound="GetMarketSalesResponse200Data")


@_attrs_define
class GetMarketSalesResponse200Data:
    """
    Attributes:
        freshness (GetMarketSalesResponse200DataFreshness):
        pulse (GetMarketSalesResponse200DataPulse):
        sold_before (GetMarketSalesResponse200DataSoldBefore):
    """

    freshness: GetMarketSalesResponse200DataFreshness
    pulse: GetMarketSalesResponse200DataPulse
    sold_before: GetMarketSalesResponse200DataSoldBefore
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        freshness = self.freshness.to_dict()

        pulse = self.pulse.to_dict()

        sold_before = self.sold_before.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "freshness": freshness,
                "pulse": pulse,
                "soldBefore": sold_before,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_market_sales_response_200_data_freshness import (
            GetMarketSalesResponse200DataFreshness,
        )
        from ..models.get_market_sales_response_200_data_pulse import (
            GetMarketSalesResponse200DataPulse,
        )
        from ..models.get_market_sales_response_200_data_sold_before import (
            GetMarketSalesResponse200DataSoldBefore,
        )

        d = dict(src_dict)
        freshness = GetMarketSalesResponse200DataFreshness.from_dict(d.pop("freshness"))

        pulse = GetMarketSalesResponse200DataPulse.from_dict(d.pop("pulse"))

        sold_before = GetMarketSalesResponse200DataSoldBefore.from_dict(
            d.pop("soldBefore")
        )

        get_market_sales_response_200_data = cls(
            freshness=freshness,
            pulse=pulse,
            sold_before=sold_before,
        )

        get_market_sales_response_200_data.additional_properties = d
        return get_market_sales_response_200_data

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
