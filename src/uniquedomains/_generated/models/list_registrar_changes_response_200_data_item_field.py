from typing import Literal

ListRegistrarChangesResponse200DataItemField = Literal[
    "purchase", "renewal", "transfer"
]

LIST_REGISTRAR_CHANGES_RESPONSE_200_DATA_ITEM_FIELD_VALUES: set[
    ListRegistrarChangesResponse200DataItemField
] = {
    "purchase",
    "renewal",
    "transfer",
}


def check_list_registrar_changes_response_200_data_item_field(
    value: str,
) -> ListRegistrarChangesResponse200DataItemField:
    if value in LIST_REGISTRAR_CHANGES_RESPONSE_200_DATA_ITEM_FIELD_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_REGISTRAR_CHANGES_RESPONSE_200_DATA_ITEM_FIELD_VALUES!r}"
    )
