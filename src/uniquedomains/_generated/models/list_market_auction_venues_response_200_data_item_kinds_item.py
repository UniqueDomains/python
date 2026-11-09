from typing import Literal

ListMarketAuctionVenuesResponse200DataItemKindsItem = Literal[
    "expired", "unspecified", "user"
]

LIST_MARKET_AUCTION_VENUES_RESPONSE_200_DATA_ITEM_KINDS_ITEM_VALUES: set[
    ListMarketAuctionVenuesResponse200DataItemKindsItem
] = {
    "expired",
    "unspecified",
    "user",
}


def check_list_market_auction_venues_response_200_data_item_kinds_item(
    value: str,
) -> ListMarketAuctionVenuesResponse200DataItemKindsItem:
    if value in LIST_MARKET_AUCTION_VENUES_RESPONSE_200_DATA_ITEM_KINDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MARKET_AUCTION_VENUES_RESPONSE_200_DATA_ITEM_KINDS_ITEM_VALUES!r}"
    )
