from typing import Literal

GetWordResponse200DataLinguisticsSpellingLabelType1 = Literal["high", "low", "medium"]

GET_WORD_RESPONSE_200_DATA_LINGUISTICS_SPELLING_LABEL_TYPE_1_VALUES: set[
    GetWordResponse200DataLinguisticsSpellingLabelType1
] = {
    "high",
    "low",
    "medium",
}


def check_get_word_response_200_data_linguistics_spelling_label_type_1(
    value: str,
) -> GetWordResponse200DataLinguisticsSpellingLabelType1:
    if value in GET_WORD_RESPONSE_200_DATA_LINGUISTICS_SPELLING_LABEL_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WORD_RESPONSE_200_DATA_LINGUISTICS_SPELLING_LABEL_TYPE_1_VALUES!r}"
    )
