from typing import Literal

GetDomainResponse200DataStatus = Literal[
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

GET_DOMAIN_RESPONSE_200_DATA_STATUS_VALUES: set[GetDomainResponse200DataStatus] = {
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


def check_get_domain_response_200_data_status(
    value: str,
) -> GetDomainResponse200DataStatus:
    if value in GET_DOMAIN_RESPONSE_200_DATA_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_DOMAIN_RESPONSE_200_DATA_STATUS_VALUES!r}"
    )
