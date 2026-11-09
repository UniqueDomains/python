from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_trend_pool_response_200_data_item_observations_item import (
        ListTrendPoolResponse200DataItemObservationsItem,
    )


T = TypeVar("T", bound="ListTrendPoolResponse200DataItem")


@_attrs_define
class ListTrendPoolResponse200DataItem:
    """
    Attributes:
        canonical (str):
        definition (None | str):
        head_words (list[str]):
        seed_words (list[str]):
        open_names_founder (int | None):
        open_names_investor (int | None):
        observations (list[ListTrendPoolResponse200DataItemObservationsItem]):
    """

    canonical: str
    definition: None | str
    head_words: list[str]
    seed_words: list[str]
    open_names_founder: int | None
    open_names_investor: int | None
    observations: list[ListTrendPoolResponse200DataItemObservationsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        canonical = self.canonical

        definition: None | str
        definition = self.definition

        head_words = self.head_words

        seed_words = self.seed_words

        open_names_founder: int | None
        open_names_founder = self.open_names_founder

        open_names_investor: int | None
        open_names_investor = self.open_names_investor

        observations = []
        for observations_item_data in self.observations:
            observations_item = observations_item_data.to_dict()
            observations.append(observations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "canonical": canonical,
                "definition": definition,
                "headWords": head_words,
                "seedWords": seed_words,
                "openNamesFounder": open_names_founder,
                "openNamesInvestor": open_names_investor,
                "observations": observations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_trend_pool_response_200_data_item_observations_item import (
            ListTrendPoolResponse200DataItemObservationsItem,
        )

        d = dict(src_dict)
        canonical = d.pop("canonical")

        def _parse_definition(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        definition = _parse_definition(d.pop("definition"))

        head_words = cast(list[str], d.pop("headWords"))

        seed_words = cast(list[str], d.pop("seedWords"))

        def _parse_open_names_founder(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        open_names_founder = _parse_open_names_founder(d.pop("openNamesFounder"))

        def _parse_open_names_investor(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        open_names_investor = _parse_open_names_investor(d.pop("openNamesInvestor"))

        observations = []
        _observations = d.pop("observations")
        for observations_item_data in _observations:
            observations_item = (
                ListTrendPoolResponse200DataItemObservationsItem.from_dict(
                    observations_item_data
                )
            )

            observations.append(observations_item)

        list_trend_pool_response_200_data_item = cls(
            canonical=canonical,
            definition=definition,
            head_words=head_words,
            seed_words=seed_words,
            open_names_founder=open_names_founder,
            open_names_investor=open_names_investor,
            observations=observations,
        )

        list_trend_pool_response_200_data_item.additional_properties = d
        return list_trend_pool_response_200_data_item

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
