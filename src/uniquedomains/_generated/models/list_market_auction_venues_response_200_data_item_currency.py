from typing import Literal

ListMarketAuctionVenuesResponse200DataItemCurrency = Literal["GBP", "USD"]

LIST_MARKET_AUCTION_VENUES_RESPONSE_200_DATA_ITEM_CURRENCY_VALUES: set[
    ListMarketAuctionVenuesResponse200DataItemCurrency
] = {
    "GBP",
    "USD",
}


def check_list_market_auction_venues_response_200_data_item_currency(
    value: str,
) -> ListMarketAuctionVenuesResponse200DataItemCurrency:
    if value in LIST_MARKET_AUCTION_VENUES_RESPONSE_200_DATA_ITEM_CURRENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MARKET_AUCTION_VENUES_RESPONSE_200_DATA_ITEM_CURRENCY_VALUES!r}"
    )
