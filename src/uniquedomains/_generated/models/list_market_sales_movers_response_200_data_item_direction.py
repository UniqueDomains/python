from typing import Literal

ListMarketSalesMoversResponse200DataItemDirection = Literal["down", "flat", "up"]

LIST_MARKET_SALES_MOVERS_RESPONSE_200_DATA_ITEM_DIRECTION_VALUES: set[
    ListMarketSalesMoversResponse200DataItemDirection
] = {
    "down",
    "flat",
    "up",
}


def check_list_market_sales_movers_response_200_data_item_direction(
    value: str,
) -> ListMarketSalesMoversResponse200DataItemDirection:
    if value in LIST_MARKET_SALES_MOVERS_RESPONSE_200_DATA_ITEM_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MARKET_SALES_MOVERS_RESPONSE_200_DATA_ITEM_DIRECTION_VALUES!r}"
    )
