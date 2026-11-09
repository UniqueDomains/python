from typing import Literal

GetWordResponse200DataLinguisticsPronunciationConfidenceType3Type1 = Literal[
    "high", "low", "medium"
]

GET_WORD_RESPONSE_200_DATA_LINGUISTICS_PRONUNCIATION_CONFIDENCE_TYPE_3_TYPE_1_VALUES: set[
    GetWordResponse200DataLinguisticsPronunciationConfidenceType3Type1
] = {
    "high",
    "low",
    "medium",
}


def check_get_word_response_200_data_linguistics_pronunciation_confidence_type_3_type_1(
    value: str,
) -> GetWordResponse200DataLinguisticsPronunciationConfidenceType3Type1:
    if (
        value
        in GET_WORD_RESPONSE_200_DATA_LINGUISTICS_PRONUNCIATION_CONFIDENCE_TYPE_3_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WORD_RESPONSE_200_DATA_LINGUISTICS_PRONUNCIATION_CONFIDENCE_TYPE_3_TYPE_1_VALUES!r}"
    )
