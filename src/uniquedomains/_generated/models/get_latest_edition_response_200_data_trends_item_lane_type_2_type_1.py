from typing import Literal

GetLatestEditionResponse200DataTrendsItemLaneType2Type1 = Literal["weekly", "yearly"]

GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_LANE_TYPE_2_TYPE_1_VALUES: set[
    GetLatestEditionResponse200DataTrendsItemLaneType2Type1
] = {
    "weekly",
    "yearly",
}


def check_get_latest_edition_response_200_data_trends_item_lane_type_2_type_1(
    value: str,
) -> GetLatestEditionResponse200DataTrendsItemLaneType2Type1:
    if (
        value
        in GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_LANE_TYPE_2_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_LANE_TYPE_2_TYPE_1_VALUES!r}"
    )
