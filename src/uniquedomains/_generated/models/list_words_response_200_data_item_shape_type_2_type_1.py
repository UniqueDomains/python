from typing import Literal

ListWordsResponse200DataItemShapeType2Type1 = Literal[
    "acronym", "phrase", "properNoun", "single", "twoWords"
]

LIST_WORDS_RESPONSE_200_DATA_ITEM_SHAPE_TYPE_2_TYPE_1_VALUES: set[
    ListWordsResponse200DataItemShapeType2Type1
] = {
    "acronym",
    "phrase",
    "properNoun",
    "single",
    "twoWords",
}


def check_list_words_response_200_data_item_shape_type_2_type_1(
    value: str,
) -> ListWordsResponse200DataItemShapeType2Type1:
    if value in LIST_WORDS_RESPONSE_200_DATA_ITEM_SHAPE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_WORDS_RESPONSE_200_DATA_ITEM_SHAPE_TYPE_2_TYPE_1_VALUES!r}"
    )
