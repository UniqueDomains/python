from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_word_fits_response_200_data_item_basis import (
    ListWordFitsResponse200DataItemBasis,
    check_list_word_fits_response_200_data_item_basis,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListWordFitsResponse200DataItem")


@_attrs_define
class ListWordFitsResponse200DataItem:
    """
    Attributes:
        ending (str | Unset):
        fit (int | Unset):
        basis (ListWordFitsResponse200DataItemBasis | Unset):
    """

    ending: str | Unset = UNSET
    fit: int | Unset = UNSET
    basis: ListWordFitsResponse200DataItemBasis | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ending = self.ending

        fit = self.fit

        basis: str | Unset = UNSET
        if not isinstance(self.basis, Unset):
            basis = self.basis

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ending is not UNSET:
            field_dict["ending"] = ending
        if fit is not UNSET:
            field_dict["fit"] = fit
        if basis is not UNSET:
            field_dict["basis"] = basis

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ending = d.pop("ending", UNSET)

        fit = d.pop("fit", UNSET)

        _basis = d.pop("basis", UNSET)
        basis: ListWordFitsResponse200DataItemBasis | Unset
        if isinstance(_basis, Unset):
            basis = UNSET
        else:
            basis = check_list_word_fits_response_200_data_item_basis(_basis)

        list_word_fits_response_200_data_item = cls(
            ending=ending,
            fit=fit,
            basis=basis,
        )

        list_word_fits_response_200_data_item.additional_properties = d
        return list_word_fits_response_200_data_item

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
