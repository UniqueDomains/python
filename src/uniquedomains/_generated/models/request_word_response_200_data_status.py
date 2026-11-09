from typing import Literal

RequestWordResponse200DataStatus = Literal["accepted", "in_catalog", "queued"]

REQUEST_WORD_RESPONSE_200_DATA_STATUS_VALUES: set[RequestWordResponse200DataStatus] = {
    "accepted",
    "in_catalog",
    "queued",
}


def check_request_word_response_200_data_status(
    value: str,
) -> RequestWordResponse200DataStatus:
    if value in REQUEST_WORD_RESPONSE_200_DATA_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REQUEST_WORD_RESPONSE_200_DATA_STATUS_VALUES!r}"
    )
