from typing import Literal

ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType1 = Literal[
    "1y", "3m", "5y", "6m"
]

LIST_TREND_POOL_RESPONSE_200_DATA_ITEM_OBSERVATIONS_ITEM_GROWTH_WINDOW_TYPE_1_VALUES: set[
    ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType1
] = {
    "1y",
    "3m",
    "5y",
    "6m",
}


def check_list_trend_pool_response_200_data_item_observations_item_growth_window_type_1(
    value: str,
) -> ListTrendPoolResponse200DataItemObservationsItemGrowthWindowType1:
    if (
        value
        in LIST_TREND_POOL_RESPONSE_200_DATA_ITEM_OBSERVATIONS_ITEM_GROWTH_WINDOW_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TREND_POOL_RESPONSE_200_DATA_ITEM_OBSERVATIONS_ITEM_GROWTH_WINDOW_TYPE_1_VALUES!r}"
    )
