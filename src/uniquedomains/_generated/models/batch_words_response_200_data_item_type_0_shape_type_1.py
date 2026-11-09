from typing import Literal

BatchWordsResponse200DataItemType0ShapeType1 = Literal[
    "acronym", "phrase", "properNoun", "single", "twoWords"
]

BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_SHAPE_TYPE_1_VALUES: set[
    BatchWordsResponse200DataItemType0ShapeType1
] = {
    "acronym",
    "phrase",
    "properNoun",
    "single",
    "twoWords",
}


def check_batch_words_response_200_data_item_type_0_shape_type_1(
    value: str,
) -> BatchWordsResponse200DataItemType0ShapeType1:
    if value in BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_SHAPE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_SHAPE_TYPE_1_VALUES!r}"
    )
