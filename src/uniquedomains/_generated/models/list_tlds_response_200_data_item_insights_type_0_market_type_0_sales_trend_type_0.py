from typing import Literal

ListTldsResponse200DataItemInsightsType0MarketType0SalesTrendType0 = Literal[
    "down", "flat", "up"
]

LIST_TLDS_RESPONSE_200_DATA_ITEM_INSIGHTS_TYPE_0_MARKET_TYPE_0_SALES_TREND_TYPE_0_VALUES: set[
    ListTldsResponse200DataItemInsightsType0MarketType0SalesTrendType0
] = {
    "down",
    "flat",
    "up",
}


def check_list_tlds_response_200_data_item_insights_type_0_market_type_0_sales_trend_type_0(
    value: str,
) -> ListTldsResponse200DataItemInsightsType0MarketType0SalesTrendType0:
    if (
        value
        in LIST_TLDS_RESPONSE_200_DATA_ITEM_INSIGHTS_TYPE_0_MARKET_TYPE_0_SALES_TREND_TYPE_0_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLDS_RESPONSE_200_DATA_ITEM_INSIGHTS_TYPE_0_MARKET_TYPE_0_SALES_TREND_TYPE_0_VALUES!r}"
    )
