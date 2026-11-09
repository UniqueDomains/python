from typing import Literal

ListMarketAuctionsSampleResponse200DataItemVenue = Literal[
    "domainlore", "dynadot", "godaddy", "namecheap", "namesilo", "parkio", "snapnames"
]

LIST_MARKET_AUCTIONS_SAMPLE_RESPONSE_200_DATA_ITEM_VENUE_VALUES: set[
    ListMarketAuctionsSampleResponse200DataItemVenue
] = {
    "domainlore",
    "dynadot",
    "godaddy",
    "namecheap",
    "namesilo",
    "parkio",
    "snapnames",
}


def check_list_market_auctions_sample_response_200_data_item_venue(
    value: str,
) -> ListMarketAuctionsSampleResponse200DataItemVenue:
    if value in LIST_MARKET_AUCTIONS_SAMPLE_RESPONSE_200_DATA_ITEM_VENUE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MARKET_AUCTIONS_SAMPLE_RESPONSE_200_DATA_ITEM_VENUE_VALUES!r}"
    )
