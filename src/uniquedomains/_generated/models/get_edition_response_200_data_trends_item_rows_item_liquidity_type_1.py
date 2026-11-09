from typing import Literal

GetEditionResponse200DataTrendsItemRowsItemLiquidityType1 = Literal[
    "high", "low", "medium"
]

GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_LIQUIDITY_TYPE_1_VALUES: set[
    GetEditionResponse200DataTrendsItemRowsItemLiquidityType1
] = {
    "high",
    "low",
    "medium",
}


def check_get_edition_response_200_data_trends_item_rows_item_liquidity_type_1(
    value: str,
) -> GetEditionResponse200DataTrendsItemRowsItemLiquidityType1:
    if (
        value
        in GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_LIQUIDITY_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_LIQUIDITY_TYPE_1_VALUES!r}"
    )
