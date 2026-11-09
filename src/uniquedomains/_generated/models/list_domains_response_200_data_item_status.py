from typing import Literal

ListDomainsResponse200DataItemStatus = Literal[
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

LIST_DOMAINS_RESPONSE_200_DATA_ITEM_STATUS_VALUES: set[
    ListDomainsResponse200DataItemStatus
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


def check_list_domains_response_200_data_item_status(
    value: str,
) -> ListDomainsResponse200DataItemStatus:
    if value in LIST_DOMAINS_RESPONSE_200_DATA_ITEM_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAINS_RESPONSE_200_DATA_ITEM_STATUS_VALUES!r}"
    )
