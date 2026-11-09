from typing import Literal

CheckNameResponse202DataValueType0LiquidityType2Type1 = Literal["high", "low", "medium"]

CHECK_NAME_RESPONSE_202_DATA_VALUE_TYPE_0_LIQUIDITY_TYPE_2_TYPE_1_VALUES: set[
    CheckNameResponse202DataValueType0LiquidityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_check_name_response_202_data_value_type_0_liquidity_type_2_type_1(
    value: str,
) -> CheckNameResponse202DataValueType0LiquidityType2Type1:
    if (
        value
        in CHECK_NAME_RESPONSE_202_DATA_VALUE_TYPE_0_LIQUIDITY_TYPE_2_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_202_DATA_VALUE_TYPE_0_LIQUIDITY_TYPE_2_TYPE_1_VALUES!r}"
    )
