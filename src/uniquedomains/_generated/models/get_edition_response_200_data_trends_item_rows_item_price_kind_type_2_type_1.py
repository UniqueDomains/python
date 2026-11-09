from typing import Literal

GetEditionResponse200DataTrendsItemRowsItemPriceKindType2Type1 = Literal[
    "auction", "marketplace", "premium", "registration"
]

GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_PRICE_KIND_TYPE_2_TYPE_1_VALUES: set[
    GetEditionResponse200DataTrendsItemRowsItemPriceKindType2Type1
] = {
    "auction",
    "marketplace",
    "premium",
    "registration",
}


def check_get_edition_response_200_data_trends_item_rows_item_price_kind_type_2_type_1(
    value: str,
) -> GetEditionResponse200DataTrendsItemRowsItemPriceKindType2Type1:
    if (
        value
        in GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_PRICE_KIND_TYPE_2_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_PRICE_KIND_TYPE_2_TYPE_1_VALUES!r}"
    )
