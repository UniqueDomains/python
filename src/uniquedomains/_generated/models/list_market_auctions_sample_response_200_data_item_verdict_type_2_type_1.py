from typing import Literal

ListMarketAuctionsSampleResponse200DataItemVerdictType2Type1 = Literal[
    "Good", "Risky", "Strong choice"
]

LIST_MARKET_AUCTIONS_SAMPLE_RESPONSE_200_DATA_ITEM_VERDICT_TYPE_2_TYPE_1_VALUES: set[
    ListMarketAuctionsSampleResponse200DataItemVerdictType2Type1
] = {
    "Good",
    "Risky",
    "Strong choice",
}


def check_list_market_auctions_sample_response_200_data_item_verdict_type_2_type_1(
    value: str,
) -> ListMarketAuctionsSampleResponse200DataItemVerdictType2Type1:
    if (
        value
        in LIST_MARKET_AUCTIONS_SAMPLE_RESPONSE_200_DATA_ITEM_VERDICT_TYPE_2_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MARKET_AUCTIONS_SAMPLE_RESPONSE_200_DATA_ITEM_VERDICT_TYPE_2_TYPE_1_VALUES!r}"
    )
