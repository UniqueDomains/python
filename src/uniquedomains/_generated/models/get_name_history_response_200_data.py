from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNameHistoryResponse200Data")


@_attrs_define
class GetNameHistoryResponse200Data:
    """
    Attributes:
        had_website (bool | None | Unset):
        first_capture_year (int | None | Unset):
        last_capture_year (int | None | Unset):
        captures (int | None | Unset):
        authority_band (None | str | Unset):
        language (None | str | Unset):
    """

    had_website: bool | None | Unset = UNSET
    first_capture_year: int | None | Unset = UNSET
    last_capture_year: int | None | Unset = UNSET
    captures: int | None | Unset = UNSET
    authority_band: None | str | Unset = UNSET
    language: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        had_website: bool | None | Unset
        if isinstance(self.had_website, Unset):
            had_website = UNSET
        else:
            had_website = self.had_website

        first_capture_year: int | None | Unset
        if isinstance(self.first_capture_year, Unset):
            first_capture_year = UNSET
        else:
            first_capture_year = self.first_capture_year

        last_capture_year: int | None | Unset
        if isinstance(self.last_capture_year, Unset):
            last_capture_year = UNSET
        else:
            last_capture_year = self.last_capture_year

        captures: int | None | Unset
        if isinstance(self.captures, Unset):
            captures = UNSET
        else:
            captures = self.captures

        authority_band: None | str | Unset
        if isinstance(self.authority_band, Unset):
            authority_band = UNSET
        else:
            authority_band = self.authority_band

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if had_website is not UNSET:
            field_dict["hadWebsite"] = had_website
        if first_capture_year is not UNSET:
            field_dict["firstCaptureYear"] = first_capture_year
        if last_capture_year is not UNSET:
            field_dict["lastCaptureYear"] = last_capture_year
        if captures is not UNSET:
            field_dict["captures"] = captures
        if authority_band is not UNSET:
            field_dict["authorityBand"] = authority_band
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_had_website(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        had_website = _parse_had_website(d.pop("hadWebsite", UNSET))

        def _parse_first_capture_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        first_capture_year = _parse_first_capture_year(d.pop("firstCaptureYear", UNSET))

        def _parse_last_capture_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_capture_year = _parse_last_capture_year(d.pop("lastCaptureYear", UNSET))

        def _parse_captures(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        captures = _parse_captures(d.pop("captures", UNSET))

        def _parse_authority_band(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authority_band = _parse_authority_band(d.pop("authorityBand", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        get_name_history_response_200_data = cls(
            had_website=had_website,
            first_capture_year=first_capture_year,
            last_capture_year=last_capture_year,
            captures=captures,
            authority_band=authority_band,
            language=language,
        )

        get_name_history_response_200_data.additional_properties = d
        return get_name_history_response_200_data

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
