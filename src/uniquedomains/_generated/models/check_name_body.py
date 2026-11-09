from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_name_body_blocks_item import (
    CheckNameBodyBlocksItem,
    check_check_name_body_blocks_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckNameBody")


@_attrs_define
class CheckNameBody:
    """
    Attributes:
        blocks (list[CheckNameBodyBlocksItem] | Unset):
    """

    blocks: list[CheckNameBodyBlocksItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blocks: list[str] | Unset = UNSET
        if not isinstance(self.blocks, Unset):
            blocks = []
            for blocks_item_data in self.blocks:
                blocks_item: str = blocks_item_data
                blocks.append(blocks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blocks is not UNSET:
            field_dict["blocks"] = blocks

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _blocks = d.pop("blocks", UNSET)
        blocks: list[CheckNameBodyBlocksItem] | Unset = UNSET
        if _blocks is not UNSET:
            blocks = []
            for blocks_item_data in _blocks:
                blocks_item = check_check_name_body_blocks_item(blocks_item_data)

                blocks.append(blocks_item)

        check_name_body = cls(
            blocks=blocks,
        )

        check_name_body.additional_properties = d
        return check_name_body

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
