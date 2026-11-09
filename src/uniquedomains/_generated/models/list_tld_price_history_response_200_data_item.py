from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListTldPriceHistoryResponse200DataItem")


@_attrs_define
class ListTldPriceHistoryResponse200DataItem:
    """
    Attributes:
        registrar (str):
        currency (None | str):
        purchase_price (float | None):
        regular_purchase_price (float | None):
        renewal_price (float | None):
        transfer_price (float | None):
        is_promo (bool | None):
        first_seen_at (datetime.datetime): First observation of this price set.
        last_seen_at (datetime.datetime): Last observation.
        observations (int): Reads that saw it.
    """

    registrar: str
    currency: None | str
    purchase_price: float | None
    regular_purchase_price: float | None
    renewal_price: float | None
    transfer_price: float | None
    is_promo: bool | None
    first_seen_at: datetime.datetime
    last_seen_at: datetime.datetime
    observations: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registrar = self.registrar

        currency: None | str
        currency = self.currency

        purchase_price: float | None
        purchase_price = self.purchase_price

        regular_purchase_price: float | None
        regular_purchase_price = self.regular_purchase_price

        renewal_price: float | None
        renewal_price = self.renewal_price

        transfer_price: float | None
        transfer_price = self.transfer_price

        is_promo: bool | None
        is_promo = self.is_promo

        first_seen_at = self.first_seen_at.isoformat()

        last_seen_at = self.last_seen_at.isoformat()

        observations = self.observations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registrar": registrar,
                "currency": currency,
                "purchasePrice": purchase_price,
                "regularPurchasePrice": regular_purchase_price,
                "renewalPrice": renewal_price,
                "transferPrice": transfer_price,
                "isPromo": is_promo,
                "firstSeenAt": first_seen_at,
                "lastSeenAt": last_seen_at,
                "observations": observations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        registrar = d.pop("registrar")

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        def _parse_purchase_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        purchase_price = _parse_purchase_price(d.pop("purchasePrice"))

        def _parse_regular_purchase_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        regular_purchase_price = _parse_regular_purchase_price(
            d.pop("regularPurchasePrice")
        )

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

        first_seen_at = datetime.datetime.fromisoformat(d.pop("firstSeenAt"))

        last_seen_at = datetime.datetime.fromisoformat(d.pop("lastSeenAt"))

        observations = d.pop("observations")

        list_tld_price_history_response_200_data_item = cls(
            registrar=registrar,
            currency=currency,
            purchase_price=purchase_price,
            regular_purchase_price=regular_purchase_price,
            renewal_price=renewal_price,
            transfer_price=transfer_price,
            is_promo=is_promo,
            first_seen_at=first_seen_at,
            last_seen_at=last_seen_at,
            observations=observations,
        )

        list_tld_price_history_response_200_data_item.additional_properties = d
        return list_tld_price_history_response_200_data_item

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
