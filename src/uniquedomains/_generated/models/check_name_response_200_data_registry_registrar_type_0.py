from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckNameResponse200DataRegistryRegistrarType0")


@_attrs_define
class CheckNameResponse200DataRegistryRegistrarType0:
    """
    Attributes:
        name (str | Unset):
        iana_id (int | None | Unset):
        url (None | str | Unset):
    """

    name: str | Unset = UNSET
    iana_id: int | None | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        iana_id: int | None | Unset
        if isinstance(self.iana_id, Unset):
            iana_id = UNSET
        else:
            iana_id = self.iana_id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if iana_id is not UNSET:
            field_dict["ianaId"] = iana_id
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_iana_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        iana_id = _parse_iana_id(d.pop("ianaId", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        check_name_response_200_data_registry_registrar_type_0 = cls(
            name=name,
            iana_id=iana_id,
            url=url,
        )

        check_name_response_200_data_registry_registrar_type_0.additional_properties = d
        return check_name_response_200_data_registry_registrar_type_0

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
