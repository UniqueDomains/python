from typing import Literal

RequestWordResponse202DataStatus = Literal["accepted", "in_catalog", "queued"]

REQUEST_WORD_RESPONSE_202_DATA_STATUS_VALUES: set[RequestWordResponse202DataStatus] = {
    "accepted",
    "in_catalog",
    "queued",
}


def check_request_word_response_202_data_status(
    value: str,
) -> RequestWordResponse202DataStatus:
    if value in REQUEST_WORD_RESPONSE_202_DATA_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REQUEST_WORD_RESPONSE_202_DATA_STATUS_VALUES!r}"
    )
