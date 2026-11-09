from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLatestEditionResponse200DataTrendsItemRowsItemIdeasItem")


@_attrs_define
class GetLatestEditionResponse200DataTrendsItemRowsItemIdeasItem:
    """
    Attributes:
        title (str | Unset):
        idea (str | Unset):
        problem (str | Unset):
        customer (str | Unset):
        value_prop (str | Unset):
        why_now (str | Unset):
        monetization (str | Unset):
        name_fit (str | Unset):
        checklist (list[str] | Unset):
    """

    title: str | Unset = UNSET
    idea: str | Unset = UNSET
    problem: str | Unset = UNSET
    customer: str | Unset = UNSET
    value_prop: str | Unset = UNSET
    why_now: str | Unset = UNSET
    monetization: str | Unset = UNSET
    name_fit: str | Unset = UNSET
    checklist: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        idea = self.idea

        problem = self.problem

        customer = self.customer

        value_prop = self.value_prop

        why_now = self.why_now

        monetization = self.monetization

        name_fit = self.name_fit

        checklist: list[str] | Unset = UNSET
        if not isinstance(self.checklist, Unset):
            checklist = self.checklist

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if idea is not UNSET:
            field_dict["idea"] = idea
        if problem is not UNSET:
            field_dict["problem"] = problem
        if customer is not UNSET:
            field_dict["customer"] = customer
        if value_prop is not UNSET:
            field_dict["valueProp"] = value_prop
        if why_now is not UNSET:
            field_dict["whyNow"] = why_now
        if monetization is not UNSET:
            field_dict["monetization"] = monetization
        if name_fit is not UNSET:
            field_dict["nameFit"] = name_fit
        if checklist is not UNSET:
            field_dict["checklist"] = checklist

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        idea = d.pop("idea", UNSET)

        problem = d.pop("problem", UNSET)

        customer = d.pop("customer", UNSET)

        value_prop = d.pop("valueProp", UNSET)

        why_now = d.pop("whyNow", UNSET)

        monetization = d.pop("monetization", UNSET)

        name_fit = d.pop("nameFit", UNSET)

        checklist = cast(list[str], d.pop("checklist", UNSET))

        get_latest_edition_response_200_data_trends_item_rows_item_ideas_item = cls(
            title=title,
            idea=idea,
            problem=problem,
            customer=customer,
            value_prop=value_prop,
            why_now=why_now,
            monetization=monetization,
            name_fit=name_fit,
            checklist=checklist,
        )

        get_latest_edition_response_200_data_trends_item_rows_item_ideas_item.additional_properties = d
        return get_latest_edition_response_200_data_trends_item_rows_item_ideas_item

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
