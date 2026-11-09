from typing import Literal

RequestWordResponse200DataWordOrigin = Literal["api", "dictionary", "review", "trend"]

REQUEST_WORD_RESPONSE_200_DATA_WORD_ORIGIN_VALUES: set[
    RequestWordResponse200DataWordOrigin
] = {
    "api",
    "dictionary",
    "review",
    "trend",
}


def check_request_word_response_200_data_word_origin(
    value: str,
) -> RequestWordResponse200DataWordOrigin:
    if value in REQUEST_WORD_RESPONSE_200_DATA_WORD_ORIGIN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REQUEST_WORD_RESPONSE_200_DATA_WORD_ORIGIN_VALUES!r}"
    )
