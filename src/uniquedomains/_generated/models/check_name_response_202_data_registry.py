from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_name_response_202_data_registry_registrar_type_0 import (
        CheckNameResponse202DataRegistryRegistrarType0,
    )


T = TypeVar("T", bound="CheckNameResponse202DataRegistry")


@_attrs_define
class CheckNameResponse202DataRegistry:
    """
    Attributes:
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        expires_at (datetime.datetime | None | Unset):
        registry_updated_at (datetime.datetime | None | Unset):
        registrar (CheckNameResponse202DataRegistryRegistrarType0 | None | Unset):
    """

    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    registry_updated_at: datetime.datetime | None | Unset = UNSET
    registrar: CheckNameResponse202DataRegistryRegistrarType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.check_name_response_202_data_registry_registrar_type_0 import (
            CheckNameResponse202DataRegistryRegistrarType0,
        )

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        registry_updated_at: None | str | Unset
        if isinstance(self.registry_updated_at, Unset):
            registry_updated_at = UNSET
        elif isinstance(self.registry_updated_at, datetime.datetime):
            registry_updated_at = self.registry_updated_at.isoformat()
        else:
            registry_updated_at = self.registry_updated_at

        registrar: dict[str, Any] | None | Unset
        if isinstance(self.registrar, Unset):
            registrar = UNSET
        elif isinstance(self.registrar, CheckNameResponse202DataRegistryRegistrarType0):
            registrar = self.registrar.to_dict()
        else:
            registrar = self.registrar

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if registry_updated_at is not UNSET:
            field_dict["registryUpdatedAt"] = registry_updated_at
        if registrar is not UNSET:
            field_dict["registrar"] = registrar

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.check_name_response_202_data_registry_registrar_type_0 import (
            CheckNameResponse202DataRegistryRegistrarType0,
        )

        d = dict(src_dict)

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))

        def _parse_registry_updated_at(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registry_updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return registry_updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        registry_updated_at = _parse_registry_updated_at(
            d.pop("registryUpdatedAt", UNSET)
        )

        def _parse_registrar(
            data: object,
        ) -> CheckNameResponse202DataRegistryRegistrarType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                registrar_type_0 = (
                    CheckNameResponse202DataRegistryRegistrarType0.from_dict(data)
                )

                return registrar_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CheckNameResponse202DataRegistryRegistrarType0 | None | Unset, data
            )

        registrar = _parse_registrar(d.pop("registrar", UNSET))

        check_name_response_202_data_registry = cls(
            created_at=created_at,
            updated_at=updated_at,
            expires_at=expires_at,
            registry_updated_at=registry_updated_at,
            registrar=registrar,
        )

        check_name_response_202_data_registry.additional_properties = d
        return check_name_response_202_data_registry

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
