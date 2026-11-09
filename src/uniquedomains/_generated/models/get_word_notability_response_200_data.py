from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWordNotabilityResponse200Data")


@_attrs_define
class GetWordNotabilityResponse200Data:
    """
    Attributes:
        wikipedia_title (None | str | Unset):
        backlinks (int | None | Unset):
        languages (int | None | Unset):
        wikidata_id (None | str | Unset):
        description (None | str | Unset):
    """

    wikipedia_title: None | str | Unset = UNSET
    backlinks: int | None | Unset = UNSET
    languages: int | None | Unset = UNSET
    wikidata_id: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wikipedia_title: None | str | Unset
        if isinstance(self.wikipedia_title, Unset):
            wikipedia_title = UNSET
        else:
            wikipedia_title = self.wikipedia_title

        backlinks: int | None | Unset
        if isinstance(self.backlinks, Unset):
            backlinks = UNSET
        else:
            backlinks = self.backlinks

        languages: int | None | Unset
        if isinstance(self.languages, Unset):
            languages = UNSET
        else:
            languages = self.languages

        wikidata_id: None | str | Unset
        if isinstance(self.wikidata_id, Unset):
            wikidata_id = UNSET
        else:
            wikidata_id = self.wikidata_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wikipedia_title is not UNSET:
            field_dict["wikipediaTitle"] = wikipedia_title
        if backlinks is not UNSET:
            field_dict["backlinks"] = backlinks
        if languages is not UNSET:
            field_dict["languages"] = languages
        if wikidata_id is not UNSET:
            field_dict["wikidataId"] = wikidata_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_wikipedia_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wikipedia_title = _parse_wikipedia_title(d.pop("wikipediaTitle", UNSET))

        def _parse_backlinks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backlinks = _parse_backlinks(d.pop("backlinks", UNSET))

        def _parse_languages(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        languages = _parse_languages(d.pop("languages", UNSET))

        def _parse_wikidata_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wikidata_id = _parse_wikidata_id(d.pop("wikidataId", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        get_word_notability_response_200_data = cls(
            wikipedia_title=wikipedia_title,
            backlinks=backlinks,
            languages=languages,
            wikidata_id=wikidata_id,
            description=description,
        )

        get_word_notability_response_200_data.additional_properties = d
        return get_word_notability_response_200_data

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
