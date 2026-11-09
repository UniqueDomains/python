from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListTldPricesResponse200DataItem")


@_attrs_define
class ListTldPricesResponse200DataItem:
    """
    Attributes:
        registrar (str):
        name (str):
        homepage_url (None | str):
        purchase_price (float | None):
        renewal_price (float | None):
        transfer_price (float | None):
        currency (None | str):
        is_promo (bool): First year is a promotion.
        renewal_trap (bool): Renewal at least twice the first year and $10 more.
        cheapest (bool): Lowest first year.
        cheapest_renewal (bool): Lowest renewal.
        cheapest_transfer (bool): Lowest transfer-in.
        regular_purchase_price (float | None | Unset):
    """

    registrar: str
    name: str
    homepage_url: None | str
    purchase_price: float | None
    renewal_price: float | None
    transfer_price: float | None
    currency: None | str
    is_promo: bool
    renewal_trap: bool
    cheapest: bool
    cheapest_renewal: bool
    cheapest_transfer: bool
    regular_purchase_price: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registrar = self.registrar

        name = self.name

        homepage_url: None | str
        homepage_url = self.homepage_url

        purchase_price: float | None
        purchase_price = self.purchase_price

        renewal_price: float | None
        renewal_price = self.renewal_price

        transfer_price: float | None
        transfer_price = self.transfer_price

        currency: None | str
        currency = self.currency

        is_promo = self.is_promo

        renewal_trap = self.renewal_trap

        cheapest = self.cheapest

        cheapest_renewal = self.cheapest_renewal

        cheapest_transfer = self.cheapest_transfer

        regular_purchase_price: float | None | Unset
        if isinstance(self.regular_purchase_price, Unset):
            regular_purchase_price = UNSET
        else:
            regular_purchase_price = self.regular_purchase_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registrar": registrar,
                "name": name,
                "homepageUrl": homepage_url,
                "purchasePrice": purchase_price,
                "renewalPrice": renewal_price,
                "transferPrice": transfer_price,
                "currency": currency,
                "isPromo": is_promo,
                "renewalTrap": renewal_trap,
                "cheapest": cheapest,
                "cheapestRenewal": cheapest_renewal,
                "cheapestTransfer": cheapest_transfer,
            }
        )
        if regular_purchase_price is not UNSET:
            field_dict["regularPurchasePrice"] = regular_purchase_price

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        registrar = d.pop("registrar")

        name = d.pop("name")

        def _parse_homepage_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        homepage_url = _parse_homepage_url(d.pop("homepageUrl"))

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

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        is_promo = d.pop("isPromo")

        renewal_trap = d.pop("renewalTrap")

        cheapest = d.pop("cheapest")

        cheapest_renewal = d.pop("cheapestRenewal")

        cheapest_transfer = d.pop("cheapestTransfer")

        def _parse_regular_purchase_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        regular_purchase_price = _parse_regular_purchase_price(
            d.pop("regularPurchasePrice", UNSET)
        )

        list_tld_prices_response_200_data_item = cls(
            registrar=registrar,
            name=name,
            homepage_url=homepage_url,
            purchase_price=purchase_price,
            renewal_price=renewal_price,
            transfer_price=transfer_price,
            currency=currency,
            is_promo=is_promo,
            renewal_trap=renewal_trap,
            cheapest=cheapest,
            cheapest_renewal=cheapest_renewal,
            cheapest_transfer=cheapest_transfer,
            regular_purchase_price=regular_purchase_price,
        )

        list_tld_prices_response_200_data_item.additional_properties = d
        return list_tld_prices_response_200_data_item

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
