from typing import Literal

ListWordsShape = Literal["acronym", "phrase", "properNoun", "single", "twoWords"]

LIST_WORDS_SHAPE_VALUES: set[ListWordsShape] = {
    "acronym",
    "phrase",
    "properNoun",
    "single",
    "twoWords",
}


def check_list_words_shape(value: str) -> ListWordsShape:
    if value in LIST_WORDS_SHAPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_WORDS_SHAPE_VALUES!r}"
    )
