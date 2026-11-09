from typing import Literal

ResolveWordResponse200DataMatchShapeType2Type1 = Literal[
    "acronym", "phrase", "properNoun", "single", "twoWords"
]

RESOLVE_WORD_RESPONSE_200_DATA_MATCH_SHAPE_TYPE_2_TYPE_1_VALUES: set[
    ResolveWordResponse200DataMatchShapeType2Type1
] = {
    "acronym",
    "phrase",
    "properNoun",
    "single",
    "twoWords",
}


def check_resolve_word_response_200_data_match_shape_type_2_type_1(
    value: str,
) -> ResolveWordResponse200DataMatchShapeType2Type1:
    if value in RESOLVE_WORD_RESPONSE_200_DATA_MATCH_SHAPE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESOLVE_WORD_RESPONSE_200_DATA_MATCH_SHAPE_TYPE_2_TYPE_1_VALUES!r}"
    )
