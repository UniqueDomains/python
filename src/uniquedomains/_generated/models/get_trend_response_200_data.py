from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_trend_response_200_data_lane_type_1 import (
    GetTrendResponse200DataLaneType1,
    check_get_trend_response_200_data_lane_type_1,
)
from ..models.get_trend_response_200_data_lane_type_2_type_1 import (
    GetTrendResponse200DataLaneType2Type1,
    check_get_trend_response_200_data_lane_type_2_type_1,
)
from ..models.get_trend_response_200_data_lane_type_3_type_1 import (
    GetTrendResponse200DataLaneType3Type1,
    check_get_trend_response_200_data_lane_type_3_type_1,
)

if TYPE_CHECKING:
    from ..models.get_trend_response_200_data_editions_item import (
        GetTrendResponse200DataEditionsItem,
    )
    from ..models.get_trend_response_200_data_observations_item import (
        GetTrendResponse200DataObservationsItem,
    )


T = TypeVar("T", bound="GetTrendResponse200Data")


@_attrs_define
class GetTrendResponse200Data:
    """
    Attributes:
        slug (str):
        name (str):
        category (None | str):
        definition (None | str):
        volume (int | None): Monthly searches at the latest edition.
        growth (int | None): Signed whole percentage at the latest edition.
        lane (GetTrendResponse200DataLaneType1 | GetTrendResponse200DataLaneType2Type1 |
            GetTrendResponse200DataLaneType3Type1 | None):
        head_word (None | str):
        why_now (None | str):
        first_edition_on (datetime.date):
        last_edition_on (datetime.date):
        edition_count (int):
        head_words (list[str]):
        editions (list[GetTrendResponse200DataEditionsItem]):
        observations (list[GetTrendResponse200DataObservationsItem]):
    """

    slug: str
    name: str
    category: None | str
    definition: None | str
    volume: int | None
    growth: int | None
    lane: (
        GetTrendResponse200DataLaneType1
        | GetTrendResponse200DataLaneType2Type1
        | GetTrendResponse200DataLaneType3Type1
        | None
    )
    head_word: None | str
    why_now: None | str
    first_edition_on: datetime.date
    last_edition_on: datetime.date
    edition_count: int
    head_words: list[str]
    editions: list[GetTrendResponse200DataEditionsItem]
    observations: list[GetTrendResponse200DataObservationsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        category: None | str
        category = self.category

        definition: None | str
        definition = self.definition

        volume: int | None
        volume = self.volume

        growth: int | None
        growth = self.growth

        lane: None | str
        if (
            isinstance(self.lane, str)
            or isinstance(self.lane, str)
            or isinstance(self.lane, str)
        ):
            lane = self.lane
        else:
            lane = self.lane

        head_word: None | str
        head_word = self.head_word

        why_now: None | str
        why_now = self.why_now

        first_edition_on = self.first_edition_on.isoformat()

        last_edition_on = self.last_edition_on.isoformat()

        edition_count = self.edition_count

        head_words = self.head_words

        editions = []
        for editions_item_data in self.editions:
            editions_item = editions_item_data.to_dict()
            editions.append(editions_item)

        observations = []
        for observations_item_data in self.observations:
            observations_item = observations_item_data.to_dict()
            observations.append(observations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "name": name,
                "category": category,
                "definition": definition,
                "volume": volume,
                "growth": growth,
                "lane": lane,
                "headWord": head_word,
                "whyNow": why_now,
                "firstEditionOn": first_edition_on,
                "lastEditionOn": last_edition_on,
                "editionCount": edition_count,
                "headWords": head_words,
                "editions": editions,
                "observations": observations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_trend_response_200_data_editions_item import (
            GetTrendResponse200DataEditionsItem,
        )
        from ..models.get_trend_response_200_data_observations_item import (
            GetTrendResponse200DataObservationsItem,
        )

        d = dict(src_dict)
        slug = d.pop("slug")

        name = d.pop("name")

        def _parse_category(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        category = _parse_category(d.pop("category"))

        def _parse_definition(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        definition = _parse_definition(d.pop("definition"))

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

        def _parse_lane(
            data: object,
        ) -> (
            GetTrendResponse200DataLaneType1
            | GetTrendResponse200DataLaneType2Type1
            | GetTrendResponse200DataLaneType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lane_type_1 = check_get_trend_response_200_data_lane_type_1(data)

                return lane_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lane_type_2_type_1 = (
                    check_get_trend_response_200_data_lane_type_2_type_1(data)
                )

                return lane_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lane_type_3_type_1 = (
                    check_get_trend_response_200_data_lane_type_3_type_1(data)
                )

                return lane_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetTrendResponse200DataLaneType1
                | GetTrendResponse200DataLaneType2Type1
                | GetTrendResponse200DataLaneType3Type1
                | None,
                data,
            )

        lane = _parse_lane(d.pop("lane"))

        def _parse_head_word(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        head_word = _parse_head_word(d.pop("headWord"))

        def _parse_why_now(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        why_now = _parse_why_now(d.pop("whyNow"))

        first_edition_on = datetime.date.fromisoformat(d.pop("firstEditionOn"))

        last_edition_on = datetime.date.fromisoformat(d.pop("lastEditionOn"))

        edition_count = d.pop("editionCount")

        head_words = cast(list[str], d.pop("headWords"))

        editions = []
        _editions = d.pop("editions")
        for editions_item_data in _editions:
            editions_item = GetTrendResponse200DataEditionsItem.from_dict(
                editions_item_data
            )

            editions.append(editions_item)

        observations = []
        _observations = d.pop("observations")
        for observations_item_data in _observations:
            observations_item = GetTrendResponse200DataObservationsItem.from_dict(
                observations_item_data
            )

            observations.append(observations_item)

        get_trend_response_200_data = cls(
            slug=slug,
            name=name,
            category=category,
            definition=definition,
            volume=volume,
            growth=growth,
            lane=lane,
            head_word=head_word,
            why_now=why_now,
            first_edition_on=first_edition_on,
            last_edition_on=last_edition_on,
            edition_count=edition_count,
            head_words=head_words,
            editions=editions,
            observations=observations,
        )

        get_trend_response_200_data.additional_properties = d
        return get_trend_response_200_data

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
