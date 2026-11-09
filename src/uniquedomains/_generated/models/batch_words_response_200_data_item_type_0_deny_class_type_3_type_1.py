from typing import Literal

BatchWordsResponse200DataItemType0DenyClassType3Type1 = Literal[
    "brand", "controversy", "harm", "person", "politics", "trademark", "vice"
]

BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_DENY_CLASS_TYPE_3_TYPE_1_VALUES: set[
    BatchWordsResponse200DataItemType0DenyClassType3Type1
] = {
    "brand",
    "controversy",
    "harm",
    "person",
    "politics",
    "trademark",
    "vice",
}


def check_batch_words_response_200_data_item_type_0_deny_class_type_3_type_1(
    value: str,
) -> BatchWordsResponse200DataItemType0DenyClassType3Type1:
    if (
        value
        in BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_DENY_CLASS_TYPE_3_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_DENY_CLASS_TYPE_3_TYPE_1_VALUES!r}"
    )
