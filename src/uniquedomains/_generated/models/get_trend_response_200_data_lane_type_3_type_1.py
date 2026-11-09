from typing import Literal

GetTrendResponse200DataLaneType3Type1 = Literal["weekly", "yearly"]

GET_TREND_RESPONSE_200_DATA_LANE_TYPE_3_TYPE_1_VALUES: set[
    GetTrendResponse200DataLaneType3Type1
] = {
    "weekly",
    "yearly",
}


def check_get_trend_response_200_data_lane_type_3_type_1(
    value: str,
) -> GetTrendResponse200DataLaneType3Type1:
    if value in GET_TREND_RESPONSE_200_DATA_LANE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TREND_RESPONSE_200_DATA_LANE_TYPE_3_TYPE_1_VALUES!r}"
    )
