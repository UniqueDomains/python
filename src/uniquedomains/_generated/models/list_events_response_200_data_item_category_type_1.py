from typing import Literal

ListEventsResponse200DataItemCategoryType1 = Literal[
    "brand_ip",
    "dns_governance",
    "domaining",
    "hosting_cloud",
    "other_tech",
    "security_privacy",
]

LIST_EVENTS_RESPONSE_200_DATA_ITEM_CATEGORY_TYPE_1_VALUES: set[
    ListEventsResponse200DataItemCategoryType1
] = {
    "brand_ip",
    "dns_governance",
    "domaining",
    "hosting_cloud",
    "other_tech",
    "security_privacy",
}


def check_list_events_response_200_data_item_category_type_1(
    value: str,
) -> ListEventsResponse200DataItemCategoryType1:
    if value in LIST_EVENTS_RESPONSE_200_DATA_ITEM_CATEGORY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_EVENTS_RESPONSE_200_DATA_ITEM_CATEGORY_TYPE_1_VALUES!r}"
    )
