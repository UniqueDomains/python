from typing import Literal

CheckNameResponse202DataStatus = Literal[
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

CHECK_NAME_RESPONSE_202_DATA_STATUS_VALUES: set[CheckNameResponse202DataStatus] = {
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


def check_check_name_response_202_data_status(
    value: str,
) -> CheckNameResponse202DataStatus:
    if value in CHECK_NAME_RESPONSE_202_DATA_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_202_DATA_STATUS_VALUES!r}"
    )
