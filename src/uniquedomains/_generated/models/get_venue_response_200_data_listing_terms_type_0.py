from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetVenueResponse200DataListingTermsType0")


@_attrs_define
class GetVenueResponse200DataListingTermsType0:
    """The verified listing terms: commission bands, exclusivity, payment plans, fast transfer and payout days.

    Attributes:
        checked_on (datetime.date | Unset): UTC day the terms were verified.
    """

    checked_on: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checked_on: str | Unset = UNSET
        if not isinstance(self.checked_on, Unset):
            checked_on = self.checked_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checked_on is not UNSET:
            field_dict["checkedOn"] = checked_on

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _checked_on = d.pop("checkedOn", UNSET)
        checked_on: datetime.date | Unset
        if isinstance(_checked_on, Unset):
            checked_on = UNSET
        else:
            checked_on = datetime.date.fromisoformat(_checked_on)

        get_venue_response_200_data_listing_terms_type_0 = cls(
            checked_on=checked_on,
        )

        get_venue_response_200_data_listing_terms_type_0.additional_properties = d
        return get_venue_response_200_data_listing_terms_type_0

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
