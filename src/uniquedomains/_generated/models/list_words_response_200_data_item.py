from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_words_response_200_data_item_origin import (
    ListWordsResponse200DataItemOrigin,
    check_list_words_response_200_data_item_origin,
)
from ..models.list_words_response_200_data_item_shape_type_1 import (
    ListWordsResponse200DataItemShapeType1,
    check_list_words_response_200_data_item_shape_type_1,
)
from ..models.list_words_response_200_data_item_shape_type_2_type_1 import (
    ListWordsResponse200DataItemShapeType2Type1,
    check_list_words_response_200_data_item_shape_type_2_type_1,
)
from ..models.list_words_response_200_data_item_shape_type_3_type_1 import (
    ListWordsResponse200DataItemShapeType3Type1,
    check_list_words_response_200_data_item_shape_type_3_type_1,
)

T = TypeVar("T", bound="ListWordsResponse200DataItem")


@_attrs_define
class ListWordsResponse200DataItem:
    """
    Attributes:
        id (str):
        slug (None | str):
        word (str):
        shape (ListWordsResponse200DataItemShapeType1 | ListWordsResponse200DataItemShapeType2Type1 |
            ListWordsResponse200DataItemShapeType3Type1 | None):
        pos (None | str):
        size (int | None):
        origin (ListWordsResponse200DataItemOrigin):
    """

    id: str
    slug: None | str
    word: str
    shape: (
        ListWordsResponse200DataItemShapeType1
        | ListWordsResponse200DataItemShapeType2Type1
        | ListWordsResponse200DataItemShapeType3Type1
        | None
    )
    pos: None | str
    size: int | None
    origin: ListWordsResponse200DataItemOrigin
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug: None | str
        slug = self.slug

        word = self.word

        shape: None | str
        if (
            isinstance(self.shape, str)
            or isinstance(self.shape, str)
            or isinstance(self.shape, str)
        ):
            shape = self.shape
        else:
            shape = self.shape

        pos: None | str
        pos = self.pos

        size: int | None
        size = self.size

        origin: str = self.origin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "word": word,
                "shape": shape,
                "pos": pos,
                "size": size,
                "origin": origin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        word = d.pop("word")

        def _parse_shape(
            data: object,
        ) -> (
            ListWordsResponse200DataItemShapeType1
            | ListWordsResponse200DataItemShapeType2Type1
            | ListWordsResponse200DataItemShapeType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_1 = check_list_words_response_200_data_item_shape_type_1(
                    data
                )

                return shape_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_2_type_1 = (
                    check_list_words_response_200_data_item_shape_type_2_type_1(data)
                )

                return shape_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_3_type_1 = (
                    check_list_words_response_200_data_item_shape_type_3_type_1(data)
                )

                return shape_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListWordsResponse200DataItemShapeType1
                | ListWordsResponse200DataItemShapeType2Type1
                | ListWordsResponse200DataItemShapeType3Type1
                | None,
                data,
            )

        shape = _parse_shape(d.pop("shape"))

        def _parse_pos(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pos = _parse_pos(d.pop("pos"))

        def _parse_size(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        size = _parse_size(d.pop("size"))

        origin = check_list_words_response_200_data_item_origin(d.pop("origin"))

        list_words_response_200_data_item = cls(
            id=id,
            slug=slug,
            word=word,
            shape=shape,
            pos=pos,
            size=size,
            origin=origin,
        )

        list_words_response_200_data_item.additional_properties = d
        return list_words_response_200_data_item

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
