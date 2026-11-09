from typing import Literal

ListTldsResponse200DataItemIanaStatusType0 = Literal[
    "delegated", "never_delegated", "removed"
]

LIST_TLDS_RESPONSE_200_DATA_ITEM_IANA_STATUS_TYPE_0_VALUES: set[
    ListTldsResponse200DataItemIanaStatusType0
] = {
    "delegated",
    "never_delegated",
    "removed",
}


def check_list_tlds_response_200_data_item_iana_status_type_0(
    value: str,
) -> ListTldsResponse200DataItemIanaStatusType0:
    if value in LIST_TLDS_RESPONSE_200_DATA_ITEM_IANA_STATUS_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLDS_RESPONSE_200_DATA_ITEM_IANA_STATUS_TYPE_0_VALUES!r}"
    )
