from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_catalog_stats_response_200_data_domains import (
        GetCatalogStatsResponse200DataDomains,
    )


T = TypeVar("T", bound="GetCatalogStatsResponse200Data")


@_attrs_define
class GetCatalogStatsResponse200Data:
    """
    Attributes:
        day (datetime.date | Unset):
        domains (GetCatalogStatsResponse200DataDomains | Unset):
        words (int | None | Unset):
        tlds (int | Unset):
    """

    day: datetime.date | Unset = UNSET
    domains: GetCatalogStatsResponse200DataDomains | Unset = UNSET
    words: int | None | Unset = UNSET
    tlds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day: str | Unset = UNSET
        if not isinstance(self.day, Unset):
            day = self.day.isoformat()

        domains: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domains, Unset):
            domains = self.domains.to_dict()

        words: int | None | Unset
        if isinstance(self.words, Unset):
            words = UNSET
        else:
            words = self.words

        tlds = self.tlds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["day"] = day
        if domains is not UNSET:
            field_dict["domains"] = domains
        if words is not UNSET:
            field_dict["words"] = words
        if tlds is not UNSET:
            field_dict["tlds"] = tlds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_catalog_stats_response_200_data_domains import (
            GetCatalogStatsResponse200DataDomains,
        )

        d = dict(src_dict)
        _day = d.pop("day", UNSET)
        day: datetime.date | Unset
        if isinstance(_day, Unset):
            day = UNSET
        else:
            day = datetime.date.fromisoformat(_day)

        _domains = d.pop("domains", UNSET)
        domains: GetCatalogStatsResponse200DataDomains | Unset
        if isinstance(_domains, Unset):
            domains = UNSET
        else:
            domains = GetCatalogStatsResponse200DataDomains.from_dict(_domains)

        def _parse_words(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        words = _parse_words(d.pop("words", UNSET))

        tlds = d.pop("tlds", UNSET)

        get_catalog_stats_response_200_data = cls(
            day=day,
            domains=domains,
            words=words,
            tlds=tlds,
        )

        get_catalog_stats_response_200_data.additional_properties = d
        return get_catalog_stats_response_200_data

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
