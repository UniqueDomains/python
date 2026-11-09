from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_edition_response_200_data_trends_item_lane_type_1 import (
    GetEditionResponse200DataTrendsItemLaneType1,
    check_get_edition_response_200_data_trends_item_lane_type_1,
)
from ..models.get_edition_response_200_data_trends_item_lane_type_2_type_1 import (
    GetEditionResponse200DataTrendsItemLaneType2Type1,
    check_get_edition_response_200_data_trends_item_lane_type_2_type_1,
)
from ..models.get_edition_response_200_data_trends_item_lane_type_3_type_1 import (
    GetEditionResponse200DataTrendsItemLaneType3Type1,
    check_get_edition_response_200_data_trends_item_lane_type_3_type_1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_edition_response_200_data_trends_item_rows_item import (
        GetEditionResponse200DataTrendsItemRowsItem,
    )


T = TypeVar("T", bound="GetEditionResponse200DataTrendsItem")


@_attrs_define
class GetEditionResponse200DataTrendsItem:
    """
    Attributes:
        slug (str | Unset):
        name (str | Unset):
        category (None | str | Unset):
        definition (None | str | Unset):
        volume (int | None | Unset): Searches a month.
        growth (float | None | Unset): Growth, percent.
        lane (GetEditionResponse200DataTrendsItemLaneType1 | GetEditionResponse200DataTrendsItemLaneType2Type1 |
            GetEditionResponse200DataTrendsItemLaneType3Type1 | None | Unset):
        head_word (None | str | Unset):
        why_now (None | str | Unset):
        open_names (int | None | Unset):
        locked_count (int | Unset): Names this audience cannot open, a count.
        rows (list[GetEditionResponse200DataTrendsItemRowsItem] | Unset):
    """

    slug: str | Unset = UNSET
    name: str | Unset = UNSET
    category: None | str | Unset = UNSET
    definition: None | str | Unset = UNSET
    volume: int | None | Unset = UNSET
    growth: float | None | Unset = UNSET
    lane: (
        GetEditionResponse200DataTrendsItemLaneType1
        | GetEditionResponse200DataTrendsItemLaneType2Type1
        | GetEditionResponse200DataTrendsItemLaneType3Type1
        | None
        | Unset
    ) = UNSET
    head_word: None | str | Unset = UNSET
    why_now: None | str | Unset = UNSET
    open_names: int | None | Unset = UNSET
    locked_count: int | Unset = UNSET
    rows: list[GetEditionResponse200DataTrendsItemRowsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        definition: None | str | Unset
        if isinstance(self.definition, Unset):
            definition = UNSET
        else:
            definition = self.definition

        volume: int | None | Unset
        if isinstance(self.volume, Unset):
            volume = UNSET
        else:
            volume = self.volume

        growth: float | None | Unset
        if isinstance(self.growth, Unset):
            growth = UNSET
        else:
            growth = self.growth

        lane: None | str | Unset
        if isinstance(self.lane, Unset):
            lane = UNSET
        elif (
            isinstance(self.lane, str)
            or isinstance(self.lane, str)
            or isinstance(self.lane, str)
        ):
            lane = self.lane
        else:
            lane = self.lane

        head_word: None | str | Unset
        if isinstance(self.head_word, Unset):
            head_word = UNSET
        else:
            head_word = self.head_word

        why_now: None | str | Unset
        if isinstance(self.why_now, Unset):
            why_now = UNSET
        else:
            why_now = self.why_now

        open_names: int | None | Unset
        if isinstance(self.open_names, Unset):
            open_names = UNSET
        else:
            open_names = self.open_names

        locked_count = self.locked_count

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if definition is not UNSET:
            field_dict["definition"] = definition
        if volume is not UNSET:
            field_dict["volume"] = volume
        if growth is not UNSET:
            field_dict["growth"] = growth
        if lane is not UNSET:
            field_dict["lane"] = lane
        if head_word is not UNSET:
            field_dict["headWord"] = head_word
        if why_now is not UNSET:
            field_dict["whyNow"] = why_now
        if open_names is not UNSET:
            field_dict["openNames"] = open_names
        if locked_count is not UNSET:
            field_dict["lockedCount"] = locked_count
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_edition_response_200_data_trends_item_rows_item import (
            GetEditionResponse200DataTrendsItemRowsItem,
        )

        d = dict(src_dict)
        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_definition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        definition = _parse_definition(d.pop("definition", UNSET))

        def _parse_volume(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume = _parse_volume(d.pop("volume", UNSET))

        def _parse_growth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        growth = _parse_growth(d.pop("growth", UNSET))

        def _parse_lane(
            data: object,
        ) -> (
            GetEditionResponse200DataTrendsItemLaneType1
            | GetEditionResponse200DataTrendsItemLaneType2Type1
            | GetEditionResponse200DataTrendsItemLaneType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lane_type_1 = (
                    check_get_edition_response_200_data_trends_item_lane_type_1(data)
                )

                return lane_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lane_type_2_type_1 = (
                    check_get_edition_response_200_data_trends_item_lane_type_2_type_1(
                        data
                    )
                )

                return lane_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lane_type_3_type_1 = (
                    check_get_edition_response_200_data_trends_item_lane_type_3_type_1(
                        data
                    )
                )

                return lane_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetEditionResponse200DataTrendsItemLaneType1
                | GetEditionResponse200DataTrendsItemLaneType2Type1
                | GetEditionResponse200DataTrendsItemLaneType3Type1
                | None
                | Unset,
                data,
            )

        lane = _parse_lane(d.pop("lane", UNSET))

        def _parse_head_word(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        head_word = _parse_head_word(d.pop("headWord", UNSET))

        def _parse_why_now(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        why_now = _parse_why_now(d.pop("whyNow", UNSET))

        def _parse_open_names(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        open_names = _parse_open_names(d.pop("openNames", UNSET))

        locked_count = d.pop("lockedCount", UNSET)

        _rows = d.pop("rows", UNSET)
        rows: list[GetEditionResponse200DataTrendsItemRowsItem] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = GetEditionResponse200DataTrendsItemRowsItem.from_dict(
                    rows_item_data
                )

                rows.append(rows_item)

        get_edition_response_200_data_trends_item = cls(
            slug=slug,
            name=name,
            category=category,
            definition=definition,
            volume=volume,
            growth=growth,
            lane=lane,
            head_word=head_word,
            why_now=why_now,
            open_names=open_names,
            locked_count=locked_count,
            rows=rows,
        )

        get_edition_response_200_data_trends_item.additional_properties = d
        return get_edition_response_200_data_trends_item

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
