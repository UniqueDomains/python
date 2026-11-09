from typing import Literal

GetWordTrademarksStatus = Literal["dead", "live"]

GET_WORD_TRADEMARKS_STATUS_VALUES: set[GetWordTrademarksStatus] = {
    "dead",
    "live",
}


def check_get_word_trademarks_status(value: str) -> GetWordTrademarksStatus:
    if value in GET_WORD_TRADEMARKS_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WORD_TRADEMARKS_STATUS_VALUES!r}"
    )
