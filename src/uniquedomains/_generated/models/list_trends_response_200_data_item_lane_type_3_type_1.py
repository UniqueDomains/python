from typing import Literal

ListTrendsResponse200DataItemLaneType3Type1 = Literal["weekly", "yearly"]

LIST_TRENDS_RESPONSE_200_DATA_ITEM_LANE_TYPE_3_TYPE_1_VALUES: set[
    ListTrendsResponse200DataItemLaneType3Type1
] = {
    "weekly",
    "yearly",
}


def check_list_trends_response_200_data_item_lane_type_3_type_1(
    value: str,
) -> ListTrendsResponse200DataItemLaneType3Type1:
    if value in LIST_TRENDS_RESPONSE_200_DATA_ITEM_LANE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TRENDS_RESPONSE_200_DATA_ITEM_LANE_TYPE_3_TYPE_1_VALUES!r}"
    )
