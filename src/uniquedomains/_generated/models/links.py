from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Links")


@_attrs_define
class Links:
    """
    Attributes:
        self_ (str):
        next_ (None | str):
        register (None | str):
        product (None | str):
        dataset (None | str):
    """

    self_: str
    next_: None | str
    register: None | str
    product: None | str
    dataset: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_

        next_: None | str
        next_ = self.next_

        register: None | str
        register = self.register

        product: None | str
        product = self.product

        dataset: None | str
        dataset = self.dataset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "next": next_,
                "register": register,
                "product": product,
                "dataset": dataset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        self_ = d.pop("self")

        def _parse_next_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_ = _parse_next_(d.pop("next"))

        def _parse_register(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        register = _parse_register(d.pop("register"))

        def _parse_product(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        product = _parse_product(d.pop("product"))

        def _parse_dataset(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        dataset = _parse_dataset(d.pop("dataset"))

        links = cls(
            self_=self_,
            next_=next_,
            register=register,
            product=product,
            dataset=dataset,
        )

        links.additional_properties = d
        return links

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
