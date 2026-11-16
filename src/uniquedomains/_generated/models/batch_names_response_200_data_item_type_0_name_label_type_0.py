from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.batch_names_response_200_data_item_type_0_name_label_type_0_type import (
    BatchNamesResponse200DataItemType0NameLabelType0Type,
    check_batch_names_response_200_data_item_type_0_name_label_type_0_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchNamesResponse200DataItemType0NameLabelType0")


@_attrs_define
class BatchNamesResponse200DataItemType0NameLabelType0:
    """Keyed. What the name is; null when the name has no reading yet.

    Attributes:
        type_ (BatchNamesResponse200DataItemType0NameLabelType0Type | Unset):
        base_words (list[str] | Unset):
    """

    type_: BatchNamesResponse200DataItemType0NameLabelType0Type | Unset = UNSET
    base_words: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        base_words: list[str] | Unset = UNSET
        if not isinstance(self.base_words, Unset):
            base_words = self.base_words

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if base_words is not UNSET:
            field_dict["baseWords"] = base_words

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: BatchNamesResponse200DataItemType0NameLabelType0Type | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = (
                check_batch_names_response_200_data_item_type_0_name_label_type_0_type(
                    _type_
                )
            )

        base_words = cast(list[str], d.pop("baseWords", UNSET))

        batch_names_response_200_data_item_type_0_name_label_type_0 = cls(
            type_=type_,
            base_words=base_words,
        )

        batch_names_response_200_data_item_type_0_name_label_type_0.additional_properties = d
        return batch_names_response_200_data_item_type_0_name_label_type_0

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
