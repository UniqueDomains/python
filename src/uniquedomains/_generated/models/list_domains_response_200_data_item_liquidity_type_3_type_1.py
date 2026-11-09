from typing import Literal

ListDomainsResponse200DataItemLiquidityType3Type1 = Literal["high", "low", "medium"]

LIST_DOMAINS_RESPONSE_200_DATA_ITEM_LIQUIDITY_TYPE_3_TYPE_1_VALUES: set[
    ListDomainsResponse200DataItemLiquidityType3Type1
] = {
    "high",
    "low",
    "medium",
}


def check_list_domains_response_200_data_item_liquidity_type_3_type_1(
    value: str,
) -> ListDomainsResponse200DataItemLiquidityType3Type1:
    if value in LIST_DOMAINS_RESPONSE_200_DATA_ITEM_LIQUIDITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAINS_RESPONSE_200_DATA_ITEM_LIQUIDITY_TYPE_3_TYPE_1_VALUES!r}"
    )
