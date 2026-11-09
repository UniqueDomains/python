from typing import Literal

GetLatestEditionResponse200DataTrendsItemRowsItemMatchKind = Literal["exact", "related"]

GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_MATCH_KIND_VALUES: set[
    GetLatestEditionResponse200DataTrendsItemRowsItemMatchKind
] = {
    "exact",
    "related",
}


def check_get_latest_edition_response_200_data_trends_item_rows_item_match_kind(
    value: str,
) -> GetLatestEditionResponse200DataTrendsItemRowsItemMatchKind:
    if (
        value
        in GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_MATCH_KIND_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_MATCH_KIND_VALUES!r}"
    )
