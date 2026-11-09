from typing import Literal

GetTrendResponse200DataEditionsItemPersona = Literal["founder", "investor"]

GET_TREND_RESPONSE_200_DATA_EDITIONS_ITEM_PERSONA_VALUES: set[
    GetTrendResponse200DataEditionsItemPersona
] = {
    "founder",
    "investor",
}


def check_get_trend_response_200_data_editions_item_persona(
    value: str,
) -> GetTrendResponse200DataEditionsItemPersona:
    if value in GET_TREND_RESPONSE_200_DATA_EDITIONS_ITEM_PERSONA_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TREND_RESPONSE_200_DATA_EDITIONS_ITEM_PERSONA_VALUES!r}"
    )
