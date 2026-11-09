from typing import Literal

CheckNameResponse200DataValueType0LiquidityType1 = Literal["high", "low", "medium"]

CHECK_NAME_RESPONSE_200_DATA_VALUE_TYPE_0_LIQUIDITY_TYPE_1_VALUES: set[
    CheckNameResponse200DataValueType0LiquidityType1
] = {
    "high",
    "low",
    "medium",
}


def check_check_name_response_200_data_value_type_0_liquidity_type_1(
    value: str,
) -> CheckNameResponse200DataValueType0LiquidityType1:
    if value in CHECK_NAME_RESPONSE_200_DATA_VALUE_TYPE_0_LIQUIDITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_200_DATA_VALUE_TYPE_0_LIQUIDITY_TYPE_1_VALUES!r}"
    )
