from typing import Literal

ListDomainHacksResponse200DataItemLiquidityType2Type1 = Literal["high", "low", "medium"]

LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_LIQUIDITY_TYPE_2_TYPE_1_VALUES: set[
    ListDomainHacksResponse200DataItemLiquidityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_list_domain_hacks_response_200_data_item_liquidity_type_2_type_1(
    value: str,
) -> ListDomainHacksResponse200DataItemLiquidityType2Type1:
    if value in LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_LIQUIDITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_LIQUIDITY_TYPE_2_TYPE_1_VALUES!r}"
    )
