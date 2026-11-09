from typing import Literal

GetTldStatsResponse200DataHistoryItemSalesTrendType0 = Literal["down", "flat", "up"]

GET_TLD_STATS_RESPONSE_200_DATA_HISTORY_ITEM_SALES_TREND_TYPE_0_VALUES: set[
    GetTldStatsResponse200DataHistoryItemSalesTrendType0
] = {
    "down",
    "flat",
    "up",
}


def check_get_tld_stats_response_200_data_history_item_sales_trend_type_0(
    value: str,
) -> GetTldStatsResponse200DataHistoryItemSalesTrendType0:
    if value in GET_TLD_STATS_RESPONSE_200_DATA_HISTORY_ITEM_SALES_TREND_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TLD_STATS_RESPONSE_200_DATA_HISTORY_ITEM_SALES_TREND_TYPE_0_VALUES!r}"
    )
