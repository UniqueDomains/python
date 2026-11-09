from typing import Literal

GetOpenapiOas = Literal["3.0", "3.1"]

GET_OPENAPI_OAS_VALUES: set[GetOpenapiOas] = {
    "3.0",
    "3.1",
}


def check_get_openapi_oas(value: str) -> GetOpenapiOas:
    if value in GET_OPENAPI_OAS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_OPENAPI_OAS_VALUES!r}"
    )
