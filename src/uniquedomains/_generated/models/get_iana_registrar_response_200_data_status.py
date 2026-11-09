from typing import Literal

GetIanaRegistrarResponse200DataStatus = Literal["accredited", "reserved", "terminated"]

GET_IANA_REGISTRAR_RESPONSE_200_DATA_STATUS_VALUES: set[
    GetIanaRegistrarResponse200DataStatus
] = {
    "accredited",
    "reserved",
    "terminated",
}


def check_get_iana_registrar_response_200_data_status(
    value: str,
) -> GetIanaRegistrarResponse200DataStatus:
    if value in GET_IANA_REGISTRAR_RESPONSE_200_DATA_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_IANA_REGISTRAR_RESPONSE_200_DATA_STATUS_VALUES!r}"
    )
