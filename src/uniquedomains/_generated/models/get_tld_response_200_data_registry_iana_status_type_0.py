from typing import Literal

GetTldResponse200DataRegistryIanaStatusType0 = Literal[
    "delegated", "never_delegated", "removed"
]

GET_TLD_RESPONSE_200_DATA_REGISTRY_IANA_STATUS_TYPE_0_VALUES: set[
    GetTldResponse200DataRegistryIanaStatusType0
] = {
    "delegated",
    "never_delegated",
    "removed",
}


def check_get_tld_response_200_data_registry_iana_status_type_0(
    value: str,
) -> GetTldResponse200DataRegistryIanaStatusType0:
    if value in GET_TLD_RESPONSE_200_DATA_REGISTRY_IANA_STATUS_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TLD_RESPONSE_200_DATA_REGISTRY_IANA_STATUS_TYPE_0_VALUES!r}"
    )
