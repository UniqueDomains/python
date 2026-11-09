from typing import Literal

BatchWordsResponse200DataItemType0LinguisticsSoundTextureLabelType3Type1 = Literal[
    "balanced", "sharp", "soft"
]

BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_LINGUISTICS_SOUND_TEXTURE_LABEL_TYPE_3_TYPE_1_VALUES: set[
    BatchWordsResponse200DataItemType0LinguisticsSoundTextureLabelType3Type1
] = {
    "balanced",
    "sharp",
    "soft",
}


def check_batch_words_response_200_data_item_type_0_linguistics_sound_texture_label_type_3_type_1(
    value: str,
) -> BatchWordsResponse200DataItemType0LinguisticsSoundTextureLabelType3Type1:
    if (
        value
        in BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_LINGUISTICS_SOUND_TEXTURE_LABEL_TYPE_3_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_WORDS_RESPONSE_200_DATA_ITEM_TYPE_0_LINGUISTICS_SOUND_TEXTURE_LABEL_TYPE_3_TYPE_1_VALUES!r}"
    )
