from typing import Literal

GetWordTrademarksOffice = Literal["EU", "US"]

GET_WORD_TRADEMARKS_OFFICE_VALUES: set[GetWordTrademarksOffice] = {
    "EU",
    "US",
}


def check_get_word_trademarks_office(value: str) -> GetWordTrademarksOffice:
    if value in GET_WORD_TRADEMARKS_OFFICE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WORD_TRADEMARKS_OFFICE_VALUES!r}"
    )
