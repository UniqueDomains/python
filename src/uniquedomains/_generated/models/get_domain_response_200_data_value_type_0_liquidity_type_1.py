from typing import Literal

GetDomainResponse200DataValueType0LiquidityType1 = Literal["high", "low", "medium"]

GET_DOMAIN_RESPONSE_200_DATA_VALUE_TYPE_0_LIQUIDITY_TYPE_1_VALUES: set[
    GetDomainResponse200DataValueType0LiquidityType1
] = {
    "high",
    "low",
    "medium",
}


def check_get_domain_response_200_data_value_type_0_liquidity_type_1(
    value: str,
) -> GetDomainResponse200DataValueType0LiquidityType1:
    if value in GET_DOMAIN_RESPONSE_200_DATA_VALUE_TYPE_0_LIQUIDITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_DOMAIN_RESPONSE_200_DATA_VALUE_TYPE_0_LIQUIDITY_TYPE_1_VALUES!r}"
    )
