from typing import Literal

BatchWordsResponse200DataItemType0Origin = Literal[
    "api", "dictionary", "review", "trend"
]

BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_ORIGIN_VALUES: set[
    BatchWordsResponse200DataItemType0Origin
] = {
    "api",
    "dictionary",
    "review",
    "trend",
}


def check_batch_words_response_200_data_item_type_0_origin(
    value: str,
) -> BatchWordsResponse200DataItemType0Origin:
    if value in BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_ORIGIN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_ORIGIN_VALUES!r}"
    )
