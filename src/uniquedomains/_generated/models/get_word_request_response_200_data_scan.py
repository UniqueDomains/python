from typing import Literal

GetWordRequestResponse200DataScan = Literal["done", "pending"]

GET_WORD_REQUEST_RESPONSE_200_DATA_SCAN_VALUES: set[
    GetWordRequestResponse200DataScan
] = {
    "done",
    "pending",
}


def check_get_word_request_response_200_data_scan(
    value: str,
) -> GetWordRequestResponse200DataScan:
    if value in GET_WORD_REQUEST_RESPONSE_200_DATA_SCAN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WORD_REQUEST_RESPONSE_200_DATA_SCAN_VALUES!r}"
    )
