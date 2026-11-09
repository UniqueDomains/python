from typing import Literal

GetAgendaResponse200DataUndatedItemCategoryType1 = Literal[
    "brand_ip",
    "dns_governance",
    "domaining",
    "hosting_cloud",
    "launches",
    "other_tech",
    "security_privacy",
]

GET_AGENDA_RESPONSE_200_DATA_UNDATED_ITEM_CATEGORY_TYPE_1_VALUES: set[
    GetAgendaResponse200DataUndatedItemCategoryType1
] = {
    "brand_ip",
    "dns_governance",
    "domaining",
    "hosting_cloud",
    "launches",
    "other_tech",
    "security_privacy",
}


def check_get_agenda_response_200_data_undated_item_category_type_1(
    value: str,
) -> GetAgendaResponse200DataUndatedItemCategoryType1:
    if value in GET_AGENDA_RESPONSE_200_DATA_UNDATED_ITEM_CATEGORY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_AGENDA_RESPONSE_200_DATA_UNDATED_ITEM_CATEGORY_TYPE_1_VALUES!r}"
    )
