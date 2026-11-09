from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_events_response_200_data_item_category_type_1 import (
    ListEventsResponse200DataItemCategoryType1,
    check_list_events_response_200_data_item_category_type_1,
)
from ..models.list_events_response_200_data_item_category_type_2_type_1 import (
    ListEventsResponse200DataItemCategoryType2Type1,
    check_list_events_response_200_data_item_category_type_2_type_1,
)
from ..models.list_events_response_200_data_item_category_type_3_type_1 import (
    ListEventsResponse200DataItemCategoryType3Type1,
    check_list_events_response_200_data_item_category_type_3_type_1,
)
from ..models.list_events_response_200_data_item_kind import (
    ListEventsResponse200DataItemKind,
    check_list_events_response_200_data_item_kind,
)

T = TypeVar("T", bound="ListEventsResponse200DataItem")


@_attrs_define
class ListEventsResponse200DataItem:
    """
    Attributes:
        id (UUID):
        slug (str):
        title (str):
        starts_on (datetime.date | None):
        ends_on (datetime.date | None): Inclusive last day; null for one day.
        category (ListEventsResponse200DataItemCategoryType1 | ListEventsResponse200DataItemCategoryType2Type1 |
            ListEventsResponse200DataItemCategoryType3Type1 | None):
        country_code (None | str):
        city (None | str):
        lat (float | None):
        lng (float | None):
        kind (ListEventsResponse200DataItemKind):
    """

    id: UUID
    slug: str
    title: str
    starts_on: datetime.date | None
    ends_on: datetime.date | None
    category: (
        ListEventsResponse200DataItemCategoryType1
        | ListEventsResponse200DataItemCategoryType2Type1
        | ListEventsResponse200DataItemCategoryType3Type1
        | None
    )
    country_code: None | str
    city: None | str
    lat: float | None
    lng: float | None
    kind: ListEventsResponse200DataItemKind
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        slug = self.slug

        title = self.title

        starts_on: None | str
        if isinstance(self.starts_on, datetime.date):
            starts_on = self.starts_on.isoformat()
        else:
            starts_on = self.starts_on

        ends_on: None | str
        if isinstance(self.ends_on, datetime.date):
            ends_on = self.ends_on.isoformat()
        else:
            ends_on = self.ends_on

        category: None | str
        if (
            isinstance(self.category, str)
            or isinstance(self.category, str)
            or isinstance(self.category, str)
        ):
            category = self.category
        else:
            category = self.category

        country_code: None | str
        country_code = self.country_code

        city: None | str
        city = self.city

        lat: float | None
        lat = self.lat

        lng: float | None
        lng = self.lng

        kind: str = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "title": title,
                "startsOn": starts_on,
                "endsOn": ends_on,
                "category": category,
                "countryCode": country_code,
                "city": city,
                "lat": lat,
                "lng": lng,
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        slug = d.pop("slug")

        title = d.pop("title")

        def _parse_starts_on(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                starts_on_type_0 = datetime.date.fromisoformat(data)

                return starts_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        starts_on = _parse_starts_on(d.pop("startsOn"))

        def _parse_ends_on(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ends_on_type_0 = datetime.date.fromisoformat(data)

                return ends_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        ends_on = _parse_ends_on(d.pop("endsOn"))

        def _parse_category(
            data: object,
        ) -> (
            ListEventsResponse200DataItemCategoryType1
            | ListEventsResponse200DataItemCategoryType2Type1
            | ListEventsResponse200DataItemCategoryType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_1 = (
                    check_list_events_response_200_data_item_category_type_1(data)
                )

                return category_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_2_type_1 = (
                    check_list_events_response_200_data_item_category_type_2_type_1(
                        data
                    )
                )

                return category_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_3_type_1 = (
                    check_list_events_response_200_data_item_category_type_3_type_1(
                        data
                    )
                )

                return category_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListEventsResponse200DataItemCategoryType1
                | ListEventsResponse200DataItemCategoryType2Type1
                | ListEventsResponse200DataItemCategoryType3Type1
                | None,
                data,
            )

        category = _parse_category(d.pop("category"))

        def _parse_country_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country_code = _parse_country_code(d.pop("countryCode"))

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

        def _parse_lat(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        lat = _parse_lat(d.pop("lat"))

        def _parse_lng(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        lng = _parse_lng(d.pop("lng"))

        kind = check_list_events_response_200_data_item_kind(d.pop("kind"))

        list_events_response_200_data_item = cls(
            id=id,
            slug=slug,
            title=title,
            starts_on=starts_on,
            ends_on=ends_on,
            category=category,
            country_code=country_code,
            city=city,
            lat=lat,
            lng=lng,
            kind=kind,
        )

        list_events_response_200_data_item.additional_properties = d
        return list_events_response_200_data_item

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
