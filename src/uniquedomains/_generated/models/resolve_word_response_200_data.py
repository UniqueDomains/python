from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resolve_word_response_200_data_candidates_item import (
        ResolveWordResponse200DataCandidatesItem,
    )
    from ..models.resolve_word_response_200_data_match import (
        ResolveWordResponse200DataMatch,
    )


T = TypeVar("T", bound="ResolveWordResponse200Data")


@_attrs_define
class ResolveWordResponse200Data:
    """
    Attributes:
        match (ResolveWordResponse200DataMatch | Unset):
        candidates (list[ResolveWordResponse200DataCandidatesItem] | Unset):
    """

    match: ResolveWordResponse200DataMatch | Unset = UNSET
    candidates: list[ResolveWordResponse200DataCandidatesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.to_dict()

        candidates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.candidates, Unset):
            candidates = []
            for candidates_item_data in self.candidates:
                candidates_item = candidates_item_data.to_dict()
                candidates.append(candidates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match is not UNSET:
            field_dict["match"] = match
        if candidates is not UNSET:
            field_dict["candidates"] = candidates

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.resolve_word_response_200_data_candidates_item import (
            ResolveWordResponse200DataCandidatesItem,
        )
        from ..models.resolve_word_response_200_data_match import (
            ResolveWordResponse200DataMatch,
        )

        d = dict(src_dict)
        _match = d.pop("match", UNSET)
        match: ResolveWordResponse200DataMatch | Unset
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = ResolveWordResponse200DataMatch.from_dict(_match)

        _candidates = d.pop("candidates", UNSET)
        candidates: list[ResolveWordResponse200DataCandidatesItem] | Unset = UNSET
        if _candidates is not UNSET:
            candidates = []
            for candidates_item_data in _candidates:
                candidates_item = ResolveWordResponse200DataCandidatesItem.from_dict(
                    candidates_item_data
                )

                candidates.append(candidates_item)

        resolve_word_response_200_data = cls(
            match=match,
            candidates=candidates,
        )

        resolve_word_response_200_data.additional_properties = d
        return resolve_word_response_200_data

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
