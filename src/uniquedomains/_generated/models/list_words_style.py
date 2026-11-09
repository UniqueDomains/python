from typing import Literal

ListWordsStyle = Literal[
    "elegant", "futuristic", "handwritten", "modern", "playful", "slab"
]

LIST_WORDS_STYLE_VALUES: set[ListWordsStyle] = {
    "elegant",
    "futuristic",
    "handwritten",
    "modern",
    "playful",
    "slab",
}


def check_list_words_style(value: str) -> ListWordsStyle:
    if value in LIST_WORDS_STYLE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_WORDS_STYLE_VALUES!r}"
    )
