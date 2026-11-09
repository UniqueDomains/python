from typing import Literal

GetWordRequestResponse200DataReason = Literal["brand", "not_a_word", "offensive"]

GET_WORD_REQUEST_RESPONSE_200_DATA_REASON_VALUES: set[
    GetWordRequestResponse200DataReason
] = {
    "brand",
    "not_a_word",
    "offensive",
}


def check_get_word_request_response_200_data_reason(
    value: str,
) -> GetWordRequestResponse200DataReason:
    if value in GET_WORD_REQUEST_RESPONSE_200_DATA_REASON_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WORD_REQUEST_RESPONSE_200_DATA_REASON_VALUES!r}"
    )
