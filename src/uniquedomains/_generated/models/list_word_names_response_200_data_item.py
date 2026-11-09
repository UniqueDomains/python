from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListWordNamesResponse200DataItem")


@_attrs_define
class ListWordNamesResponse200DataItem:
    """
    Attributes:
        id (str | Unset): `dom_<uuid>`.
        name (str | Unset):
        ending (str | Unset):
        status (str | Unset):
        price (float | None | Unset):
        renewal (float | None | Unset):
        registrar (None | str | Unset):
        expires (datetime.datetime | None | Unset):
        parking (None | str | Unset):
        lifecycle (None | str | Unset):
        drops_on (datetime.date | None | Unset):
        created (datetime.datetime | None | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    ending: str | Unset = UNSET
    status: str | Unset = UNSET
    price: float | None | Unset = UNSET
    renewal: float | None | Unset = UNSET
    registrar: None | str | Unset = UNSET
    expires: datetime.datetime | None | Unset = UNSET
    parking: None | str | Unset = UNSET
    lifecycle: None | str | Unset = UNSET
    drops_on: datetime.date | None | Unset = UNSET
    created: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        ending = self.ending

        status = self.status

        price: float | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        renewal: float | None | Unset
        if isinstance(self.renewal, Unset):
            renewal = UNSET
        else:
            renewal = self.renewal

        registrar: None | str | Unset
        if isinstance(self.registrar, Unset):
            registrar = UNSET
        else:
            registrar = self.registrar

        expires: None | str | Unset
        if isinstance(self.expires, Unset):
            expires = UNSET
        elif isinstance(self.expires, datetime.datetime):
            expires = self.expires.isoformat()
        else:
            expires = self.expires

        parking: None | str | Unset
        if isinstance(self.parking, Unset):
            parking = UNSET
        else:
            parking = self.parking

        lifecycle: None | str | Unset
        if isinstance(self.lifecycle, Unset):
            lifecycle = UNSET
        else:
            lifecycle = self.lifecycle

        drops_on: None | str | Unset
        if isinstance(self.drops_on, Unset):
            drops_on = UNSET
        elif isinstance(self.drops_on, datetime.date):
            drops_on = self.drops_on.isoformat()
        else:
            drops_on = self.drops_on

        created: None | str | Unset
        if isinstance(self.created, Unset):
            created = UNSET
        elif isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

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
        if price is not UNSET:
            field_dict["price"] = price
        if renewal is not UNSET:
            field_dict["renewal"] = renewal
        if registrar is not UNSET:
            field_dict["registrar"] = registrar
        if expires is not UNSET:
            field_dict["expires"] = expires
        if parking is not UNSET:
            field_dict["parking"] = parking
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if drops_on is not UNSET:
            field_dict["dropsOn"] = drops_on
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        ending = d.pop("ending", UNSET)

        status = d.pop("status", UNSET)

        def _parse_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_renewal(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        renewal = _parse_renewal(d.pop("renewal", UNSET))

        def _parse_registrar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registrar = _parse_registrar(d.pop("registrar", UNSET))

        def _parse_expires(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_type_0 = datetime.datetime.fromisoformat(data)

                return expires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires = _parse_expires(d.pop("expires", UNSET))

        def _parse_parking(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parking = _parse_parking(d.pop("parking", UNSET))

        def _parse_lifecycle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lifecycle = _parse_lifecycle(d.pop("lifecycle", UNSET))

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

        def _parse_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = datetime.datetime.fromisoformat(data)

                return created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created = _parse_created(d.pop("created", UNSET))

        list_word_names_response_200_data_item = cls(
            id=id,
            name=name,
            ending=ending,
            status=status,
            price=price,
            renewal=renewal,
            registrar=registrar,
            expires=expires,
            parking=parking,
            lifecycle=lifecycle,
            drops_on=drops_on,
            created=created,
        )

        list_word_names_response_200_data_item.additional_properties = d
        return list_word_names_response_200_data_item

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
