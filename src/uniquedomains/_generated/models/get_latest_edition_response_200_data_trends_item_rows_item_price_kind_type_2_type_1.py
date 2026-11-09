from typing import Literal

GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType2Type1 = Literal[
    "auction", "marketplace", "premium", "registration"
]

GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_PRICE_KIND_TYPE_2_TYPE_1_VALUES: set[
    GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType2Type1
] = {
    "auction",
    "marketplace",
    "premium",
    "registration",
}


def check_get_latest_edition_response_200_data_trends_item_rows_item_price_kind_type_2_type_1(
    value: str,
) -> GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType2Type1:
    if (
        value
        in GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_PRICE_KIND_TYPE_2_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_PRICE_KIND_TYPE_2_TYPE_1_VALUES!r}"
    )
