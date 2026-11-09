from typing import Literal

GetEventResponse200DataCategoryType3Type1 = Literal[
    "brand_ip",
    "dns_governance",
    "domaining",
    "hosting_cloud",
    "other_tech",
    "security_privacy",
]

GET_EVENT_RESPONSE_200_DATA_CATEGORY_TYPE_3_TYPE_1_VALUES: set[
    GetEventResponse200DataCategoryType3Type1
] = {
    "brand_ip",
    "dns_governance",
    "domaining",
    "hosting_cloud",
    "other_tech",
    "security_privacy",
}


def check_get_event_response_200_data_category_type_3_type_1(
    value: str,
) -> GetEventResponse200DataCategoryType3Type1:
    if value in GET_EVENT_RESPONSE_200_DATA_CATEGORY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_EVENT_RESPONSE_200_DATA_CATEGORY_TYPE_3_TYPE_1_VALUES!r}"
    )
