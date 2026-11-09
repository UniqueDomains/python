from typing import Literal

ListMarketAuctionsSampleResponse200DataItemTagType1 = Literal["jumped"]

LIST_MARKET_AUCTIONS_SAMPLE_RESPONSE_200_DATA_ITEM_TAG_TYPE_1_VALUES: set[
    ListMarketAuctionsSampleResponse200DataItemTagType1
] = {
    "jumped",
}


def check_list_market_auctions_sample_response_200_data_item_tag_type_1(
    value: str,
) -> ListMarketAuctionsSampleResponse200DataItemTagType1:
    if value in LIST_MARKET_AUCTIONS_SAMPLE_RESPONSE_200_DATA_ITEM_TAG_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MARKET_AUCTIONS_SAMPLE_RESPONSE_200_DATA_ITEM_TAG_TYPE_1_VALUES!r}"
    )
