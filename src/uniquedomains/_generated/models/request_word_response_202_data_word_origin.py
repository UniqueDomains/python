from typing import Literal

RequestWordResponse202DataWordOrigin = Literal["api", "dictionary", "review", "trend"]

REQUEST_WORD_RESPONSE_202_DATA_WORD_ORIGIN_VALUES: set[
    RequestWordResponse202DataWordOrigin
] = {
    "api",
    "dictionary",
    "review",
    "trend",
}


def check_request_word_response_202_data_word_origin(
    value: str,
) -> RequestWordResponse202DataWordOrigin:
    if value in REQUEST_WORD_RESPONSE_202_DATA_WORD_ORIGIN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REQUEST_WORD_RESPONSE_202_DATA_WORD_ORIGIN_VALUES!r}"
    )
