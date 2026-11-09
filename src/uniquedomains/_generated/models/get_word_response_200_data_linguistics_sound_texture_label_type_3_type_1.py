from typing import Literal

GetWordResponse200DataLinguisticsSoundTextureLabelType3Type1 = Literal[
    "balanced", "sharp", "soft"
]

GET_WORD_RESPONSE_200_DATA_LINGUISTICS_SOUND_TEXTURE_LABEL_TYPE_3_TYPE_1_VALUES: set[
    GetWordResponse200DataLinguisticsSoundTextureLabelType3Type1
] = {
    "balanced",
    "sharp",
    "soft",
}


def check_get_word_response_200_data_linguistics_sound_texture_label_type_3_type_1(
    value: str,
) -> GetWordResponse200DataLinguisticsSoundTextureLabelType3Type1:
    if (
        value
        in GET_WORD_RESPONSE_200_DATA_LINGUISTICS_SOUND_TEXTURE_LABEL_TYPE_3_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WORD_RESPONSE_200_DATA_LINGUISTICS_SOUND_TEXTURE_LABEL_TYPE_3_TYPE_1_VALUES!r}"
    )
