from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_name_registry_response_200_data_transport_type_1 import (
    GetNameRegistryResponse200DataTransportType1,
    check_get_name_registry_response_200_data_transport_type_1,
)
from ..models.get_name_registry_response_200_data_transport_type_2_type_1 import (
    GetNameRegistryResponse200DataTransportType2Type1,
    check_get_name_registry_response_200_data_transport_type_2_type_1,
)
from ..models.get_name_registry_response_200_data_transport_type_3_type_1 import (
    GetNameRegistryResponse200DataTransportType3Type1,
    check_get_name_registry_response_200_data_transport_type_3_type_1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_name_registry_response_200_data_epp_statuses_item import (
        GetNameRegistryResponse200DataEppStatusesItem,
    )
    from ..models.get_name_registry_response_200_data_holder import (
        GetNameRegistryResponse200DataHolder,
    )
    from ..models.get_name_registry_response_200_data_registrar_type_0 import (
        GetNameRegistryResponse200DataRegistrarType0,
    )


T = TypeVar("T", bound="GetNameRegistryResponse200Data")


@_attrs_define
class GetNameRegistryResponse200Data:
    """
    Attributes:
        read (bool):
        observed_on (datetime.date | None):
        registrar (GetNameRegistryResponse200DataRegistrarType0 | None):
        epp_statuses (list[GetNameRegistryResponse200DataEppStatusesItem]):
        nameservers (list[str]):
        holder (GetNameRegistryResponse200DataHolder):
        transport (GetNameRegistryResponse200DataTransportType1 | GetNameRegistryResponse200DataTransportType2Type1 |
            GetNameRegistryResponse200DataTransportType3Type1 | None):
        observed_at (datetime.datetime | None | Unset): Keyed.
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        expires_at (datetime.datetime | None | Unset):
        registry_updated_at (datetime.datetime | None | Unset):
        dnssec (bool | None | Unset):
    """

    read: bool
    observed_on: datetime.date | None
    registrar: GetNameRegistryResponse200DataRegistrarType0 | None
    epp_statuses: list[GetNameRegistryResponse200DataEppStatusesItem]
    nameservers: list[str]
    holder: GetNameRegistryResponse200DataHolder
    transport: (
        GetNameRegistryResponse200DataTransportType1
        | GetNameRegistryResponse200DataTransportType2Type1
        | GetNameRegistryResponse200DataTransportType3Type1
        | None
    )
    observed_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    registry_updated_at: datetime.datetime | None | Unset = UNSET
    dnssec: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_name_registry_response_200_data_registrar_type_0 import (
            GetNameRegistryResponse200DataRegistrarType0,
        )

        read = self.read

        observed_on: None | str
        if isinstance(self.observed_on, datetime.date):
            observed_on = self.observed_on.isoformat()
        else:
            observed_on = self.observed_on

        registrar: dict[str, Any] | None
        if isinstance(self.registrar, GetNameRegistryResponse200DataRegistrarType0):
            registrar = self.registrar.to_dict()
        else:
            registrar = self.registrar

        epp_statuses = []
        for epp_statuses_item_data in self.epp_statuses:
            epp_statuses_item = epp_statuses_item_data.to_dict()
            epp_statuses.append(epp_statuses_item)

        nameservers = self.nameservers

        holder = self.holder.to_dict()

        transport: None | str
        if (
            isinstance(self.transport, str)
            or isinstance(self.transport, str)
            or isinstance(self.transport, str)
        ):
            transport = self.transport
        else:
            transport = self.transport

        observed_at: None | str | Unset
        if isinstance(self.observed_at, Unset):
            observed_at = UNSET
        elif isinstance(self.observed_at, datetime.datetime):
            observed_at = self.observed_at.isoformat()
        else:
            observed_at = self.observed_at

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

        dnssec: bool | None | Unset
        if isinstance(self.dnssec, Unset):
            dnssec = UNSET
        else:
            dnssec = self.dnssec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "read": read,
                "observedOn": observed_on,
                "registrar": registrar,
                "eppStatuses": epp_statuses,
                "nameservers": nameservers,
                "holder": holder,
                "transport": transport,
            }
        )
        if observed_at is not UNSET:
            field_dict["observedAt"] = observed_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if registry_updated_at is not UNSET:
            field_dict["registryUpdatedAt"] = registry_updated_at
        if dnssec is not UNSET:
            field_dict["dnssec"] = dnssec

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_name_registry_response_200_data_epp_statuses_item import (
            GetNameRegistryResponse200DataEppStatusesItem,
        )
        from ..models.get_name_registry_response_200_data_holder import (
            GetNameRegistryResponse200DataHolder,
        )
        from ..models.get_name_registry_response_200_data_registrar_type_0 import (
            GetNameRegistryResponse200DataRegistrarType0,
        )

        d = dict(src_dict)
        read = d.pop("read")

        def _parse_observed_on(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                observed_on_type_0 = datetime.date.fromisoformat(data)

                return observed_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        observed_on = _parse_observed_on(d.pop("observedOn"))

        def _parse_registrar(
            data: object,
        ) -> GetNameRegistryResponse200DataRegistrarType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                registrar_type_0 = (
                    GetNameRegistryResponse200DataRegistrarType0.from_dict(data)
                )

                return registrar_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetNameRegistryResponse200DataRegistrarType0 | None, data)

        registrar = _parse_registrar(d.pop("registrar"))

        epp_statuses = []
        _epp_statuses = d.pop("eppStatuses")
        for epp_statuses_item_data in _epp_statuses:
            epp_statuses_item = GetNameRegistryResponse200DataEppStatusesItem.from_dict(
                epp_statuses_item_data
            )

            epp_statuses.append(epp_statuses_item)

        nameservers = cast(list[str], d.pop("nameservers"))

        holder = GetNameRegistryResponse200DataHolder.from_dict(d.pop("holder"))

        def _parse_transport(
            data: object,
        ) -> (
            GetNameRegistryResponse200DataTransportType1
            | GetNameRegistryResponse200DataTransportType2Type1
            | GetNameRegistryResponse200DataTransportType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                transport_type_1 = (
                    check_get_name_registry_response_200_data_transport_type_1(data)
                )

                return transport_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                transport_type_2_type_1 = (
                    check_get_name_registry_response_200_data_transport_type_2_type_1(
                        data
                    )
                )

                return transport_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                transport_type_3_type_1 = (
                    check_get_name_registry_response_200_data_transport_type_3_type_1(
                        data
                    )
                )

                return transport_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetNameRegistryResponse200DataTransportType1
                | GetNameRegistryResponse200DataTransportType2Type1
                | GetNameRegistryResponse200DataTransportType3Type1
                | None,
                data,
            )

        transport = _parse_transport(d.pop("transport"))

        def _parse_observed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                observed_at_type_0 = datetime.datetime.fromisoformat(data)

                return observed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        observed_at = _parse_observed_at(d.pop("observedAt", UNSET))

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

        def _parse_dnssec(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        dnssec = _parse_dnssec(d.pop("dnssec", UNSET))

        get_name_registry_response_200_data = cls(
            read=read,
            observed_on=observed_on,
            registrar=registrar,
            epp_statuses=epp_statuses,
            nameservers=nameservers,
            holder=holder,
            transport=transport,
            observed_at=observed_at,
            created_at=created_at,
            updated_at=updated_at,
            expires_at=expires_at,
            registry_updated_at=registry_updated_at,
            dnssec=dnssec,
        )

        get_name_registry_response_200_data.additional_properties = d
        return get_name_registry_response_200_data

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
