from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_word_endings_response_200_data_by_group_type_0 import (
        GetWordEndingsResponse200DataByGroupType0,
    )
    from ..models.get_word_endings_response_200_data_cheapest import (
        GetWordEndingsResponse200DataCheapest,
    )
    from ..models.get_word_endings_response_200_data_key_endings_item import (
        GetWordEndingsResponse200DataKeyEndingsItem,
    )
    from ..models.get_word_endings_response_200_data_open_by_ending_type_0 import (
        GetWordEndingsResponse200DataOpenByEndingType0,
    )


T = TypeVar("T", bound="GetWordEndingsResponse200Data")


@_attrs_define
class GetWordEndingsResponse200Data:
    """
    Attributes:
        by_group (GetWordEndingsResponse200DataByGroupType0 | None): Null for a word with no count yet; zeros are real.
        key_endings (list[GetWordEndingsResponse200DataKeyEndingsItem]):
        open_by_ending (GetWordEndingsResponse200DataOpenByEndingType0 | None): `{ ending: count }`; null for a word
            with no count yet; zeros are real.
        available_on (list[str] | None): `availableOn` names the endings where the word is unregistered at the standard
            price.
        for_sale_on (list[str] | None): `forSaleOn` names the endings where it can be bought another way: at a premium
            price, from a resale listing, or as a name that is expiring or expired.
        cheapest (GetWordEndingsResponse200DataCheapest | Unset): Keyed `include=cheapest` only.
    """

    by_group: GetWordEndingsResponse200DataByGroupType0 | None
    key_endings: list[GetWordEndingsResponse200DataKeyEndingsItem]
    open_by_ending: GetWordEndingsResponse200DataOpenByEndingType0 | None
    available_on: list[str] | None
    for_sale_on: list[str] | None
    cheapest: GetWordEndingsResponse200DataCheapest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_word_endings_response_200_data_by_group_type_0 import (
            GetWordEndingsResponse200DataByGroupType0,
        )
        from ..models.get_word_endings_response_200_data_open_by_ending_type_0 import (
            GetWordEndingsResponse200DataOpenByEndingType0,
        )

        by_group: dict[str, Any] | None
        if isinstance(self.by_group, GetWordEndingsResponse200DataByGroupType0):
            by_group = self.by_group.to_dict()
        else:
            by_group = self.by_group

        key_endings = []
        for key_endings_item_data in self.key_endings:
            key_endings_item = key_endings_item_data.to_dict()
            key_endings.append(key_endings_item)

        open_by_ending: dict[str, Any] | None
        if isinstance(
            self.open_by_ending, GetWordEndingsResponse200DataOpenByEndingType0
        ):
            open_by_ending = self.open_by_ending.to_dict()
        else:
            open_by_ending = self.open_by_ending

        available_on: list[str] | None
        if isinstance(self.available_on, list):
            available_on = self.available_on

        else:
            available_on = self.available_on

        for_sale_on: list[str] | None
        if isinstance(self.for_sale_on, list):
            for_sale_on = self.for_sale_on

        else:
            for_sale_on = self.for_sale_on

        cheapest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cheapest, Unset):
            cheapest = self.cheapest.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "byGroup": by_group,
                "keyEndings": key_endings,
                "openByEnding": open_by_ending,
                "availableOn": available_on,
                "forSaleOn": for_sale_on,
            }
        )
        if cheapest is not UNSET:
            field_dict["cheapest"] = cheapest

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_word_endings_response_200_data_by_group_type_0 import (
            GetWordEndingsResponse200DataByGroupType0,
        )
        from ..models.get_word_endings_response_200_data_cheapest import (
            GetWordEndingsResponse200DataCheapest,
        )
        from ..models.get_word_endings_response_200_data_key_endings_item import (
            GetWordEndingsResponse200DataKeyEndingsItem,
        )
        from ..models.get_word_endings_response_200_data_open_by_ending_type_0 import (
            GetWordEndingsResponse200DataOpenByEndingType0,
        )

        d = dict(src_dict)

        def _parse_by_group(
            data: object,
        ) -> GetWordEndingsResponse200DataByGroupType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                by_group_type_0 = GetWordEndingsResponse200DataByGroupType0.from_dict(
                    data
                )

                return by_group_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetWordEndingsResponse200DataByGroupType0 | None, data)

        by_group = _parse_by_group(d.pop("byGroup"))

        key_endings = []
        _key_endings = d.pop("keyEndings")
        for key_endings_item_data in _key_endings:
            key_endings_item = GetWordEndingsResponse200DataKeyEndingsItem.from_dict(
                key_endings_item_data
            )

            key_endings.append(key_endings_item)

        def _parse_open_by_ending(
            data: object,
        ) -> GetWordEndingsResponse200DataOpenByEndingType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                open_by_ending_type_0 = (
                    GetWordEndingsResponse200DataOpenByEndingType0.from_dict(data)
                )

                return open_by_ending_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetWordEndingsResponse200DataOpenByEndingType0 | None, data)

        open_by_ending = _parse_open_by_ending(d.pop("openByEnding"))

        def _parse_available_on(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                available_on_type_0 = cast(list[str], data)

                return available_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        available_on = _parse_available_on(d.pop("availableOn"))

        def _parse_for_sale_on(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                for_sale_on_type_0 = cast(list[str], data)

                return for_sale_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        for_sale_on = _parse_for_sale_on(d.pop("forSaleOn"))

        _cheapest = d.pop("cheapest", UNSET)
        cheapest: GetWordEndingsResponse200DataCheapest | Unset
        if isinstance(_cheapest, Unset):
            cheapest = UNSET
        else:
            cheapest = GetWordEndingsResponse200DataCheapest.from_dict(_cheapest)

        get_word_endings_response_200_data = cls(
            by_group=by_group,
            key_endings=key_endings,
            open_by_ending=open_by_ending,
            available_on=available_on,
            for_sale_on=for_sale_on,
            cheapest=cheapest,
        )

        get_word_endings_response_200_data.additional_properties = d
        return get_word_endings_response_200_data

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
