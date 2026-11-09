from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_market_sales_word_response_200_data_status import (
    GetMarketSalesWordResponse200DataStatus,
    check_get_market_sales_word_response_200_data_status,
)

T = TypeVar("T", bound="GetMarketSalesWordResponse200Data")


@_attrs_define
class GetMarketSalesWordResponse200Data:
    """
    Attributes:
        status (GetMarketSalesWordResponse200DataStatus):
        word (str):
        sales12m (int):
        median_12_m_usd (int | None):
        endings_sold_on (int):
        last_sale_month (None | str): `YYYY-MM`.
    """

    status: GetMarketSalesWordResponse200DataStatus
    word: str
    sales12m: int
    median_12_m_usd: int | None
    endings_sold_on: int
    last_sale_month: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        word = self.word

        sales12m = self.sales12m

        median_12_m_usd: int | None
        median_12_m_usd = self.median_12_m_usd

        endings_sold_on = self.endings_sold_on

        last_sale_month: None | str
        last_sale_month = self.last_sale_month

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "word": word,
                "sales12m": sales12m,
                "median12mUsd": median_12_m_usd,
                "endingsSoldOn": endings_sold_on,
                "lastSaleMonth": last_sale_month,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = check_get_market_sales_word_response_200_data_status(d.pop("status"))

        word = d.pop("word")

        sales12m = d.pop("sales12m")

        def _parse_median_12_m_usd(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        median_12_m_usd = _parse_median_12_m_usd(d.pop("median12mUsd"))

        endings_sold_on = d.pop("endingsSoldOn")

        def _parse_last_sale_month(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_sale_month = _parse_last_sale_month(d.pop("lastSaleMonth"))

        get_market_sales_word_response_200_data = cls(
            status=status,
            word=word,
            sales12m=sales12m,
            median_12_m_usd=median_12_m_usd,
            endings_sold_on=endings_sold_on,
            last_sale_month=last_sale_month,
        )

        get_market_sales_word_response_200_data.additional_properties = d
        return get_market_sales_word_response_200_data

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
