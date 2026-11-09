from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNameRegistryHistoryResponse200DataVersionsItem")


@_attrs_define
class GetNameRegistryHistoryResponse200DataVersionsItem:
    """
    Attributes:
        observed_at (datetime.datetime | Unset):
        registrar (None | str | Unset):
        registered (bool | None | Unset):
    """

    observed_at: datetime.datetime | Unset = UNSET
    registrar: None | str | Unset = UNSET
    registered: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        observed_at: str | Unset = UNSET
        if not isinstance(self.observed_at, Unset):
            observed_at = self.observed_at.isoformat()

        registrar: None | str | Unset
        if isinstance(self.registrar, Unset):
            registrar = UNSET
        else:
            registrar = self.registrar

        registered: bool | None | Unset
        if isinstance(self.registered, Unset):
            registered = UNSET
        else:
            registered = self.registered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if observed_at is not UNSET:
            field_dict["observedAt"] = observed_at
        if registrar is not UNSET:
            field_dict["registrar"] = registrar
        if registered is not UNSET:
            field_dict["registered"] = registered

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _observed_at = d.pop("observedAt", UNSET)
        observed_at: datetime.datetime | Unset
        if isinstance(_observed_at, Unset):
            observed_at = UNSET
        else:
            observed_at = datetime.datetime.fromisoformat(_observed_at)

        def _parse_registrar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registrar = _parse_registrar(d.pop("registrar", UNSET))

        def _parse_registered(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        registered = _parse_registered(d.pop("registered", UNSET))

        get_name_registry_history_response_200_data_versions_item = cls(
            observed_at=observed_at,
            registrar=registrar,
            registered=registered,
        )

        get_name_registry_history_response_200_data_versions_item.additional_properties = d
        return get_name_registry_history_response_200_data_versions_item

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
