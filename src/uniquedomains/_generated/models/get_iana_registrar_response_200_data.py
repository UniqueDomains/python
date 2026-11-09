from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_iana_registrar_response_200_data_status import (
    GetIanaRegistrarResponse200DataStatus,
    check_get_iana_registrar_response_200_data_status,
)

T = TypeVar("T", bound="GetIanaRegistrarResponse200Data")


@_attrs_define
class GetIanaRegistrarResponse200Data:
    """
    Attributes:
        id (int): IANA registrar id.
        name (str): Name as IANA publishes it.
        status (GetIanaRegistrarResponse200DataStatus):
        rdap_base_url (None | str):
    """

    id: int
    name: str
    status: GetIanaRegistrarResponse200DataStatus
    rdap_base_url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status: str = self.status

        rdap_base_url: None | str
        rdap_base_url = self.rdap_base_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "rdapBaseUrl": rdap_base_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status = check_get_iana_registrar_response_200_data_status(d.pop("status"))

        def _parse_rdap_base_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rdap_base_url = _parse_rdap_base_url(d.pop("rdapBaseUrl"))

        get_iana_registrar_response_200_data = cls(
            id=id,
            name=name,
            status=status,
            rdap_base_url=rdap_base_url,
        )

        get_iana_registrar_response_200_data.additional_properties = d
        return get_iana_registrar_response_200_data

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
