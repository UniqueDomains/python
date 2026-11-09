from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_agenda_response_200_data_undated_item_category_type_1 import (
    GetAgendaResponse200DataUndatedItemCategoryType1,
    check_get_agenda_response_200_data_undated_item_category_type_1,
)
from ..models.get_agenda_response_200_data_undated_item_category_type_2_type_1 import (
    GetAgendaResponse200DataUndatedItemCategoryType2Type1,
    check_get_agenda_response_200_data_undated_item_category_type_2_type_1,
)
from ..models.get_agenda_response_200_data_undated_item_category_type_3_type_1 import (
    GetAgendaResponse200DataUndatedItemCategoryType3Type1,
    check_get_agenda_response_200_data_undated_item_category_type_3_type_1,
)
from ..models.get_agenda_response_200_data_undated_item_kind import (
    GetAgendaResponse200DataUndatedItemKind,
    check_get_agenda_response_200_data_undated_item_kind,
)

T = TypeVar("T", bound="GetAgendaResponse200DataUndatedItem")


@_attrs_define
class GetAgendaResponse200DataUndatedItem:
    """
    Attributes:
        id (str):
        kind (GetAgendaResponse200DataUndatedItemKind):
        title (str):
        starts_on (datetime.date | None):
        ends_on (datetime.date | None):
        category (GetAgendaResponse200DataUndatedItemCategoryType1 |
            GetAgendaResponse200DataUndatedItemCategoryType2Type1 | GetAgendaResponse200DataUndatedItemCategoryType3Type1 |
            None):
        country_code (None | str):
        city (None | str):
        lat (float | None):
        lng (float | None):
        tld (None | str):
    """

    id: str
    kind: GetAgendaResponse200DataUndatedItemKind
    title: str
    starts_on: datetime.date | None
    ends_on: datetime.date | None
    category: (
        GetAgendaResponse200DataUndatedItemCategoryType1
        | GetAgendaResponse200DataUndatedItemCategoryType2Type1
        | GetAgendaResponse200DataUndatedItemCategoryType3Type1
        | None
    )
    country_code: None | str
    city: None | str
    lat: float | None
    lng: float | None
    tld: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind: str = self.kind

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

        tld: None | str
        tld = self.tld

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "title": title,
                "startsOn": starts_on,
                "endsOn": ends_on,
                "category": category,
                "countryCode": country_code,
                "city": city,
                "lat": lat,
                "lng": lng,
                "tld": tld,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        kind = check_get_agenda_response_200_data_undated_item_kind(d.pop("kind"))

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
            GetAgendaResponse200DataUndatedItemCategoryType1
            | GetAgendaResponse200DataUndatedItemCategoryType2Type1
            | GetAgendaResponse200DataUndatedItemCategoryType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_1 = (
                    check_get_agenda_response_200_data_undated_item_category_type_1(
                        data
                    )
                )

                return category_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_2_type_1 = check_get_agenda_response_200_data_undated_item_category_type_2_type_1(
                    data
                )

                return category_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_3_type_1 = check_get_agenda_response_200_data_undated_item_category_type_3_type_1(
                    data
                )

                return category_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetAgendaResponse200DataUndatedItemCategoryType1
                | GetAgendaResponse200DataUndatedItemCategoryType2Type1
                | GetAgendaResponse200DataUndatedItemCategoryType3Type1
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

        def _parse_tld(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tld = _parse_tld(d.pop("tld"))

        get_agenda_response_200_data_undated_item = cls(
            id=id,
            kind=kind,
            title=title,
            starts_on=starts_on,
            ends_on=ends_on,
            category=category,
            country_code=country_code,
            city=city,
            lat=lat,
            lng=lng,
            tld=tld,
        )

        get_agenda_response_200_data_undated_item.additional_properties = d
        return get_agenda_response_200_data_undated_item

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
