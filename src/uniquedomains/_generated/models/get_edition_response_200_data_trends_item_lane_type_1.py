from typing import Literal

GetEditionResponse200DataTrendsItemLaneType1 = Literal["weekly", "yearly"]

GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_LANE_TYPE_1_VALUES: set[
    GetEditionResponse200DataTrendsItemLaneType1
] = {
    "weekly",
    "yearly",
}


def check_get_edition_response_200_data_trends_item_lane_type_1(
    value: str,
) -> GetEditionResponse200DataTrendsItemLaneType1:
    if value in GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_LANE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_LANE_TYPE_1_VALUES!r}"
    )
