from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_agenda_response_200_data_entries_item import (
        GetAgendaResponse200DataEntriesItem,
    )
    from ..models.get_agenda_response_200_data_recently_added_item import (
        GetAgendaResponse200DataRecentlyAddedItem,
    )
    from ..models.get_agenda_response_200_data_undated_item import (
        GetAgendaResponse200DataUndatedItem,
    )


T = TypeVar("T", bound="GetAgendaResponse200Data")


@_attrs_define
class GetAgendaResponse200Data:
    """
    Attributes:
        entries (list[GetAgendaResponse200DataEntriesItem]):
        recently_added (list[GetAgendaResponse200DataRecentlyAddedItem]):
        undated (list[GetAgendaResponse200DataUndatedItem]):
    """

    entries: list[GetAgendaResponse200DataEntriesItem]
    recently_added: list[GetAgendaResponse200DataRecentlyAddedItem]
    undated: list[GetAgendaResponse200DataUndatedItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        recently_added = []
        for recently_added_item_data in self.recently_added:
            recently_added_item = recently_added_item_data.to_dict()
            recently_added.append(recently_added_item)

        undated = []
        for undated_item_data in self.undated:
            undated_item = undated_item_data.to_dict()
            undated.append(undated_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entries": entries,
                "recentlyAdded": recently_added,
                "undated": undated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_agenda_response_200_data_entries_item import (
            GetAgendaResponse200DataEntriesItem,
        )
        from ..models.get_agenda_response_200_data_recently_added_item import (
            GetAgendaResponse200DataRecentlyAddedItem,
        )
        from ..models.get_agenda_response_200_data_undated_item import (
            GetAgendaResponse200DataUndatedItem,
        )

        d = dict(src_dict)
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = GetAgendaResponse200DataEntriesItem.from_dict(
                entries_item_data
            )

            entries.append(entries_item)

        recently_added = []
        _recently_added = d.pop("recentlyAdded")
        for recently_added_item_data in _recently_added:
            recently_added_item = GetAgendaResponse200DataRecentlyAddedItem.from_dict(
                recently_added_item_data
            )

            recently_added.append(recently_added_item)

        undated = []
        _undated = d.pop("undated")
        for undated_item_data in _undated:
            undated_item = GetAgendaResponse200DataUndatedItem.from_dict(
                undated_item_data
            )

            undated.append(undated_item)

        get_agenda_response_200_data = cls(
            entries=entries,
            recently_added=recently_added,
            undated=undated,
        )

        get_agenda_response_200_data.additional_properties = d
        return get_agenda_response_200_data

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
