from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_tlds_response_200_data_item_insights_type_0_market_type_0 import (
        ListTldsResponse200DataItemInsightsType0MarketType0,
    )


T = TypeVar("T", bound="ListTldsResponse200DataItemInsightsType0")


@_attrs_define
class ListTldsResponse200DataItemInsightsType0:
    """
    Attributes:
        insight_url (str):
        market (ListTldsResponse200DataItemInsightsType0MarketType0 | None):
    """

    insight_url: str
    market: ListTldsResponse200DataItemInsightsType0MarketType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_tlds_response_200_data_item_insights_type_0_market_type_0 import (
            ListTldsResponse200DataItemInsightsType0MarketType0,
        )

        insight_url = self.insight_url

        market: dict[str, Any] | None
        if isinstance(self.market, ListTldsResponse200DataItemInsightsType0MarketType0):
            market = self.market.to_dict()
        else:
            market = self.market

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "insightUrl": insight_url,
                "market": market,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_tlds_response_200_data_item_insights_type_0_market_type_0 import (
            ListTldsResponse200DataItemInsightsType0MarketType0,
        )

        d = dict(src_dict)
        insight_url = d.pop("insightUrl")

        def _parse_market(
            data: object,
        ) -> ListTldsResponse200DataItemInsightsType0MarketType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                market_type_0 = (
                    ListTldsResponse200DataItemInsightsType0MarketType0.from_dict(data)
                )

                return market_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListTldsResponse200DataItemInsightsType0MarketType0 | None, data
            )

        market = _parse_market(d.pop("market"))

        list_tlds_response_200_data_item_insights_type_0 = cls(
            insight_url=insight_url,
            market=market,
        )

        list_tlds_response_200_data_item_insights_type_0.additional_properties = d
        return list_tlds_response_200_data_item_insights_type_0

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
