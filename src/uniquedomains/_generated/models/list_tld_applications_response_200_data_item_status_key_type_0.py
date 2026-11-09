from typing import Literal

ListTldApplicationsResponse200DataItemStatusKeyType0 = Literal[
    "early_warning",
    "initial_evaluation",
    "objection_filed",
    "other",
    "received",
    "withdrawn",
]

LIST_TLD_APPLICATIONS_RESPONSE_200_DATA_ITEM_STATUS_KEY_TYPE_0_VALUES: set[
    ListTldApplicationsResponse200DataItemStatusKeyType0
] = {
    "early_warning",
    "initial_evaluation",
    "objection_filed",
    "other",
    "received",
    "withdrawn",
}


def check_list_tld_applications_response_200_data_item_status_key_type_0(
    value: str,
) -> ListTldApplicationsResponse200DataItemStatusKeyType0:
    if value in LIST_TLD_APPLICATIONS_RESPONSE_200_DATA_ITEM_STATUS_KEY_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLD_APPLICATIONS_RESPONSE_200_DATA_ITEM_STATUS_KEY_TYPE_0_VALUES!r}"
    )
