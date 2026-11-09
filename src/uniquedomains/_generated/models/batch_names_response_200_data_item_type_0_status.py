from typing import Literal

BatchNamesResponse200DataItemType0Status = Literal[
    "at_auction",
    "expired",
    "expiring",
    "for_sale",
    "free",
    "free_premium",
    "in_use",
    "not_a_name",
    "not_checked",
    "not_covered",
    "parked",
    "pending_delete",
    "redemption",
    "registered",
]

BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_STATUS_VALUES: set[
    BatchNamesResponse200DataItemType0Status
] = {
    "at_auction",
    "expired",
    "expiring",
    "for_sale",
    "free",
    "free_premium",
    "in_use",
    "not_a_name",
    "not_checked",
    "not_covered",
    "parked",
    "pending_delete",
    "redemption",
    "registered",
}


def check_batch_names_response_200_data_item_type_0_status(
    value: str,
) -> BatchNamesResponse200DataItemType0Status:
    if value in BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_STATUS_VALUES!r}"
    )
