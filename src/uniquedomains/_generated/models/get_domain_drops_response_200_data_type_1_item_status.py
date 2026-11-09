from typing import Literal

GetDomainDropsResponse200DataType1ItemStatus = Literal[
    "available",
    "dormant",
    "expired",
    "expiring",
    "premium",
    "resell",
    "sold",
    "taken",
    "unknown",
]

GET_DOMAIN_DROPS_RESPONSE_200_DATA_TYPE_1_ITEM_STATUS_VALUES: set[
    GetDomainDropsResponse200DataType1ItemStatus
] = {
    "available",
    "dormant",
    "expired",
    "expiring",
    "premium",
    "resell",
    "sold",
    "taken",
    "unknown",
}


def check_get_domain_drops_response_200_data_type_1_item_status(
    value: str,
) -> GetDomainDropsResponse200DataType1ItemStatus:
    if value in GET_DOMAIN_DROPS_RESPONSE_200_DATA_TYPE_1_ITEM_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_DOMAIN_DROPS_RESPONSE_200_DATA_TYPE_1_ITEM_STATUS_VALUES!r}"
    )
