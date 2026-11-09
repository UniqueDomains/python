from typing import Literal

GetTldStatsResponse200DataSalesTrendType0 = Literal["down", "flat", "up"]

GET_TLD_STATS_RESPONSE_200_DATA_SALES_TREND_TYPE_0_VALUES: set[
    GetTldStatsResponse200DataSalesTrendType0
] = {
    "down",
    "flat",
    "up",
}


def check_get_tld_stats_response_200_data_sales_trend_type_0(
    value: str,
) -> GetTldStatsResponse200DataSalesTrendType0:
    if value in GET_TLD_STATS_RESPONSE_200_DATA_SALES_TREND_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TLD_STATS_RESPONSE_200_DATA_SALES_TREND_TYPE_0_VALUES!r}"
    )
