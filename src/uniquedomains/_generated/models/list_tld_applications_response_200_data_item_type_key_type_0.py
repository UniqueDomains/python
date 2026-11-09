from typing import Literal

ListTldApplicationsResponse200DataItemTypeKeyType0 = Literal[
    "brand", "community", "geographic", "other", "standard"
]

LIST_TLD_APPLICATIONS_RESPONSE_200_DATA_ITEM_TYPE_KEY_TYPE_0_VALUES: set[
    ListTldApplicationsResponse200DataItemTypeKeyType0
] = {
    "brand",
    "community",
    "geographic",
    "other",
    "standard",
}


def check_list_tld_applications_response_200_data_item_type_key_type_0(
    value: str,
) -> ListTldApplicationsResponse200DataItemTypeKeyType0:
    if value in LIST_TLD_APPLICATIONS_RESPONSE_200_DATA_ITEM_TYPE_KEY_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLD_APPLICATIONS_RESPONSE_200_DATA_ITEM_TYPE_KEY_TYPE_0_VALUES!r}"
    )
