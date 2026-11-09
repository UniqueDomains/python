from typing import Literal

ListTldChangesResponse200DataItemKind = Literal[
    "contract_termination", "delegation", "phase_added", "phase_moved", "removal"
]

LIST_TLD_CHANGES_RESPONSE_200_DATA_ITEM_KIND_VALUES: set[
    ListTldChangesResponse200DataItemKind
] = {
    "contract_termination",
    "delegation",
    "phase_added",
    "phase_moved",
    "removal",
}


def check_list_tld_changes_response_200_data_item_kind(
    value: str,
) -> ListTldChangesResponse200DataItemKind:
    if value in LIST_TLD_CHANGES_RESPONSE_200_DATA_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLD_CHANGES_RESPONSE_200_DATA_ITEM_KIND_VALUES!r}"
    )
