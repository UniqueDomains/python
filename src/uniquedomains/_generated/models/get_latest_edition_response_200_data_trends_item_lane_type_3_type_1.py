from typing import Literal

GetLatestEditionResponse200DataTrendsItemLaneType3Type1 = Literal["weekly", "yearly"]

GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_LANE_TYPE_3_TYPE_1_VALUES: set[
    GetLatestEditionResponse200DataTrendsItemLaneType3Type1
] = {
    "weekly",
    "yearly",
}


def check_get_latest_edition_response_200_data_trends_item_lane_type_3_type_1(
    value: str,
) -> GetLatestEditionResponse200DataTrendsItemLaneType3Type1:
    if (
        value
        in GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_LANE_TYPE_3_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_LANE_TYPE_3_TYPE_1_VALUES!r}"
    )
