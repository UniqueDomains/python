from typing import Literal

ListDomainHacksResponse200DataItemStatus = Literal[
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

LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_STATUS_VALUES: set[
    ListDomainHacksResponse200DataItemStatus
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


def check_list_domain_hacks_response_200_data_item_status(
    value: str,
) -> ListDomainHacksResponse200DataItemStatus:
    if value in LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_STATUS_VALUES!r}"
    )
