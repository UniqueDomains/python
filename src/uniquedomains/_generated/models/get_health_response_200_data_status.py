from typing import Literal

GetHealthResponse200DataStatus = Literal["ok"]

GET_HEALTH_RESPONSE_200_DATA_STATUS_VALUES: set[GetHealthResponse200DataStatus] = {
    "ok",
}


def check_get_health_response_200_data_status(
    value: str,
) -> GetHealthResponse200DataStatus:
    if value in GET_HEALTH_RESPONSE_200_DATA_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HEALTH_RESPONSE_200_DATA_STATUS_VALUES!r}"
    )
