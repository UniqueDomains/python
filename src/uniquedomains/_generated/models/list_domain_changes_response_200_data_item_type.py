from typing import Literal

ListDomainChangesResponse200DataItemType = Literal[
    "auction_ending",
    "auction_jump",
    "expiry_window",
    "lifecycle_move",
    "lock_removed",
    "nameserver_change",
    "parking_change",
    "price_drop",
    "price_increase",
    "registrar_change",
    "renewal_observed",
    "status_change",
    "transfer",
]

LIST_DOMAIN_CHANGES_RESPONSE_200_DATA_ITEM_TYPE_VALUES: set[
    ListDomainChangesResponse200DataItemType
] = {
    "auction_ending",
    "auction_jump",
    "expiry_window",
    "lifecycle_move",
    "lock_removed",
    "nameserver_change",
    "parking_change",
    "price_drop",
    "price_increase",
    "registrar_change",
    "renewal_observed",
    "status_change",
    "transfer",
}


def check_list_domain_changes_response_200_data_item_type(
    value: str,
) -> ListDomainChangesResponse200DataItemType:
    if value in LIST_DOMAIN_CHANGES_RESPONSE_200_DATA_ITEM_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAIN_CHANGES_RESPONSE_200_DATA_ITEM_TYPE_VALUES!r}"
    )
