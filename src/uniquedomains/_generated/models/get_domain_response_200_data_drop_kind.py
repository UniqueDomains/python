from typing import Literal

GetDomainResponse200DataDropKind = Literal["date", "none"]

GET_DOMAIN_RESPONSE_200_DATA_DROP_KIND_VALUES: set[GetDomainResponse200DataDropKind] = {
    "date",
    "none",
}


def check_get_domain_response_200_data_drop_kind(
    value: str,
) -> GetDomainResponse200DataDropKind:
    if value in GET_DOMAIN_RESPONSE_200_DATA_DROP_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_DOMAIN_RESPONSE_200_DATA_DROP_KIND_VALUES!r}"
    )
