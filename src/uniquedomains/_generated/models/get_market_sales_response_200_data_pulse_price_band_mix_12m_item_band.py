from typing import Literal

GetMarketSalesResponse200DataPulsePriceBandMix12MItemBand = Literal[
    "100000_up", "1000_4999", "25000_99999", "5000_24999", "50_999"
]

GET_MARKET_SALES_RESPONSE_200_DATA_PULSE_PRICE_BAND_MIX_12M_ITEM_BAND_VALUES: set[
    GetMarketSalesResponse200DataPulsePriceBandMix12MItemBand
] = {
    "100000_up",
    "1000_4999",
    "25000_99999",
    "5000_24999",
    "50_999",
}


def check_get_market_sales_response_200_data_pulse_price_band_mix_12m_item_band(
    value: str,
) -> GetMarketSalesResponse200DataPulsePriceBandMix12MItemBand:
    if (
        value
        in GET_MARKET_SALES_RESPONSE_200_DATA_PULSE_PRICE_BAND_MIX_12M_ITEM_BAND_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_MARKET_SALES_RESPONSE_200_DATA_PULSE_PRICE_BAND_MIX_12M_ITEM_BAND_VALUES!r}"
    )
