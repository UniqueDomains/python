from typing import Literal

GetTrendResponse200DataObservationsItemGrowthWindowType2Type1 = Literal[
    "1y", "3m", "5y", "6m"
]

GET_TREND_RESPONSE_200_DATA_OBSERVATIONS_ITEM_GROWTH_WINDOW_TYPE_2_TYPE_1_VALUES: set[
    GetTrendResponse200DataObservationsItemGrowthWindowType2Type1
] = {
    "1y",
    "3m",
    "5y",
    "6m",
}


def check_get_trend_response_200_data_observations_item_growth_window_type_2_type_1(
    value: str,
) -> GetTrendResponse200DataObservationsItemGrowthWindowType2Type1:
    if (
        value
        in GET_TREND_RESPONSE_200_DATA_OBSERVATIONS_ITEM_GROWTH_WINDOW_TYPE_2_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TREND_RESPONSE_200_DATA_OBSERVATIONS_ITEM_GROWTH_WINDOW_TYPE_2_TYPE_1_VALUES!r}"
    )
