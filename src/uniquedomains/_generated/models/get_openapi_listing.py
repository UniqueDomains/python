from typing import Literal

GetOpenapiListing = Literal[
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

GET_OPENAPI_LISTING_VALUES: set[GetOpenapiListing] = {
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


def check_get_openapi_listing(value: str) -> GetOpenapiListing:
    if value in GET_OPENAPI_LISTING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_OPENAPI_LISTING_VALUES!r}"
    )
