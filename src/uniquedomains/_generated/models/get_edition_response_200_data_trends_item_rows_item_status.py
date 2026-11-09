from typing import Literal

GetEditionResponse200DataTrendsItemRowsItemStatus = Literal[
    "auction", "available", "expiring", "forSale", "premium"
]

GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_STATUS_VALUES: set[
    GetEditionResponse200DataTrendsItemRowsItemStatus
] = {
    "auction",
    "available",
    "expiring",
    "forSale",
    "premium",
}


def check_get_edition_response_200_data_trends_item_rows_item_status(
    value: str,
) -> GetEditionResponse200DataTrendsItemRowsItemStatus:
    if value in GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_STATUS_VALUES!r}"
    )
