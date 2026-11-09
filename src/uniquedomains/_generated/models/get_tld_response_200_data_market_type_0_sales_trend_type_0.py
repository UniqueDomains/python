from typing import Literal

GetTldResponse200DataMarketType0SalesTrendType0 = Literal["down", "flat", "up"]

GET_TLD_RESPONSE_200_DATA_MARKET_TYPE_0_SALES_TREND_TYPE_0_VALUES: set[
    GetTldResponse200DataMarketType0SalesTrendType0
] = {
    "down",
    "flat",
    "up",
}


def check_get_tld_response_200_data_market_type_0_sales_trend_type_0(
    value: str,
) -> GetTldResponse200DataMarketType0SalesTrendType0:
    if value in GET_TLD_RESPONSE_200_DATA_MARKET_TYPE_0_SALES_TREND_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TLD_RESPONSE_200_DATA_MARKET_TYPE_0_SALES_TREND_TYPE_0_VALUES!r}"
    )
