from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListRegistrarPricesResponse200DataItem")


@_attrs_define
class ListRegistrarPricesResponse200DataItem:
    """
    Attributes:
        extension (str): Bare ending, the row key.
        purchase_price (float | None):
        renewal_price (float | None):
        transfer_price (float | None):
        is_promo (bool | None):
        currency (None | str):
        delisted (bool | Unset): Paid subscriptions only: the last complete list no longer carries the ending.
    """

    extension: str
    purchase_price: float | None
    renewal_price: float | None
    transfer_price: float | None
    is_promo: bool | None
    currency: None | str
    delisted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extension = self.extension

        purchase_price: float | None
        purchase_price = self.purchase_price

        renewal_price: float | None
        renewal_price = self.renewal_price

        transfer_price: float | None
        transfer_price = self.transfer_price

        is_promo: bool | None
        is_promo = self.is_promo

        currency: None | str
        currency = self.currency

        delisted = self.delisted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extension": extension,
                "purchasePrice": purchase_price,
                "renewalPrice": renewal_price,
                "transferPrice": transfer_price,
                "isPromo": is_promo,
                "currency": currency,
            }
        )
        if delisted is not UNSET:
            field_dict["delisted"] = delisted

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        extension = d.pop("extension")

        def _parse_purchase_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        purchase_price = _parse_purchase_price(d.pop("purchasePrice"))

        def _parse_renewal_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        renewal_price = _parse_renewal_price(d.pop("renewalPrice"))

        def _parse_transfer_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        transfer_price = _parse_transfer_price(d.pop("transferPrice"))

        def _parse_is_promo(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_promo = _parse_is_promo(d.pop("isPromo"))

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        delisted = d.pop("delisted", UNSET)

        list_registrar_prices_response_200_data_item = cls(
            extension=extension,
            purchase_price=purchase_price,
            renewal_price=renewal_price,
            transfer_price=transfer_price,
            is_promo=is_promo,
            currency=currency,
            delisted=delisted,
        )

        list_registrar_prices_response_200_data_item.additional_properties = d
        return list_registrar_prices_response_200_data_item

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
