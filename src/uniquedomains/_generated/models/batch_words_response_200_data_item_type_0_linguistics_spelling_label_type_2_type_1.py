from typing import Literal

BatchWordsResponse200DataItemType0LinguisticsSpellingLabelType2Type1 = Literal[
    "high", "low", "medium"
]

BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_LINGUISTICS_SPELLING_LABEL_TYPE_2_TYPE_1_VALUES: set[
    BatchWordsResponse200DataItemType0LinguisticsSpellingLabelType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_batch_words_response_200_data_item_type_0_linguistics_spelling_label_type_2_type_1(
    value: str,
) -> BatchWordsResponse200DataItemType0LinguisticsSpellingLabelType2Type1:
    if (
        value
        in BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_LINGUISTICS_SPELLING_LABEL_TYPE_2_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_LINGUISTICS_SPELLING_LABEL_TYPE_2_TYPE_1_VALUES!r}"
    )
