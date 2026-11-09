from typing import Literal

ListIanaRegistrarsResponse200DataItemStatus = Literal[
    "accredited", "reserved", "terminated"
]

LIST_IANA_REGISTRARS_RESPONSE_200_DATA_ITEM_STATUS_VALUES: set[
    ListIanaRegistrarsResponse200DataItemStatus
] = {
    "accredited",
    "reserved",
    "terminated",
}


def check_list_iana_registrars_response_200_data_item_status(
    value: str,
) -> ListIanaRegistrarsResponse200DataItemStatus:
    if value in LIST_IANA_REGISTRARS_RESPONSE_200_DATA_ITEM_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_IANA_REGISTRARS_RESPONSE_200_DATA_ITEM_STATUS_VALUES!r}"
    )
