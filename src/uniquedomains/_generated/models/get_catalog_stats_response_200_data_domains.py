from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCatalogStatsResponse200DataDomains")


@_attrs_define
class GetCatalogStatsResponse200DataDomains:
    """
    Attributes:
        total (int | Unset):
        available (int | Unset):
        registered (int | Unset):
        premium (int | Unset):
        resell (int | Unset):
        expiring (int | Unset):
        expired (int | Unset):
    """

    total: int | Unset = UNSET
    available: int | Unset = UNSET
    registered: int | Unset = UNSET
    premium: int | Unset = UNSET
    resell: int | Unset = UNSET
    expiring: int | Unset = UNSET
    expired: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        available = self.available

        registered = self.registered

        premium = self.premium

        resell = self.resell

        expiring = self.expiring

        expired = self.expired

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if available is not UNSET:
            field_dict["available"] = available
        if registered is not UNSET:
            field_dict["registered"] = registered
        if premium is not UNSET:
            field_dict["premium"] = premium
        if resell is not UNSET:
            field_dict["resell"] = resell
        if expiring is not UNSET:
            field_dict["expiring"] = expiring
        if expired is not UNSET:
            field_dict["expired"] = expired

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        available = d.pop("available", UNSET)

        registered = d.pop("registered", UNSET)

        premium = d.pop("premium", UNSET)

        resell = d.pop("resell", UNSET)

        expiring = d.pop("expiring", UNSET)

        expired = d.pop("expired", UNSET)

        get_catalog_stats_response_200_data_domains = cls(
            total=total,
            available=available,
            registered=registered,
            premium=premium,
            resell=resell,
            expiring=expiring,
            expired=expired,
        )

        get_catalog_stats_response_200_data_domains.additional_properties = d
        return get_catalog_stats_response_200_data_domains

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
