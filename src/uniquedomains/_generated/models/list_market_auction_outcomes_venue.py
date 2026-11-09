from typing import Literal

ListMarketAuctionOutcomesVenue = Literal[
    "domainlore", "dynadot", "godaddy", "namecheap", "namesilo", "parkio", "snapnames"
]

LIST_MARKET_AUCTION_OUTCOMES_VENUE_VALUES: set[ListMarketAuctionOutcomesVenue] = {
    "domainlore",
    "dynadot",
    "godaddy",
    "namecheap",
    "namesilo",
    "parkio",
    "snapnames",
}


def check_list_market_auction_outcomes_venue(
    value: str,
) -> ListMarketAuctionOutcomesVenue:
    if value in LIST_MARKET_AUCTION_OUTCOMES_VENUE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MARKET_AUCTION_OUTCOMES_VENUE_VALUES!r}"
    )
