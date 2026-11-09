from typing import Literal

GetMarketAuctionsResponse200DataByVenueItemVenue = Literal[
    "domainlore", "dynadot", "godaddy", "namecheap", "namesilo", "parkio", "snapnames"
]

GET_MARKET_AUCTIONS_RESPONSE_200_DATA_BY_VENUE_ITEM_VENUE_VALUES: set[
    GetMarketAuctionsResponse200DataByVenueItemVenue
] = {
    "domainlore",
    "dynadot",
    "godaddy",
    "namecheap",
    "namesilo",
    "parkio",
    "snapnames",
}


def check_get_market_auctions_response_200_data_by_venue_item_venue(
    value: str,
) -> GetMarketAuctionsResponse200DataByVenueItemVenue:
    if value in GET_MARKET_AUCTIONS_RESPONSE_200_DATA_BY_VENUE_ITEM_VENUE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_MARKET_AUCTIONS_RESPONSE_200_DATA_BY_VENUE_ITEM_VENUE_VALUES!r}"
    )
