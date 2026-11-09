from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_name_registry_history_response_200_data_lock_changes_item import (
        GetNameRegistryHistoryResponse200DataLockChangesItem,
    )
    from ..models.get_name_registry_history_response_200_data_moves_item import (
        GetNameRegistryHistoryResponse200DataMovesItem,
    )
    from ..models.get_name_registry_history_response_200_data_transfers_item import (
        GetNameRegistryHistoryResponse200DataTransfersItem,
    )
    from ..models.get_name_registry_history_response_200_data_versions_item import (
        GetNameRegistryHistoryResponse200DataVersionsItem,
    )


T = TypeVar("T", bound="GetNameRegistryHistoryResponse200Data")


@_attrs_define
class GetNameRegistryHistoryResponse200Data:
    """
    Attributes:
        versions (list[GetNameRegistryHistoryResponse200DataVersionsItem] | Unset):
        moves (list[GetNameRegistryHistoryResponse200DataMovesItem] | Unset):
        transfers (list[GetNameRegistryHistoryResponse200DataTransfersItem] | Unset):
        lock_changes (list[GetNameRegistryHistoryResponse200DataLockChangesItem] | Unset):
    """

    versions: list[GetNameRegistryHistoryResponse200DataVersionsItem] | Unset = UNSET
    moves: list[GetNameRegistryHistoryResponse200DataMovesItem] | Unset = UNSET
    transfers: list[GetNameRegistryHistoryResponse200DataTransfersItem] | Unset = UNSET
    lock_changes: list[GetNameRegistryHistoryResponse200DataLockChangesItem] | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        moves: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.moves, Unset):
            moves = []
            for moves_item_data in self.moves:
                moves_item = moves_item_data.to_dict()
                moves.append(moves_item)

        transfers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transfers, Unset):
            transfers = []
            for transfers_item_data in self.transfers:
                transfers_item = transfers_item_data.to_dict()
                transfers.append(transfers_item)

        lock_changes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lock_changes, Unset):
            lock_changes = []
            for lock_changes_item_data in self.lock_changes:
                lock_changes_item = lock_changes_item_data.to_dict()
                lock_changes.append(lock_changes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if versions is not UNSET:
            field_dict["versions"] = versions
        if moves is not UNSET:
            field_dict["moves"] = moves
        if transfers is not UNSET:
            field_dict["transfers"] = transfers
        if lock_changes is not UNSET:
            field_dict["lockChanges"] = lock_changes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_name_registry_history_response_200_data_lock_changes_item import (
            GetNameRegistryHistoryResponse200DataLockChangesItem,
        )
        from ..models.get_name_registry_history_response_200_data_moves_item import (
            GetNameRegistryHistoryResponse200DataMovesItem,
        )
        from ..models.get_name_registry_history_response_200_data_transfers_item import (
            GetNameRegistryHistoryResponse200DataTransfersItem,
        )
        from ..models.get_name_registry_history_response_200_data_versions_item import (
            GetNameRegistryHistoryResponse200DataVersionsItem,
        )

        d = dict(src_dict)
        _versions = d.pop("versions", UNSET)
        versions: list[GetNameRegistryHistoryResponse200DataVersionsItem] | Unset = (
            UNSET
        )
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = (
                    GetNameRegistryHistoryResponse200DataVersionsItem.from_dict(
                        versions_item_data
                    )
                )

                versions.append(versions_item)

        _moves = d.pop("moves", UNSET)
        moves: list[GetNameRegistryHistoryResponse200DataMovesItem] | Unset = UNSET
        if _moves is not UNSET:
            moves = []
            for moves_item_data in _moves:
                moves_item = GetNameRegistryHistoryResponse200DataMovesItem.from_dict(
                    moves_item_data
                )

                moves.append(moves_item)

        _transfers = d.pop("transfers", UNSET)
        transfers: list[GetNameRegistryHistoryResponse200DataTransfersItem] | Unset = (
            UNSET
        )
        if _transfers is not UNSET:
            transfers = []
            for transfers_item_data in _transfers:
                transfers_item = (
                    GetNameRegistryHistoryResponse200DataTransfersItem.from_dict(
                        transfers_item_data
                    )
                )

                transfers.append(transfers_item)

        _lock_changes = d.pop("lockChanges", UNSET)
        lock_changes: (
            list[GetNameRegistryHistoryResponse200DataLockChangesItem] | Unset
        ) = UNSET
        if _lock_changes is not UNSET:
            lock_changes = []
            for lock_changes_item_data in _lock_changes:
                lock_changes_item = (
                    GetNameRegistryHistoryResponse200DataLockChangesItem.from_dict(
                        lock_changes_item_data
                    )
                )

                lock_changes.append(lock_changes_item)

        get_name_registry_history_response_200_data = cls(
            versions=versions,
            moves=moves,
            transfers=transfers,
            lock_changes=lock_changes,
        )

        get_name_registry_history_response_200_data.additional_properties = d
        return get_name_registry_history_response_200_data

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
