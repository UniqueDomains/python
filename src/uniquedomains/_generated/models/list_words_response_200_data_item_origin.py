from typing import Literal

ListWordsResponse200DataItemOrigin = Literal["api", "dictionary", "review", "trend"]

LIST_WORDS_RESPONSE_200_DATA_ITEM_ORIGIN_VALUES: set[
    ListWordsResponse200DataItemOrigin
] = {
    "api",
    "dictionary",
    "review",
    "trend",
}


def check_list_words_response_200_data_item_origin(
    value: str,
) -> ListWordsResponse200DataItemOrigin:
    if value in LIST_WORDS_RESPONSE_200_DATA_ITEM_ORIGIN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_WORDS_RESPONSE_200_DATA_ITEM_ORIGIN_VALUES!r}"
    )
