from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_word_endings_response_200_data_by_group import (
        GetWordEndingsResponse200DataByGroup,
    )
    from ..models.get_word_endings_response_200_data_cheapest import (
        GetWordEndingsResponse200DataCheapest,
    )
    from ..models.get_word_endings_response_200_data_key_endings_item import (
        GetWordEndingsResponse200DataKeyEndingsItem,
    )
    from ..models.get_word_endings_response_200_data_open_by_ending import (
        GetWordEndingsResponse200DataOpenByEnding,
    )


T = TypeVar("T", bound="GetWordEndingsResponse200Data")


@_attrs_define
class GetWordEndingsResponse200Data:
    """
    Attributes:
        by_group (GetWordEndingsResponse200DataByGroup):
        key_endings (list[GetWordEndingsResponse200DataKeyEndingsItem]):
        open_by_ending (GetWordEndingsResponse200DataOpenByEnding): `{ ending: count }`.
        cheapest (GetWordEndingsResponse200DataCheapest | Unset): Keyed `include=cheapest` only.
    """

    by_group: GetWordEndingsResponse200DataByGroup
    key_endings: list[GetWordEndingsResponse200DataKeyEndingsItem]
    open_by_ending: GetWordEndingsResponse200DataOpenByEnding
    cheapest: GetWordEndingsResponse200DataCheapest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_group = self.by_group.to_dict()

        key_endings = []
        for key_endings_item_data in self.key_endings:
            key_endings_item = key_endings_item_data.to_dict()
            key_endings.append(key_endings_item)

        open_by_ending = self.open_by_ending.to_dict()

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
            }
        )
        if cheapest is not UNSET:
            field_dict["cheapest"] = cheapest

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_word_endings_response_200_data_by_group import (
            GetWordEndingsResponse200DataByGroup,
        )
        from ..models.get_word_endings_response_200_data_cheapest import (
            GetWordEndingsResponse200DataCheapest,
        )
        from ..models.get_word_endings_response_200_data_key_endings_item import (
            GetWordEndingsResponse200DataKeyEndingsItem,
        )
        from ..models.get_word_endings_response_200_data_open_by_ending import (
            GetWordEndingsResponse200DataOpenByEnding,
        )

        d = dict(src_dict)
        by_group = GetWordEndingsResponse200DataByGroup.from_dict(d.pop("byGroup"))

        key_endings = []
        _key_endings = d.pop("keyEndings")
        for key_endings_item_data in _key_endings:
            key_endings_item = GetWordEndingsResponse200DataKeyEndingsItem.from_dict(
                key_endings_item_data
            )

            key_endings.append(key_endings_item)

        open_by_ending = GetWordEndingsResponse200DataOpenByEnding.from_dict(
            d.pop("openByEnding")
        )

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
