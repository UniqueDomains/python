from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetTldResponse200DataRegistrarsItem")


@_attrs_define
class GetTldResponse200DataRegistrarsItem:
    """
    Attributes:
        registrar (str):
        name (str):
        homepage_url (None | str):
        purchase_price (float | None):
        renewal_price (float | None):
        renewal_trap (bool): Renewal at least twice the first year and $10 more.
        cheapest (bool): Lowest first year of this list.
    """

    registrar: str
    name: str
    homepage_url: None | str
    purchase_price: float | None
    renewal_price: float | None
    renewal_trap: bool
    cheapest: bool
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

        renewal_trap = self.renewal_trap

        cheapest = self.cheapest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registrar": registrar,
                "name": name,
                "homepageUrl": homepage_url,
                "purchasePrice": purchase_price,
                "renewalPrice": renewal_price,
                "renewalTrap": renewal_trap,
                "cheapest": cheapest,
            }
        )

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

        renewal_trap = d.pop("renewalTrap")

        cheapest = d.pop("cheapest")

        get_tld_response_200_data_registrars_item = cls(
            registrar=registrar,
            name=name,
            homepage_url=homepage_url,
            purchase_price=purchase_price,
            renewal_price=renewal_price,
            renewal_trap=renewal_trap,
            cheapest=cheapest,
        )

        get_tld_response_200_data_registrars_item.additional_properties = d
        return get_tld_response_200_data_registrars_item

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
