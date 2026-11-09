from typing import Literal

GetWordResponse200DataOrigin = Literal["api", "dictionary", "review", "trend"]

GET_WORD_RESPONSE_200_DATA_ORIGIN_VALUES: set[GetWordResponse200DataOrigin] = {
    "api",
    "dictionary",
    "review",
    "trend",
}


def check_get_word_response_200_data_origin(value: str) -> GetWordResponse200DataOrigin:
    if value in GET_WORD_RESPONSE_200_DATA_ORIGIN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WORD_RESPONSE_200_DATA_ORIGIN_VALUES!r}"
    )
