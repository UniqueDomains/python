from typing import Literal

GetTldApplicationStringResponse200DataApplicationsItemStatusKeyType0 = Literal[
    "early_warning",
    "initial_evaluation",
    "objection_filed",
    "other",
    "received",
    "withdrawn",
]

GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_APPLICATIONS_ITEM_STATUS_KEY_TYPE_0_VALUES: set[
    GetTldApplicationStringResponse200DataApplicationsItemStatusKeyType0
] = {
    "early_warning",
    "initial_evaluation",
    "objection_filed",
    "other",
    "received",
    "withdrawn",
}


def check_get_tld_application_string_response_200_data_applications_item_status_key_type_0(
    value: str,
) -> GetTldApplicationStringResponse200DataApplicationsItemStatusKeyType0:
    if (
        value
        in GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_APPLICATIONS_ITEM_STATUS_KEY_TYPE_0_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_APPLICATIONS_ITEM_STATUS_KEY_TYPE_0_VALUES!r}"
    )
