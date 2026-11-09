from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_name_prices_response_200_data_quotes_item_kind_type_1 import (
    GetNamePricesResponse200DataQuotesItemKindType1,
    check_get_name_prices_response_200_data_quotes_item_kind_type_1,
)
from ..models.get_name_prices_response_200_data_quotes_item_kind_type_2_type_1 import (
    GetNamePricesResponse200DataQuotesItemKindType2Type1,
    check_get_name_prices_response_200_data_quotes_item_kind_type_2_type_1,
)
from ..models.get_name_prices_response_200_data_quotes_item_kind_type_3_type_1 import (
    GetNamePricesResponse200DataQuotesItemKindType3Type1,
    check_get_name_prices_response_200_data_quotes_item_kind_type_3_type_1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNamePricesResponse200DataQuotesItem")


@_attrs_define
class GetNamePricesResponse200DataQuotesItem:
    """
    Attributes:
        registrar (str | Unset):
        first_year (float | None | Unset):
        renewal (float | None | Unset):
        transfer (float | None | Unset):
        regular_price (float | None | Unset):
        is_promo (bool | None | Unset):
        currency (None | str | Unset):
        kind (GetNamePricesResponse200DataQuotesItemKindType1 | GetNamePricesResponse200DataQuotesItemKindType2Type1 |
            GetNamePricesResponse200DataQuotesItemKindType3Type1 | None | Unset):
    """

    registrar: str | Unset = UNSET
    first_year: float | None | Unset = UNSET
    renewal: float | None | Unset = UNSET
    transfer: float | None | Unset = UNSET
    regular_price: float | None | Unset = UNSET
    is_promo: bool | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    kind: (
        GetNamePricesResponse200DataQuotesItemKindType1
        | GetNamePricesResponse200DataQuotesItemKindType2Type1
        | GetNamePricesResponse200DataQuotesItemKindType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registrar = self.registrar

        first_year: float | None | Unset
        if isinstance(self.first_year, Unset):
            first_year = UNSET
        else:
            first_year = self.first_year

        renewal: float | None | Unset
        if isinstance(self.renewal, Unset):
            renewal = UNSET
        else:
            renewal = self.renewal

        transfer: float | None | Unset
        if isinstance(self.transfer, Unset):
            transfer = UNSET
        else:
            transfer = self.transfer

        regular_price: float | None | Unset
        if isinstance(self.regular_price, Unset):
            regular_price = UNSET
        else:
            regular_price = self.regular_price

        is_promo: bool | None | Unset
        if isinstance(self.is_promo, Unset):
            is_promo = UNSET
        else:
            is_promo = self.is_promo

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        elif (
            isinstance(self.kind, str)
            or isinstance(self.kind, str)
            or isinstance(self.kind, str)
        ):
            kind = self.kind
        else:
            kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if registrar is not UNSET:
            field_dict["registrar"] = registrar
        if first_year is not UNSET:
            field_dict["firstYear"] = first_year
        if renewal is not UNSET:
            field_dict["renewal"] = renewal
        if transfer is not UNSET:
            field_dict["transfer"] = transfer
        if regular_price is not UNSET:
            field_dict["regularPrice"] = regular_price
        if is_promo is not UNSET:
            field_dict["isPromo"] = is_promo
        if currency is not UNSET:
            field_dict["currency"] = currency
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        registrar = d.pop("registrar", UNSET)

        def _parse_first_year(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        first_year = _parse_first_year(d.pop("firstYear", UNSET))

        def _parse_renewal(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        renewal = _parse_renewal(d.pop("renewal", UNSET))

        def _parse_transfer(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        transfer = _parse_transfer(d.pop("transfer", UNSET))

        def _parse_regular_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        regular_price = _parse_regular_price(d.pop("regularPrice", UNSET))

        def _parse_is_promo(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_promo = _parse_is_promo(d.pop("isPromo", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_kind(
            data: object,
        ) -> (
            GetNamePricesResponse200DataQuotesItemKindType1
            | GetNamePricesResponse200DataQuotesItemKindType2Type1
            | GetNamePricesResponse200DataQuotesItemKindType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_1 = (
                    check_get_name_prices_response_200_data_quotes_item_kind_type_1(
                        data
                    )
                )

                return kind_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_2_type_1 = check_get_name_prices_response_200_data_quotes_item_kind_type_2_type_1(
                    data
                )

                return kind_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_3_type_1 = check_get_name_prices_response_200_data_quotes_item_kind_type_3_type_1(
                    data
                )

                return kind_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetNamePricesResponse200DataQuotesItemKindType1
                | GetNamePricesResponse200DataQuotesItemKindType2Type1
                | GetNamePricesResponse200DataQuotesItemKindType3Type1
                | None
                | Unset,
                data,
            )

        kind = _parse_kind(d.pop("kind", UNSET))

        get_name_prices_response_200_data_quotes_item = cls(
            registrar=registrar,
            first_year=first_year,
            renewal=renewal,
            transfer=transfer,
            regular_price=regular_price,
            is_promo=is_promo,
            currency=currency,
            kind=kind,
        )

        get_name_prices_response_200_data_quotes_item.additional_properties = d
        return get_name_prices_response_200_data_quotes_item

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
