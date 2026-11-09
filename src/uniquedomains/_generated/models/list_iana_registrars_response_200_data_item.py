from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_iana_registrars_response_200_data_item_status import (
    ListIanaRegistrarsResponse200DataItemStatus,
    check_list_iana_registrars_response_200_data_item_status,
)

T = TypeVar("T", bound="ListIanaRegistrarsResponse200DataItem")


@_attrs_define
class ListIanaRegistrarsResponse200DataItem:
    """
    Attributes:
        id (int): IANA registrar id.
        name (str): Name as IANA publishes it.
        status (ListIanaRegistrarsResponse200DataItemStatus):
        rdap_base_url (None | str):
    """

    id: int
    name: str
    status: ListIanaRegistrarsResponse200DataItemStatus
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

        status = check_list_iana_registrars_response_200_data_item_status(
            d.pop("status")
        )

        def _parse_rdap_base_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rdap_base_url = _parse_rdap_base_url(d.pop("rdapBaseUrl"))

        list_iana_registrars_response_200_data_item = cls(
            id=id,
            name=name,
            status=status,
            rdap_base_url=rdap_base_url,
        )

        list_iana_registrars_response_200_data_item.additional_properties = d
        return list_iana_registrars_response_200_data_item

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
