from typing import Literal

BatchNamesResponse200DataItemType0ValueType0LiquidityType3Type1 = Literal[
    "high", "low", "medium"
]

BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_VALUE_TYPE_0_LIQUIDITY_TYPE_3_TYPE_1_VALUES: set[
    BatchNamesResponse200DataItemType0ValueType0LiquidityType3Type1
] = {
    "high",
    "low",
    "medium",
}


def check_batch_names_response_200_data_item_type_0_value_type_0_liquidity_type_3_type_1(
    value: str,
) -> BatchNamesResponse200DataItemType0ValueType0LiquidityType3Type1:
    if (
        value
        in BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_VALUE_TYPE_0_LIQUIDITY_TYPE_3_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_VALUE_TYPE_0_LIQUIDITY_TYPE_3_TYPE_1_VALUES!r}"
    )
