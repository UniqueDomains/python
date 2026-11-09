from typing import Literal

GetMetaEnumsResponse200DataParkingServicesItemKind = Literal[
    "dropcatch", "marketplace", "parking"
]

GET_META_ENUMS_RESPONSE_200_DATA_PARKING_SERVICES_ITEM_KIND_VALUES: set[
    GetMetaEnumsResponse200DataParkingServicesItemKind
] = {
    "dropcatch",
    "marketplace",
    "parking",
}


def check_get_meta_enums_response_200_data_parking_services_item_kind(
    value: str,
) -> GetMetaEnumsResponse200DataParkingServicesItemKind:
    if value in GET_META_ENUMS_RESPONSE_200_DATA_PARKING_SERVICES_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_META_ENUMS_RESPONSE_200_DATA_PARKING_SERVICES_ITEM_KIND_VALUES!r}"
    )
