from typing import Literal

GetMetaTldsListing = Literal["all", "public"]

GET_META_TLDS_LISTING_VALUES: set[GetMetaTldsListing] = {
    "all",
    "public",
}


def check_get_meta_tlds_listing(value: str) -> GetMetaTldsListing:
    if value in GET_META_TLDS_LISTING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_META_TLDS_LISTING_VALUES!r}"
    )
