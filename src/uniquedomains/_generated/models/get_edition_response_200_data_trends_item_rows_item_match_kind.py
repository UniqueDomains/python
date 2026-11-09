from typing import Literal

GetEditionResponse200DataTrendsItemRowsItemMatchKind = Literal["exact", "related"]

GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_MATCH_KIND_VALUES: set[
    GetEditionResponse200DataTrendsItemRowsItemMatchKind
] = {
    "exact",
    "related",
}


def check_get_edition_response_200_data_trends_item_rows_item_match_kind(
    value: str,
) -> GetEditionResponse200DataTrendsItemRowsItemMatchKind:
    if value in GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_MATCH_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_MATCH_KIND_VALUES!r}"
    )
