from typing import Literal

GetMetaProvidersResponse200DataParkingServicesItemKind = Literal[
    "dropcatch", "marketplace", "parking"
]

GET_META_PROVIDERS_RESPONSE_200_DATA_PARKING_SERVICES_ITEM_KIND_VALUES: set[
    GetMetaProvidersResponse200DataParkingServicesItemKind
] = {
    "dropcatch",
    "marketplace",
    "parking",
}


def check_get_meta_providers_response_200_data_parking_services_item_kind(
    value: str,
) -> GetMetaProvidersResponse200DataParkingServicesItemKind:
    if value in GET_META_PROVIDERS_RESPONSE_200_DATA_PARKING_SERVICES_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_META_PROVIDERS_RESPONSE_200_DATA_PARKING_SERVICES_ITEM_KIND_VALUES!r}"
    )
