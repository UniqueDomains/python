from typing import Literal

ListWordsOrigin = Literal["api", "dictionary", "review", "trend"]

LIST_WORDS_ORIGIN_VALUES: set[ListWordsOrigin] = {
    "api",
    "dictionary",
    "review",
    "trend",
}


def check_list_words_origin(value: str) -> ListWordsOrigin:
    if value in LIST_WORDS_ORIGIN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_WORDS_ORIGIN_VALUES!r}"
    )
