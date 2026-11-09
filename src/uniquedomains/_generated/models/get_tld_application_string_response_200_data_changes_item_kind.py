from typing import Literal

GetTldApplicationStringResponse200DataChangesItemKind = Literal[
    "contention_set", "status"
]

GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_CHANGES_ITEM_KIND_VALUES: set[
    GetTldApplicationStringResponse200DataChangesItemKind
] = {
    "contention_set",
    "status",
}


def check_get_tld_application_string_response_200_data_changes_item_kind(
    value: str,
) -> GetTldApplicationStringResponse200DataChangesItemKind:
    if value in GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_CHANGES_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_CHANGES_ITEM_KIND_VALUES!r}"
    )
