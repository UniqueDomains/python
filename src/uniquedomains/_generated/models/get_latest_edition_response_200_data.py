from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_latest_edition_response_200_data_persona import (
    GetLatestEditionResponse200DataPersona,
    check_get_latest_edition_response_200_data_persona,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_latest_edition_response_200_data_trends_item import (
        GetLatestEditionResponse200DataTrendsItem,
    )


T = TypeVar("T", bound="GetLatestEditionResponse200Data")


@_attrs_define
class GetLatestEditionResponse200Data:
    """
    Attributes:
        persona (GetLatestEditionResponse200DataPersona | Unset):
        date (datetime.date | Unset):
        publish_at (datetime.datetime | Unset):
        trend_count (int | Unset):
        name_count (int | Unset):
        open_count (int | Unset):
        previous_date (datetime.date | None | Unset):
        next_date (datetime.date | None | Unset):
        trends (list[GetLatestEditionResponse200DataTrendsItem] | Unset):
    """

    persona: GetLatestEditionResponse200DataPersona | Unset = UNSET
    date: datetime.date | Unset = UNSET
    publish_at: datetime.datetime | Unset = UNSET
    trend_count: int | Unset = UNSET
    name_count: int | Unset = UNSET
    open_count: int | Unset = UNSET
    previous_date: datetime.date | None | Unset = UNSET
    next_date: datetime.date | None | Unset = UNSET
    trends: list[GetLatestEditionResponse200DataTrendsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        persona: str | Unset = UNSET
        if not isinstance(self.persona, Unset):
            persona = self.persona

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        publish_at: str | Unset = UNSET
        if not isinstance(self.publish_at, Unset):
            publish_at = self.publish_at.isoformat()

        trend_count = self.trend_count

        name_count = self.name_count

        open_count = self.open_count

        previous_date: None | str | Unset
        if isinstance(self.previous_date, Unset):
            previous_date = UNSET
        elif isinstance(self.previous_date, datetime.date):
            previous_date = self.previous_date.isoformat()
        else:
            previous_date = self.previous_date

        next_date: None | str | Unset
        if isinstance(self.next_date, Unset):
            next_date = UNSET
        elif isinstance(self.next_date, datetime.date):
            next_date = self.next_date.isoformat()
        else:
            next_date = self.next_date

        trends: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.trends, Unset):
            trends = []
            for trends_item_data in self.trends:
                trends_item = trends_item_data.to_dict()
                trends.append(trends_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if persona is not UNSET:
            field_dict["persona"] = persona
        if date is not UNSET:
            field_dict["date"] = date
        if publish_at is not UNSET:
            field_dict["publishAt"] = publish_at
        if trend_count is not UNSET:
            field_dict["trendCount"] = trend_count
        if name_count is not UNSET:
            field_dict["nameCount"] = name_count
        if open_count is not UNSET:
            field_dict["openCount"] = open_count
        if previous_date is not UNSET:
            field_dict["previousDate"] = previous_date
        if next_date is not UNSET:
            field_dict["nextDate"] = next_date
        if trends is not UNSET:
            field_dict["trends"] = trends

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_latest_edition_response_200_data_trends_item import (
            GetLatestEditionResponse200DataTrendsItem,
        )

        d = dict(src_dict)
        _persona = d.pop("persona", UNSET)
        persona: GetLatestEditionResponse200DataPersona | Unset
        if isinstance(_persona, Unset):
            persona = UNSET
        else:
            persona = check_get_latest_edition_response_200_data_persona(_persona)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)

        _publish_at = d.pop("publishAt", UNSET)
        publish_at: datetime.datetime | Unset
        if isinstance(_publish_at, Unset):
            publish_at = UNSET
        else:
            publish_at = datetime.datetime.fromisoformat(_publish_at)

        trend_count = d.pop("trendCount", UNSET)

        name_count = d.pop("nameCount", UNSET)

        open_count = d.pop("openCount", UNSET)

        def _parse_previous_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                previous_date_type_0 = datetime.date.fromisoformat(data)

                return previous_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        previous_date = _parse_previous_date(d.pop("previousDate", UNSET))

        def _parse_next_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_date_type_0 = datetime.date.fromisoformat(data)

                return next_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        next_date = _parse_next_date(d.pop("nextDate", UNSET))

        _trends = d.pop("trends", UNSET)
        trends: list[GetLatestEditionResponse200DataTrendsItem] | Unset = UNSET
        if _trends is not UNSET:
            trends = []
            for trends_item_data in _trends:
                trends_item = GetLatestEditionResponse200DataTrendsItem.from_dict(
                    trends_item_data
                )

                trends.append(trends_item)

        get_latest_edition_response_200_data = cls(
            persona=persona,
            date=date,
            publish_at=publish_at,
            trend_count=trend_count,
            name_count=name_count,
            open_count=open_count,
            previous_date=previous_date,
            next_date=next_date,
            trends=trends,
        )

        get_latest_edition_response_200_data.additional_properties = d
        return get_latest_edition_response_200_data

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
