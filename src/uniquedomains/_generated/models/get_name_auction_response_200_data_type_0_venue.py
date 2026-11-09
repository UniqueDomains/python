from typing import Literal

GetNameAuctionResponse200DataType0Venue = Literal[
    "domainlore", "dynadot", "godaddy", "namecheap", "namesilo", "parkio", "snapnames"
]

GET_NAME_AUCTION_RESPONSE_200_DATA_TYPE_0_VENUE_VALUES: set[
    GetNameAuctionResponse200DataType0Venue
] = {
    "domainlore",
    "dynadot",
    "godaddy",
    "namecheap",
    "namesilo",
    "parkio",
    "snapnames",
}


def check_get_name_auction_response_200_data_type_0_venue(
    value: str,
) -> GetNameAuctionResponse200DataType0Venue:
    if value in GET_NAME_AUCTION_RESPONSE_200_DATA_TYPE_0_VENUE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_NAME_AUCTION_RESPONSE_200_DATA_TYPE_0_VENUE_VALUES!r}"
    )
