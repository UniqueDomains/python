from typing import Literal

ListMarketAuctionOutcomesResponse200DataItemVenue = Literal[
    "domainlore", "dynadot", "godaddy", "namecheap", "namesilo", "parkio", "snapnames"
]

LIST_MARKET_AUCTION_OUTCOMES_RESPONSE_200_DATA_ITEM_VENUE_VALUES: set[
    ListMarketAuctionOutcomesResponse200DataItemVenue
] = {
    "domainlore",
    "dynadot",
    "godaddy",
    "namecheap",
    "namesilo",
    "parkio",
    "snapnames",
}


def check_list_market_auction_outcomes_response_200_data_item_venue(
    value: str,
) -> ListMarketAuctionOutcomesResponse200DataItemVenue:
    if value in LIST_MARKET_AUCTION_OUTCOMES_RESPONSE_200_DATA_ITEM_VENUE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MARKET_AUCTION_OUTCOMES_RESPONSE_200_DATA_ITEM_VENUE_VALUES!r}"
    )
