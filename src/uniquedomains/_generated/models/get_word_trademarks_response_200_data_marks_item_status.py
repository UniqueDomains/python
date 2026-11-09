from typing import Literal

GetWordTrademarksResponse200DataMarksItemStatus = Literal["dead", "live"]

GET_WORD_TRADEMARKS_RESPONSE_200_DATA_MARKS_ITEM_STATUS_VALUES: set[
    GetWordTrademarksResponse200DataMarksItemStatus
] = {
    "dead",
    "live",
}


def check_get_word_trademarks_response_200_data_marks_item_status(
    value: str,
) -> GetWordTrademarksResponse200DataMarksItemStatus:
    if value in GET_WORD_TRADEMARKS_RESPONSE_200_DATA_MARKS_ITEM_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WORD_TRADEMARKS_RESPONSE_200_DATA_MARKS_ITEM_STATUS_VALUES!r}"
    )
