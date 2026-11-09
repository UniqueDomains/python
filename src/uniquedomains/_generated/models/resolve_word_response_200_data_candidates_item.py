from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resolve_word_response_200_data_candidates_item_origin import (
    ResolveWordResponse200DataCandidatesItemOrigin,
    check_resolve_word_response_200_data_candidates_item_origin,
)
from ..models.resolve_word_response_200_data_candidates_item_shape_type_1 import (
    ResolveWordResponse200DataCandidatesItemShapeType1,
    check_resolve_word_response_200_data_candidates_item_shape_type_1,
)
from ..models.resolve_word_response_200_data_candidates_item_shape_type_2_type_1 import (
    ResolveWordResponse200DataCandidatesItemShapeType2Type1,
    check_resolve_word_response_200_data_candidates_item_shape_type_2_type_1,
)
from ..models.resolve_word_response_200_data_candidates_item_shape_type_3_type_1 import (
    ResolveWordResponse200DataCandidatesItemShapeType3Type1,
    check_resolve_word_response_200_data_candidates_item_shape_type_3_type_1,
)

T = TypeVar("T", bound="ResolveWordResponse200DataCandidatesItem")


@_attrs_define
class ResolveWordResponse200DataCandidatesItem:
    """
    Attributes:
        id (str): `wrd_<id>`.
        slug (None | str):
        word (str):
        shape (None | ResolveWordResponse200DataCandidatesItemShapeType1 |
            ResolveWordResponse200DataCandidatesItemShapeType2Type1 |
            ResolveWordResponse200DataCandidatesItemShapeType3Type1):
        origin (ResolveWordResponse200DataCandidatesItemOrigin):
    """

    id: str
    slug: None | str
    word: str
    shape: (
        None
        | ResolveWordResponse200DataCandidatesItemShapeType1
        | ResolveWordResponse200DataCandidatesItemShapeType2Type1
        | ResolveWordResponse200DataCandidatesItemShapeType3Type1
    )
    origin: ResolveWordResponse200DataCandidatesItemOrigin
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

        origin: str = self.origin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "word": word,
                "shape": shape,
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
            None
            | ResolveWordResponse200DataCandidatesItemShapeType1
            | ResolveWordResponse200DataCandidatesItemShapeType2Type1
            | ResolveWordResponse200DataCandidatesItemShapeType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_1 = (
                    check_resolve_word_response_200_data_candidates_item_shape_type_1(
                        data
                    )
                )

                return shape_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_2_type_1 = check_resolve_word_response_200_data_candidates_item_shape_type_2_type_1(
                    data
                )

                return shape_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_3_type_1 = check_resolve_word_response_200_data_candidates_item_shape_type_3_type_1(
                    data
                )

                return shape_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | ResolveWordResponse200DataCandidatesItemShapeType1
                | ResolveWordResponse200DataCandidatesItemShapeType2Type1
                | ResolveWordResponse200DataCandidatesItemShapeType3Type1,
                data,
            )

        shape = _parse_shape(d.pop("shape"))

        origin = check_resolve_word_response_200_data_candidates_item_origin(
            d.pop("origin")
        )

        resolve_word_response_200_data_candidates_item = cls(
            id=id,
            slug=slug,
            word=word,
            shape=shape,
            origin=origin,
        )

        resolve_word_response_200_data_candidates_item.additional_properties = d
        return resolve_word_response_200_data_candidates_item

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
