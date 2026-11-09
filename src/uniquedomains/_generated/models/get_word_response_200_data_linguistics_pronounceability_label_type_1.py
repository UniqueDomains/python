from typing import Literal

GetWordResponse200DataLinguisticsPronounceabilityLabelType1 = Literal[
    "easy", "hard", "medium"
]

GET_WORD_RESPONSE_200_DATA_LINGUISTICS_PRONOUNCEABILITY_LABEL_TYPE_1_VALUES: set[
    GetWordResponse200DataLinguisticsPronounceabilityLabelType1
] = {
    "easy",
    "hard",
    "medium",
}


def check_get_word_response_200_data_linguistics_pronounceability_label_type_1(
    value: str,
) -> GetWordResponse200DataLinguisticsPronounceabilityLabelType1:
    if (
        value
        in GET_WORD_RESPONSE_200_DATA_LINGUISTICS_PRONOUNCEABILITY_LABEL_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WORD_RESPONSE_200_DATA_LINGUISTICS_PRONOUNCEABILITY_LABEL_TYPE_1_VALUES!r}"
    )
