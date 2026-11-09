from typing import Literal

GetWordResponse200DataStyleType3Type1 = Literal[
    "elegant", "futuristic", "handwritten", "modern", "playful", "slab"
]

GET_WORD_RESPONSE_200_DATA_STYLE_TYPE_3_TYPE_1_VALUES: set[
    GetWordResponse200DataStyleType3Type1
] = {
    "elegant",
    "futuristic",
    "handwritten",
    "modern",
    "playful",
    "slab",
}


def check_get_word_response_200_data_style_type_3_type_1(
    value: str,
) -> GetWordResponse200DataStyleType3Type1:
    if value in GET_WORD_RESPONSE_200_DATA_STYLE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WORD_RESPONSE_200_DATA_STYLE_TYPE_3_TYPE_1_VALUES!r}"
    )
