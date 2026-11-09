from typing import Literal

GetTldApplicationStringResponse200DataApplicationsItemTypeKeyType0 = Literal[
    "brand", "community", "geographic", "other", "standard"
]

GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_APPLICATIONS_ITEM_TYPE_KEY_TYPE_0_VALUES: set[
    GetTldApplicationStringResponse200DataApplicationsItemTypeKeyType0
] = {
    "brand",
    "community",
    "geographic",
    "other",
    "standard",
}


def check_get_tld_application_string_response_200_data_applications_item_type_key_type_0(
    value: str,
) -> GetTldApplicationStringResponse200DataApplicationsItemTypeKeyType0:
    if (
        value
        in GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_APPLICATIONS_ITEM_TYPE_KEY_TYPE_0_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_APPLICATIONS_ITEM_TYPE_KEY_TYPE_0_VALUES!r}"
    )
