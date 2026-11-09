from typing import Literal

GetKeyResponse200DataAccess = Literal["member", "rapidapi"]

GET_KEY_RESPONSE_200_DATA_ACCESS_VALUES: set[GetKeyResponse200DataAccess] = {
    "member",
    "rapidapi",
}


def check_get_key_response_200_data_access(value: str) -> GetKeyResponse200DataAccess:
    if value in GET_KEY_RESPONSE_200_DATA_ACCESS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_KEY_RESPONSE_200_DATA_ACCESS_VALUES!r}"
    )
