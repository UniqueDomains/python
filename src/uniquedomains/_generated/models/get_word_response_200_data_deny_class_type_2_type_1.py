from typing import Literal

GetWordResponse200DataDenyClassType2Type1 = Literal[
    "brand", "controversy", "harm", "person", "politics", "trademark", "vice"
]

GET_WORD_RESPONSE_200_DATA_DENY_CLASS_TYPE_2_TYPE_1_VALUES: set[
    GetWordResponse200DataDenyClassType2Type1
] = {
    "brand",
    "controversy",
    "harm",
    "person",
    "politics",
    "trademark",
    "vice",
}


def check_get_word_response_200_data_deny_class_type_2_type_1(
    value: str,
) -> GetWordResponse200DataDenyClassType2Type1:
    if value in GET_WORD_RESPONSE_200_DATA_DENY_CLASS_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WORD_RESPONSE_200_DATA_DENY_CLASS_TYPE_2_TYPE_1_VALUES!r}"
    )
