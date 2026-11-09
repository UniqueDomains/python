from typing import Literal

GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType2Type1 = Literal[
    "high", "low", "medium"
]

GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_LIQUIDITY_TYPE_2_TYPE_1_VALUES: set[
    GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_get_latest_edition_response_200_data_trends_item_rows_item_liquidity_type_2_type_1(
    value: str,
) -> GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType2Type1:
    if (
        value
        in GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_LIQUIDITY_TYPE_2_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_LIQUIDITY_TYPE_2_TYPE_1_VALUES!r}"
    )
