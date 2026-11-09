from typing import Literal

GetWordTrademarksResponse200DataMarksItemOffice = Literal["EU", "US"]

GET_WORD_TRADEMARKS_RESPONSE_200_DATA_MARKS_ITEM_OFFICE_VALUES: set[
    GetWordTrademarksResponse200DataMarksItemOffice
] = {
    "EU",
    "US",
}


def check_get_word_trademarks_response_200_data_marks_item_office(
    value: str,
) -> GetWordTrademarksResponse200DataMarksItemOffice:
    if value in GET_WORD_TRADEMARKS_RESPONSE_200_DATA_MARKS_ITEM_OFFICE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WORD_TRADEMARKS_RESPONSE_200_DATA_MARKS_ITEM_OFFICE_VALUES!r}"
    )
