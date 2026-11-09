from typing import Literal

ListMarketAuctionVenuesResponse200DataItemId = Literal[
    "domainlore", "dynadot", "godaddy", "namecheap", "namesilo", "parkio", "snapnames"
]

LIST_MARKET_AUCTION_VENUES_RESPONSE_200_DATA_ITEM_ID_VALUES: set[
    ListMarketAuctionVenuesResponse200DataItemId
] = {
    "domainlore",
    "dynadot",
    "godaddy",
    "namecheap",
    "namesilo",
    "parkio",
    "snapnames",
}


def check_list_market_auction_venues_response_200_data_item_id(
    value: str,
) -> ListMarketAuctionVenuesResponse200DataItemId:
    if value in LIST_MARKET_AUCTION_VENUES_RESPONSE_200_DATA_ITEM_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MARKET_AUCTION_VENUES_RESPONSE_200_DATA_ITEM_ID_VALUES!r}"
    )
