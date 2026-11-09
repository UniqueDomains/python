from typing import Literal

GetMarketSalesLengthsResponse200DataIoItemTrendWord = Literal[
    "down", "flat", "new", "up"
]

GET_MARKET_SALES_LENGTHS_RESPONSE_200_DATA_IO_ITEM_TREND_WORD_VALUES: set[
    GetMarketSalesLengthsResponse200DataIoItemTrendWord
] = {
    "down",
    "flat",
    "new",
    "up",
}


def check_get_market_sales_lengths_response_200_data_io_item_trend_word(
    value: str,
) -> GetMarketSalesLengthsResponse200DataIoItemTrendWord:
    if value in GET_MARKET_SALES_LENGTHS_RESPONSE_200_DATA_IO_ITEM_TREND_WORD_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_MARKET_SALES_LENGTHS_RESPONSE_200_DATA_IO_ITEM_TREND_WORD_VALUES!r}"
    )
