from typing import Literal

BatchWordsResponse200DataItemType0LinguisticsPronounceabilityLabelType1 = Literal[
    "easy", "hard", "medium"
]

BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_LINGUISTICS_PRONOUNCEABILITY_LABEL_TYPE_1_VALUES: set[
    BatchWordsResponse200DataItemType0LinguisticsPronounceabilityLabelType1
] = {
    "easy",
    "hard",
    "medium",
}


def check_batch_words_response_200_data_item_type_0_linguistics_pronounceability_label_type_1(
    value: str,
) -> BatchWordsResponse200DataItemType0LinguisticsPronounceabilityLabelType1:
    if (
        value
        in BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_LINGUISTICS_PRONOUNCEABILITY_LABEL_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_LINGUISTICS_PRONOUNCEABILITY_LABEL_TYPE_1_VALUES!r}"
    )
