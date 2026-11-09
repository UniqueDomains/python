from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_trend_response_200_data_editions_item_persona import (
    GetTrendResponse200DataEditionsItemPersona,
    check_get_trend_response_200_data_editions_item_persona,
)

T = TypeVar("T", bound="GetTrendResponse200DataEditionsItem")


@_attrs_define
class GetTrendResponse200DataEditionsItem:
    """
    Attributes:
        date (datetime.date):
        persona (GetTrendResponse200DataEditionsItemPersona):
        searches (int | None):
        growth (int | None):
    """

    date: datetime.date
    persona: GetTrendResponse200DataEditionsItemPersona
    searches: int | None
    growth: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        persona: str = self.persona

        searches: int | None
        searches = self.searches

        growth: int | None
        growth = self.growth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "persona": persona,
                "searches": searches,
                "growth": growth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        persona = check_get_trend_response_200_data_editions_item_persona(
            d.pop("persona")
        )

        def _parse_searches(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        searches = _parse_searches(d.pop("searches"))

        def _parse_growth(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        growth = _parse_growth(d.pop("growth"))

        get_trend_response_200_data_editions_item = cls(
            date=date,
            persona=persona,
            searches=searches,
            growth=growth,
        )

        get_trend_response_200_data_editions_item.additional_properties = d
        return get_trend_response_200_data_editions_item

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
