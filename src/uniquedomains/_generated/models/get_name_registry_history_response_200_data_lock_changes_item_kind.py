from typing import Literal

GetNameRegistryHistoryResponse200DataLockChangesItemKind = Literal["lock_removed"]

GET_NAME_REGISTRY_HISTORY_RESPONSE_200_DATA_LOCK_CHANGES_ITEM_KIND_VALUES: set[
    GetNameRegistryHistoryResponse200DataLockChangesItemKind
] = {
    "lock_removed",
}


def check_get_name_registry_history_response_200_data_lock_changes_item_kind(
    value: str,
) -> GetNameRegistryHistoryResponse200DataLockChangesItemKind:
    if (
        value
        in GET_NAME_REGISTRY_HISTORY_RESPONSE_200_DATA_LOCK_CHANGES_ITEM_KIND_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_NAME_REGISTRY_HISTORY_RESPONSE_200_DATA_LOCK_CHANGES_ITEM_KIND_VALUES!r}"
    )
