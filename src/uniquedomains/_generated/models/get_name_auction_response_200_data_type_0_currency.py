from typing import Literal

GetNameAuctionResponse200DataType0Currency = Literal["GBP", "USD"]

GET_NAME_AUCTION_RESPONSE_200_DATA_TYPE_0_CURRENCY_VALUES: set[
    GetNameAuctionResponse200DataType0Currency
] = {
    "GBP",
    "USD",
}


def check_get_name_auction_response_200_data_type_0_currency(
    value: str,
) -> GetNameAuctionResponse200DataType0Currency:
    if value in GET_NAME_AUCTION_RESPONSE_200_DATA_TYPE_0_CURRENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_NAME_AUCTION_RESPONSE_200_DATA_TYPE_0_CURRENCY_VALUES!r}"
    )
