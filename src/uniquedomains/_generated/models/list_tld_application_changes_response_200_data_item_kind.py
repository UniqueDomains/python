from typing import Literal

ListTldApplicationChangesResponse200DataItemKind = Literal["contention_set", "status"]

LIST_TLD_APPLICATION_CHANGES_RESPONSE_200_DATA_ITEM_KIND_VALUES: set[
    ListTldApplicationChangesResponse200DataItemKind
] = {
    "contention_set",
    "status",
}


def check_list_tld_application_changes_response_200_data_item_kind(
    value: str,
) -> ListTldApplicationChangesResponse200DataItemKind:
    if value in LIST_TLD_APPLICATION_CHANGES_RESPONSE_200_DATA_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLD_APPLICATION_CHANGES_RESPONSE_200_DATA_ITEM_KIND_VALUES!r}"
    )
