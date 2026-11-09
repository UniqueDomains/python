from typing import Literal

GetMetaProvidersResponse200DataAuctionVenuesItemId = Literal[
    "domainlore", "dynadot", "godaddy", "namecheap", "namesilo", "snapnames"
]

GET_META_PROVIDERS_RESPONSE_200_DATA_AUCTION_VENUES_ITEM_ID_VALUES: set[
    GetMetaProvidersResponse200DataAuctionVenuesItemId
] = {
    "domainlore",
    "dynadot",
    "godaddy",
    "namecheap",
    "namesilo",
    "snapnames",
}


def check_get_meta_providers_response_200_data_auction_venues_item_id(
    value: str,
) -> GetMetaProvidersResponse200DataAuctionVenuesItemId:
    if value in GET_META_PROVIDERS_RESPONSE_200_DATA_AUCTION_VENUES_ITEM_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_META_PROVIDERS_RESPONSE_200_DATA_AUCTION_VENUES_ITEM_ID_VALUES!r}"
    )
