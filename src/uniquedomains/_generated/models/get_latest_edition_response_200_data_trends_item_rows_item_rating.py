from typing import Literal

GetLatestEditionResponse200DataTrendsItemRowsItemRating = Literal[
    "good", "risky", "strong", "unrated"
]

GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_RATING_VALUES: set[
    GetLatestEditionResponse200DataTrendsItemRowsItemRating
] = {
    "good",
    "risky",
    "strong",
    "unrated",
}


def check_get_latest_edition_response_200_data_trends_item_rows_item_rating(
    value: str,
) -> GetLatestEditionResponse200DataTrendsItemRowsItemRating:
    if (
        value
        in GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_RATING_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_RATING_VALUES!r}"
    )
