from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_expiring_domains_response_200_data_item_status import (
    ListExpiringDomainsResponse200DataItemStatus,
    check_list_expiring_domains_response_200_data_item_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListExpiringDomainsResponse200DataItem")


@_attrs_define
class ListExpiringDomainsResponse200DataItem:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        ending (str | Unset):
        status (ListExpiringDomainsResponse200DataItemStatus | Unset):
        expires_on (datetime.date | Unset):
        drops_on (datetime.date | None | Unset):
        registrar (None | str | Unset):
        price (float | None | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    ending: str | Unset = UNSET
    status: ListExpiringDomainsResponse200DataItemStatus | Unset = UNSET
    expires_on: datetime.date | Unset = UNSET
    drops_on: datetime.date | None | Unset = UNSET
    registrar: None | str | Unset = UNSET
    price: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        ending = self.ending

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        expires_on: str | Unset = UNSET
        if not isinstance(self.expires_on, Unset):
            expires_on = self.expires_on.isoformat()

        drops_on: None | str | Unset
        if isinstance(self.drops_on, Unset):
            drops_on = UNSET
        elif isinstance(self.drops_on, datetime.date):
            drops_on = self.drops_on.isoformat()
        else:
            drops_on = self.drops_on

        registrar: None | str | Unset
        if isinstance(self.registrar, Unset):
            registrar = UNSET
        else:
            registrar = self.registrar

        price: float | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if ending is not UNSET:
            field_dict["ending"] = ending
        if status is not UNSET:
            field_dict["status"] = status
        if expires_on is not UNSET:
            field_dict["expiresOn"] = expires_on
        if drops_on is not UNSET:
            field_dict["dropsOn"] = drops_on
        if registrar is not UNSET:
            field_dict["registrar"] = registrar
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        ending = d.pop("ending", UNSET)

        _status = d.pop("status", UNSET)
        status: ListExpiringDomainsResponse200DataItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_list_expiring_domains_response_200_data_item_status(_status)

        _expires_on = d.pop("expiresOn", UNSET)
        expires_on: datetime.date | Unset
        if isinstance(_expires_on, Unset):
            expires_on = UNSET
        else:
            expires_on = datetime.date.fromisoformat(_expires_on)

        def _parse_drops_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                drops_on_type_0 = datetime.date.fromisoformat(data)

                return drops_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        drops_on = _parse_drops_on(d.pop("dropsOn", UNSET))

        def _parse_registrar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registrar = _parse_registrar(d.pop("registrar", UNSET))

        def _parse_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        list_expiring_domains_response_200_data_item = cls(
            id=id,
            name=name,
            ending=ending,
            status=status,
            expires_on=expires_on,
            drops_on=drops_on,
            registrar=registrar,
            price=price,
        )

        list_expiring_domains_response_200_data_item.additional_properties = d
        return list_expiring_domains_response_200_data_item

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
