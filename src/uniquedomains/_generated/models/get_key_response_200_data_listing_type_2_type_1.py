from typing import Literal

GetKeyResponse200DataListingType2Type1 = Literal[
    "agenda",
    "appraisal",
    "auctions",
    "availability",
    "catalog",
    "expired",
    "market",
    "names",
    "price-comparison",
    "registrars",
    "sales-history",
    "tlds",
    "trending-topics",
    "trends",
    "whois",
    "words",
]

GET_KEY_RESPONSE_200_DATA_LISTING_TYPE_2_TYPE_1_VALUES: set[
    GetKeyResponse200DataListingType2Type1
] = {
    "agenda",
    "appraisal",
    "auctions",
    "availability",
    "catalog",
    "expired",
    "market",
    "names",
    "price-comparison",
    "registrars",
    "sales-history",
    "tlds",
    "trending-topics",
    "trends",
    "whois",
    "words",
}


def check_get_key_response_200_data_listing_type_2_type_1(
    value: str,
) -> GetKeyResponse200DataListingType2Type1:
    if value in GET_KEY_RESPONSE_200_DATA_LISTING_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_KEY_RESPONSE_200_DATA_LISTING_TYPE_2_TYPE_1_VALUES!r}"
    )
