from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_word_response_200_data_deny_class_type_1 import (
    GetWordResponse200DataDenyClassType1,
    check_get_word_response_200_data_deny_class_type_1,
)
from ..models.get_word_response_200_data_deny_class_type_2_type_1 import (
    GetWordResponse200DataDenyClassType2Type1,
    check_get_word_response_200_data_deny_class_type_2_type_1,
)
from ..models.get_word_response_200_data_deny_class_type_3_type_1 import (
    GetWordResponse200DataDenyClassType3Type1,
    check_get_word_response_200_data_deny_class_type_3_type_1,
)
from ..models.get_word_response_200_data_origin import (
    GetWordResponse200DataOrigin,
    check_get_word_response_200_data_origin,
)
from ..models.get_word_response_200_data_shape_type_1 import (
    GetWordResponse200DataShapeType1,
    check_get_word_response_200_data_shape_type_1,
)
from ..models.get_word_response_200_data_shape_type_2_type_1 import (
    GetWordResponse200DataShapeType2Type1,
    check_get_word_response_200_data_shape_type_2_type_1,
)
from ..models.get_word_response_200_data_shape_type_3_type_1 import (
    GetWordResponse200DataShapeType3Type1,
    check_get_word_response_200_data_shape_type_3_type_1,
)
from ..models.get_word_response_200_data_style_type_1 import (
    GetWordResponse200DataStyleType1,
    check_get_word_response_200_data_style_type_1,
)
from ..models.get_word_response_200_data_style_type_2_type_1 import (
    GetWordResponse200DataStyleType2Type1,
    check_get_word_response_200_data_style_type_2_type_1,
)
from ..models.get_word_response_200_data_style_type_3_type_1 import (
    GetWordResponse200DataStyleType3Type1,
    check_get_word_response_200_data_style_type_3_type_1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_word_response_200_data_categories_item import (
        GetWordResponse200DataCategoriesItem,
    )
    from ..models.get_word_response_200_data_linguistics import (
        GetWordResponse200DataLinguistics,
    )


T = TypeVar("T", bound="GetWordResponse200Data")


@_attrs_define
class GetWordResponse200Data:
    """
    Attributes:
        id (str): `wrd_<id>`.
        word (str):
        categories (list[GetWordResponse200DataCategoriesItem]):
        origin (GetWordResponse200DataOrigin):
        linguistics (GetWordResponse200DataLinguistics):
        slug (None | str | Unset):
        shape (GetWordResponse200DataShapeType1 | GetWordResponse200DataShapeType2Type1 |
            GetWordResponse200DataShapeType3Type1 | None | Unset):
        pos (None | str | Unset): Parts of speech as stored, comma-joined tags.
        definition (None | str | Unset):
        inflected (bool | None | Unset):
        size (int | None | Unset):
        popularity (int | None | Unset): How widely the word is used; never sales or demand.
        sentiment (int | None | Unset): 50 is neutral.
        brandability (int | None | Unset):
        style (GetWordResponse200DataStyleType1 | GetWordResponse200DataStyleType2Type1 |
            GetWordResponse200DataStyleType3Type1 | None | Unset):
        deny_class (GetWordResponse200DataDenyClassType1 | GetWordResponse200DataDenyClassType2Type1 |
            GetWordResponse200DataDenyClassType3Type1 | None | Unset): Why the word stays off public lists (ADR-0111); null
            when none.
        added_at (datetime.datetime | None | Unset): When the intake added it; null means the dictionary load.
    """

    id: str
    word: str
    categories: list[GetWordResponse200DataCategoriesItem]
    origin: GetWordResponse200DataOrigin
    linguistics: GetWordResponse200DataLinguistics
    slug: None | str | Unset = UNSET
    shape: (
        GetWordResponse200DataShapeType1
        | GetWordResponse200DataShapeType2Type1
        | GetWordResponse200DataShapeType3Type1
        | None
        | Unset
    ) = UNSET
    pos: None | str | Unset = UNSET
    definition: None | str | Unset = UNSET
    inflected: bool | None | Unset = UNSET
    size: int | None | Unset = UNSET
    popularity: int | None | Unset = UNSET
    sentiment: int | None | Unset = UNSET
    brandability: int | None | Unset = UNSET
    style: (
        GetWordResponse200DataStyleType1
        | GetWordResponse200DataStyleType2Type1
        | GetWordResponse200DataStyleType3Type1
        | None
        | Unset
    ) = UNSET
    deny_class: (
        GetWordResponse200DataDenyClassType1
        | GetWordResponse200DataDenyClassType2Type1
        | GetWordResponse200DataDenyClassType3Type1
        | None
        | Unset
    ) = UNSET
    added_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        word = self.word

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        origin: str = self.origin

        linguistics = self.linguistics.to_dict()

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        shape: None | str | Unset
        if isinstance(self.shape, Unset):
            shape = UNSET
        elif (
            isinstance(self.shape, str)
            or isinstance(self.shape, str)
            or isinstance(self.shape, str)
        ):
            shape = self.shape
        else:
            shape = self.shape

        pos: None | str | Unset
        if isinstance(self.pos, Unset):
            pos = UNSET
        else:
            pos = self.pos

        definition: None | str | Unset
        if isinstance(self.definition, Unset):
            definition = UNSET
        else:
            definition = self.definition

        inflected: bool | None | Unset
        if isinstance(self.inflected, Unset):
            inflected = UNSET
        else:
            inflected = self.inflected

        size: int | None | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        popularity: int | None | Unset
        if isinstance(self.popularity, Unset):
            popularity = UNSET
        else:
            popularity = self.popularity

        sentiment: int | None | Unset
        if isinstance(self.sentiment, Unset):
            sentiment = UNSET
        else:
            sentiment = self.sentiment

        brandability: int | None | Unset
        if isinstance(self.brandability, Unset):
            brandability = UNSET
        else:
            brandability = self.brandability

        style: None | str | Unset
        if isinstance(self.style, Unset):
            style = UNSET
        elif (
            isinstance(self.style, str)
            or isinstance(self.style, str)
            or isinstance(self.style, str)
        ):
            style = self.style
        else:
            style = self.style

        deny_class: None | str | Unset
        if isinstance(self.deny_class, Unset):
            deny_class = UNSET
        elif (
            isinstance(self.deny_class, str)
            or isinstance(self.deny_class, str)
            or isinstance(self.deny_class, str)
        ):
            deny_class = self.deny_class
        else:
            deny_class = self.deny_class

        added_at: None | str | Unset
        if isinstance(self.added_at, Unset):
            added_at = UNSET
        elif isinstance(self.added_at, datetime.datetime):
            added_at = self.added_at.isoformat()
        else:
            added_at = self.added_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "word": word,
                "categories": categories,
                "origin": origin,
                "linguistics": linguistics,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if shape is not UNSET:
            field_dict["shape"] = shape
        if pos is not UNSET:
            field_dict["pos"] = pos
        if definition is not UNSET:
            field_dict["definition"] = definition
        if inflected is not UNSET:
            field_dict["inflected"] = inflected
        if size is not UNSET:
            field_dict["size"] = size
        if popularity is not UNSET:
            field_dict["popularity"] = popularity
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment
        if brandability is not UNSET:
            field_dict["brandability"] = brandability
        if style is not UNSET:
            field_dict["style"] = style
        if deny_class is not UNSET:
            field_dict["denyClass"] = deny_class
        if added_at is not UNSET:
            field_dict["addedAt"] = added_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_word_response_200_data_categories_item import (
            GetWordResponse200DataCategoriesItem,
        )
        from ..models.get_word_response_200_data_linguistics import (
            GetWordResponse200DataLinguistics,
        )

        d = dict(src_dict)
        id = d.pop("id")

        word = d.pop("word")

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = GetWordResponse200DataCategoriesItem.from_dict(
                categories_item_data
            )

            categories.append(categories_item)

        origin = check_get_word_response_200_data_origin(d.pop("origin"))

        linguistics = GetWordResponse200DataLinguistics.from_dict(d.pop("linguistics"))

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_shape(
            data: object,
        ) -> (
            GetWordResponse200DataShapeType1
            | GetWordResponse200DataShapeType2Type1
            | GetWordResponse200DataShapeType3Type1
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
                shape_type_1 = check_get_word_response_200_data_shape_type_1(data)

                return shape_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_2_type_1 = (
                    check_get_word_response_200_data_shape_type_2_type_1(data)
                )

                return shape_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_3_type_1 = (
                    check_get_word_response_200_data_shape_type_3_type_1(data)
                )

                return shape_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetWordResponse200DataShapeType1
                | GetWordResponse200DataShapeType2Type1
                | GetWordResponse200DataShapeType3Type1
                | None
                | Unset,
                data,
            )

        shape = _parse_shape(d.pop("shape", UNSET))

        def _parse_pos(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pos = _parse_pos(d.pop("pos", UNSET))

        def _parse_definition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        definition = _parse_definition(d.pop("definition", UNSET))

        def _parse_inflected(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        inflected = _parse_inflected(d.pop("inflected", UNSET))

        def _parse_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_popularity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        popularity = _parse_popularity(d.pop("popularity", UNSET))

        def _parse_sentiment(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sentiment = _parse_sentiment(d.pop("sentiment", UNSET))

        def _parse_brandability(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        brandability = _parse_brandability(d.pop("brandability", UNSET))

        def _parse_style(
            data: object,
        ) -> (
            GetWordResponse200DataStyleType1
            | GetWordResponse200DataStyleType2Type1
            | GetWordResponse200DataStyleType3Type1
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
                style_type_1 = check_get_word_response_200_data_style_type_1(data)

                return style_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                style_type_2_type_1 = (
                    check_get_word_response_200_data_style_type_2_type_1(data)
                )

                return style_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                style_type_3_type_1 = (
                    check_get_word_response_200_data_style_type_3_type_1(data)
                )

                return style_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetWordResponse200DataStyleType1
                | GetWordResponse200DataStyleType2Type1
                | GetWordResponse200DataStyleType3Type1
                | None
                | Unset,
                data,
            )

        style = _parse_style(d.pop("style", UNSET))

        def _parse_deny_class(
            data: object,
        ) -> (
            GetWordResponse200DataDenyClassType1
            | GetWordResponse200DataDenyClassType2Type1
            | GetWordResponse200DataDenyClassType3Type1
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
                deny_class_type_1 = check_get_word_response_200_data_deny_class_type_1(
                    data
                )

                return deny_class_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deny_class_type_2_type_1 = (
                    check_get_word_response_200_data_deny_class_type_2_type_1(data)
                )

                return deny_class_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deny_class_type_3_type_1 = (
                    check_get_word_response_200_data_deny_class_type_3_type_1(data)
                )

                return deny_class_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetWordResponse200DataDenyClassType1
                | GetWordResponse200DataDenyClassType2Type1
                | GetWordResponse200DataDenyClassType3Type1
                | None
                | Unset,
                data,
            )

        deny_class = _parse_deny_class(d.pop("denyClass", UNSET))

        def _parse_added_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                added_at_type_0 = datetime.datetime.fromisoformat(data)

                return added_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        added_at = _parse_added_at(d.pop("addedAt", UNSET))

        get_word_response_200_data = cls(
            id=id,
            word=word,
            categories=categories,
            origin=origin,
            linguistics=linguistics,
            slug=slug,
            shape=shape,
            pos=pos,
            definition=definition,
            inflected=inflected,
            size=size,
            popularity=popularity,
            sentiment=sentiment,
            brandability=brandability,
            style=style,
            deny_class=deny_class,
            added_at=added_at,
        )

        get_word_response_200_data.additional_properties = d
        return get_word_response_200_data

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
