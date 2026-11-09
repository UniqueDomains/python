from typing import Literal

GetNameRegistryResponse200DataTransportType2Type1 = Literal["rdap", "whois"]

GET_NAME_REGISTRY_RESPONSE_200_DATA_TRANSPORT_TYPE_2_TYPE_1_VALUES: set[
    GetNameRegistryResponse200DataTransportType2Type1
] = {
    "rdap",
    "whois",
}


def check_get_name_registry_response_200_data_transport_type_2_type_1(
    value: str,
) -> GetNameRegistryResponse200DataTransportType2Type1:
    if value in GET_NAME_REGISTRY_RESPONSE_200_DATA_TRANSPORT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_NAME_REGISTRY_RESPONSE_200_DATA_TRANSPORT_TYPE_2_TYPE_1_VALUES!r}"
    )
