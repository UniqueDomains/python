from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_meta_trademark_classes_response_200_data_item_kind import (
    ListMetaTrademarkClassesResponse200DataItemKind,
    check_list_meta_trademark_classes_response_200_data_item_kind,
)

T = TypeVar("T", bound="ListMetaTrademarkClassesResponse200DataItem")


@_attrs_define
class ListMetaTrademarkClassesResponse200DataItem:
    """
    Attributes:
        class_ (int):
        title (str):
        kind (ListMetaTrademarkClassesResponse200DataItemKind):
    """

    class_: int
    title: str
    kind: ListMetaTrademarkClassesResponse200DataItemKind
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_ = self.class_

        title = self.title

        kind: str = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "class": class_,
                "title": title,
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        class_ = d.pop("class")

        title = d.pop("title")

        kind = check_list_meta_trademark_classes_response_200_data_item_kind(
            d.pop("kind")
        )

        list_meta_trademark_classes_response_200_data_item = cls(
            class_=class_,
            title=title,
            kind=kind,
        )

        list_meta_trademark_classes_response_200_data_item.additional_properties = d
        return list_meta_trademark_classes_response_200_data_item

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
