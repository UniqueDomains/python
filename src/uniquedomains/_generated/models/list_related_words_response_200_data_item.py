from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_related_words_response_200_data_item_relation import (
    ListRelatedWordsResponse200DataItemRelation,
    check_list_related_words_response_200_data_item_relation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListRelatedWordsResponse200DataItem")


@_attrs_define
class ListRelatedWordsResponse200DataItem:
    """
    Attributes:
        word (str | Unset):
        slug (None | str | Unset):
        relation (ListRelatedWordsResponse200DataItemRelation | Unset):
        open_names (int | None | Unset): Open to register plus for sale; null: not counted yet.
    """

    word: str | Unset = UNSET
    slug: None | str | Unset = UNSET
    relation: ListRelatedWordsResponse200DataItemRelation | Unset = UNSET
    open_names: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        word = self.word

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        relation: str | Unset = UNSET
        if not isinstance(self.relation, Unset):
            relation = self.relation

        open_names: int | None | Unset
        if isinstance(self.open_names, Unset):
            open_names = UNSET
        else:
            open_names = self.open_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if word is not UNSET:
            field_dict["word"] = word
        if slug is not UNSET:
            field_dict["slug"] = slug
        if relation is not UNSET:
            field_dict["relation"] = relation
        if open_names is not UNSET:
            field_dict["openNames"] = open_names

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        word = d.pop("word", UNSET)

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        _relation = d.pop("relation", UNSET)
        relation: ListRelatedWordsResponse200DataItemRelation | Unset
        if isinstance(_relation, Unset):
            relation = UNSET
        else:
            relation = check_list_related_words_response_200_data_item_relation(
                _relation
            )

        def _parse_open_names(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        open_names = _parse_open_names(d.pop("openNames", UNSET))

        list_related_words_response_200_data_item = cls(
            word=word,
            slug=slug,
            relation=relation,
            open_names=open_names,
        )

        list_related_words_response_200_data_item.additional_properties = d
        return list_related_words_response_200_data_item

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
