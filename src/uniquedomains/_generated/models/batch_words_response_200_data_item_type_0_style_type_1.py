from typing import Literal

BatchWordsResponse200DataItemType0StyleType1 = Literal[
    "elegant", "futuristic", "handwritten", "modern", "playful", "slab"
]

BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_STYLE_TYPE_1_VALUES: set[
    BatchWordsResponse200DataItemType0StyleType1
] = {
    "elegant",
    "futuristic",
    "handwritten",
    "modern",
    "playful",
    "slab",
}


def check_batch_words_response_200_data_item_type_0_style_type_1(
    value: str,
) -> BatchWordsResponse200DataItemType0StyleType1:
    if value in BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_STYLE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_STYLE_TYPE_1_VALUES!r}"
    )
