from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_domain_drops_response_200_data_type_0_by_ending_item import (
        GetDomainDropsResponse200DataType0ByEndingItem,
    )
    from ..models.get_domain_drops_response_200_data_type_0_sample_item import (
        GetDomainDropsResponse200DataType0SampleItem,
    )


T = TypeVar("T", bound="GetDomainDropsResponse200DataType0")


@_attrs_define
class GetDomainDropsResponse200DataType0:
    """
    Attributes:
        count (int | Unset):
        by_ending (list[GetDomainDropsResponse200DataType0ByEndingItem] | Unset):
        sample (list[GetDomainDropsResponse200DataType0SampleItem] | Unset):
    """

    count: int | Unset = UNSET
    by_ending: list[GetDomainDropsResponse200DataType0ByEndingItem] | Unset = UNSET
    sample: list[GetDomainDropsResponse200DataType0SampleItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        by_ending: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_ending, Unset):
            by_ending = []
            for by_ending_item_data in self.by_ending:
                by_ending_item = by_ending_item_data.to_dict()
                by_ending.append(by_ending_item)

        sample: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sample, Unset):
            sample = []
            for sample_item_data in self.sample:
                sample_item = sample_item_data.to_dict()
                sample.append(sample_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if by_ending is not UNSET:
            field_dict["byEnding"] = by_ending
        if sample is not UNSET:
            field_dict["sample"] = sample

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_domain_drops_response_200_data_type_0_by_ending_item import (
            GetDomainDropsResponse200DataType0ByEndingItem,
        )
        from ..models.get_domain_drops_response_200_data_type_0_sample_item import (
            GetDomainDropsResponse200DataType0SampleItem,
        )

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        _by_ending = d.pop("byEnding", UNSET)
        by_ending: list[GetDomainDropsResponse200DataType0ByEndingItem] | Unset = UNSET
        if _by_ending is not UNSET:
            by_ending = []
            for by_ending_item_data in _by_ending:
                by_ending_item = (
                    GetDomainDropsResponse200DataType0ByEndingItem.from_dict(
                        by_ending_item_data
                    )
                )

                by_ending.append(by_ending_item)

        _sample = d.pop("sample", UNSET)
        sample: list[GetDomainDropsResponse200DataType0SampleItem] | Unset = UNSET
        if _sample is not UNSET:
            sample = []
            for sample_item_data in _sample:
                sample_item = GetDomainDropsResponse200DataType0SampleItem.from_dict(
                    sample_item_data
                )

                sample.append(sample_item)

        get_domain_drops_response_200_data_type_0 = cls(
            count=count,
            by_ending=by_ending,
            sample=sample,
        )

        get_domain_drops_response_200_data_type_0.additional_properties = d
        return get_domain_drops_response_200_data_type_0

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
