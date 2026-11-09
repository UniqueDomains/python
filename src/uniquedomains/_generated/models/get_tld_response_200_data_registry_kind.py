from typing import Literal

GetTldResponse200DataRegistryKind = Literal["root", "second_level", "web3"]

GET_TLD_RESPONSE_200_DATA_REGISTRY_KIND_VALUES: set[
    GetTldResponse200DataRegistryKind
] = {
    "root",
    "second_level",
    "web3",
}


def check_get_tld_response_200_data_registry_kind(
    value: str,
) -> GetTldResponse200DataRegistryKind:
    if value in GET_TLD_RESPONSE_200_DATA_REGISTRY_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TLD_RESPONSE_200_DATA_REGISTRY_KIND_VALUES!r}"
    )
