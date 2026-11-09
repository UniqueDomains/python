from typing import Literal

GetMarketSalesWordResponse200DataStatus = Literal["none", "result"]

GET_MARKET_SALES_WORD_RESPONSE_200_DATA_STATUS_VALUES: set[
    GetMarketSalesWordResponse200DataStatus
] = {
    "none",
    "result",
}


def check_get_market_sales_word_response_200_data_status(
    value: str,
) -> GetMarketSalesWordResponse200DataStatus:
    if value in GET_MARKET_SALES_WORD_RESPONSE_200_DATA_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_MARKET_SALES_WORD_RESPONSE_200_DATA_STATUS_VALUES!r}"
    )
