from typing import Literal

ListExpiringDomainsResponse200DataItemStatus = Literal["expired", "expiring"]

LIST_EXPIRING_DOMAINS_RESPONSE_200_DATA_ITEM_STATUS_VALUES: set[
    ListExpiringDomainsResponse200DataItemStatus
] = {
    "expired",
    "expiring",
}


def check_list_expiring_domains_response_200_data_item_status(
    value: str,
) -> ListExpiringDomainsResponse200DataItemStatus:
    if value in LIST_EXPIRING_DOMAINS_RESPONSE_200_DATA_ITEM_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_EXPIRING_DOMAINS_RESPONSE_200_DATA_ITEM_STATUS_VALUES!r}"
    )
