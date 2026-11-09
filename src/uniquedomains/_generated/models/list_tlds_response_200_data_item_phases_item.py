from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_tlds_response_200_data_item_phases_item_phase import (
    ListTldsResponse200DataItemPhasesItemPhase,
    check_list_tlds_response_200_data_item_phases_item_phase,
)

T = TypeVar("T", bound="ListTldsResponse200DataItemPhasesItem")


@_attrs_define
class ListTldsResponse200DataItemPhasesItem:
    """
    Attributes:
        id (str): `TldLaunchPhase.id`.
        phase (ListTldsResponse200DataItemPhasesItemPhase):
        starts_on (datetime.date): First day.
        ends_on (datetime.date | None):
        program_label (None | str):
    """

    id: str
    phase: ListTldsResponse200DataItemPhasesItemPhase
    starts_on: datetime.date
    ends_on: datetime.date | None
    program_label: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        phase: str = self.phase

        starts_on = self.starts_on.isoformat()

        ends_on: None | str
        if isinstance(self.ends_on, datetime.date):
            ends_on = self.ends_on.isoformat()
        else:
            ends_on = self.ends_on

        program_label: None | str
        program_label = self.program_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "phase": phase,
                "startsOn": starts_on,
                "endsOn": ends_on,
                "programLabel": program_label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        phase = check_list_tlds_response_200_data_item_phases_item_phase(d.pop("phase"))

        starts_on = datetime.date.fromisoformat(d.pop("startsOn"))

        def _parse_ends_on(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ends_on_type_0 = datetime.date.fromisoformat(data)

                return ends_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        ends_on = _parse_ends_on(d.pop("endsOn"))

        def _parse_program_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        program_label = _parse_program_label(d.pop("programLabel"))

        list_tlds_response_200_data_item_phases_item = cls(
            id=id,
            phase=phase,
            starts_on=starts_on,
            ends_on=ends_on,
            program_label=program_label,
        )

        list_tlds_response_200_data_item_phases_item.additional_properties = d
        return list_tlds_response_200_data_item_phases_item

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
