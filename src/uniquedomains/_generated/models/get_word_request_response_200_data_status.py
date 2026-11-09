from typing import Literal

GetWordRequestResponse200DataStatus = Literal["failed", "queued", "ready", "rejected"]

GET_WORD_REQUEST_RESPONSE_200_DATA_STATUS_VALUES: set[
    GetWordRequestResponse200DataStatus
] = {
    "failed",
    "queued",
    "ready",
    "rejected",
}


def check_get_word_request_response_200_data_status(
    value: str,
) -> GetWordRequestResponse200DataStatus:
    if value in GET_WORD_REQUEST_RESPONSE_200_DATA_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WORD_REQUEST_RESPONSE_200_DATA_STATUS_VALUES!r}"
    )
