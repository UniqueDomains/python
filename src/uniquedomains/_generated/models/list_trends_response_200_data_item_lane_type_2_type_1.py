from typing import Literal

ListTrendsResponse200DataItemLaneType2Type1 = Literal["weekly", "yearly"]

LIST_TRENDS_RESPONSE_200_DATA_ITEM_LANE_TYPE_2_TYPE_1_VALUES: set[
    ListTrendsResponse200DataItemLaneType2Type1
] = {
    "weekly",
    "yearly",
}


def check_list_trends_response_200_data_item_lane_type_2_type_1(
    value: str,
) -> ListTrendsResponse200DataItemLaneType2Type1:
    if value in LIST_TRENDS_RESPONSE_200_DATA_ITEM_LANE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TRENDS_RESPONSE_200_DATA_ITEM_LANE_TYPE_2_TYPE_1_VALUES!r}"
    )
