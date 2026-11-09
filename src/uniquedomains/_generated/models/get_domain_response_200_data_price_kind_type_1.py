from typing import Literal

GetDomainResponse200DataPriceKindType1 = Literal[
    "aftermarket", "backorder", "premium", "registry"
]

GET_DOMAIN_RESPONSE_200_DATA_PRICE_KIND_TYPE_1_VALUES: set[
    GetDomainResponse200DataPriceKindType1
] = {
    "aftermarket",
    "backorder",
    "premium",
    "registry",
}


def check_get_domain_response_200_data_price_kind_type_1(
    value: str,
) -> GetDomainResponse200DataPriceKindType1:
    if value in GET_DOMAIN_RESPONSE_200_DATA_PRICE_KIND_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_DOMAIN_RESPONSE_200_DATA_PRICE_KIND_TYPE_1_VALUES!r}"
    )
