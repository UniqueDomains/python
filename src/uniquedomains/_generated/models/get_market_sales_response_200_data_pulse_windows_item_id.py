from typing import Literal

GetMarketSalesResponse200DataPulseWindowsItemId = Literal["12m", "30d", "7d"]

GET_MARKET_SALES_RESPONSE_200_DATA_PULSE_WINDOWS_ITEM_ID_VALUES: set[
    GetMarketSalesResponse200DataPulseWindowsItemId
] = {
    "12m",
    "30d",
    "7d",
}


def check_get_market_sales_response_200_data_pulse_windows_item_id(
    value: str,
) -> GetMarketSalesResponse200DataPulseWindowsItemId:
    if value in GET_MARKET_SALES_RESPONSE_200_DATA_PULSE_WINDOWS_ITEM_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_MARKET_SALES_RESPONSE_200_DATA_PULSE_WINDOWS_ITEM_ID_VALUES!r}"
    )
