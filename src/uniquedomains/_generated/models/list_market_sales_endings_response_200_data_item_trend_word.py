from typing import Literal

ListMarketSalesEndingsResponse200DataItemTrendWord = Literal[
    "down", "flat", "new", "up"
]

LIST_MARKET_SALES_ENDINGS_RESPONSE_200_DATA_ITEM_TREND_WORD_VALUES: set[
    ListMarketSalesEndingsResponse200DataItemTrendWord
] = {
    "down",
    "flat",
    "new",
    "up",
}


def check_list_market_sales_endings_response_200_data_item_trend_word(
    value: str,
) -> ListMarketSalesEndingsResponse200DataItemTrendWord:
    if value in LIST_MARKET_SALES_ENDINGS_RESPONSE_200_DATA_ITEM_TREND_WORD_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MARKET_SALES_ENDINGS_RESPONSE_200_DATA_ITEM_TREND_WORD_VALUES!r}"
    )
