from typing import Literal

ListMarketAuctionsSampleResponse200DataItemCurrency = Literal["GBP", "USD"]

LIST_MARKET_AUCTIONS_SAMPLE_RESPONSE_200_DATA_ITEM_CURRENCY_VALUES: set[
    ListMarketAuctionsSampleResponse200DataItemCurrency
] = {
    "GBP",
    "USD",
}


def check_list_market_auctions_sample_response_200_data_item_currency(
    value: str,
) -> ListMarketAuctionsSampleResponse200DataItemCurrency:
    if value in LIST_MARKET_AUCTIONS_SAMPLE_RESPONSE_200_DATA_ITEM_CURRENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MARKET_AUCTIONS_SAMPLE_RESPONSE_200_DATA_ITEM_CURRENCY_VALUES!r}"
    )
