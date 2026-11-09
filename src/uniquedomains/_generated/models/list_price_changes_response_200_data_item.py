from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_price_changes_response_200_data_item_field import (
    ListPriceChangesResponse200DataItemField,
    check_list_price_changes_response_200_data_item_field,
)

T = TypeVar("T", bound="ListPriceChangesResponse200DataItem")


@_attrs_define
class ListPriceChangesResponse200DataItem:
    """
    Attributes:
        id (str): `TldPriceChange.id` as a string.
        extension (str): Bare ending.
        registrar (str): Registrar slug.
        registrar_name (str): Display name.
        field (ListPriceChangesResponse200DataItemField): Which price moved.
        old_price (float): Before.
        new_price (float): After.
        currency (str): ISO 4217.
        confirmed_at (datetime.datetime): Confirmation timestamp.
    """

    id: str
    extension: str
    registrar: str
    registrar_name: str
    field: ListPriceChangesResponse200DataItemField
    old_price: float
    new_price: float
    currency: str
    confirmed_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        extension = self.extension

        registrar = self.registrar

        registrar_name = self.registrar_name

        field: str = self.field

        old_price = self.old_price

        new_price = self.new_price

        currency = self.currency

        confirmed_at = self.confirmed_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "extension": extension,
                "registrar": registrar,
                "registrarName": registrar_name,
                "field": field,
                "oldPrice": old_price,
                "newPrice": new_price,
                "currency": currency,
                "confirmedAt": confirmed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        extension = d.pop("extension")

        registrar = d.pop("registrar")

        registrar_name = d.pop("registrarName")

        field = check_list_price_changes_response_200_data_item_field(d.pop("field"))

        old_price = d.pop("oldPrice")

        new_price = d.pop("newPrice")

        currency = d.pop("currency")

        confirmed_at = datetime.datetime.fromisoformat(d.pop("confirmedAt"))

        list_price_changes_response_200_data_item = cls(
            id=id,
            extension=extension,
            registrar=registrar,
            registrar_name=registrar_name,
            field=field,
            old_price=old_price,
            new_price=new_price,
            currency=currency,
            confirmed_at=confirmed_at,
        )

        list_price_changes_response_200_data_item.additional_properties = d
        return list_price_changes_response_200_data_item

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
