from typing import Literal

GetNameResponse200DataVerdictType0ConfidenceType2Type1 = Literal[
    "high", "low", "medium"
]

GET_NAME_RESPONSE_200_DATA_VERDICT_TYPE_0_CONFIDENCE_TYPE_2_TYPE_1_VALUES: set[
    GetNameResponse200DataVerdictType0ConfidenceType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_get_name_response_200_data_verdict_type_0_confidence_type_2_type_1(
    value: str,
) -> GetNameResponse200DataVerdictType0ConfidenceType2Type1:
    if (
        value
        in GET_NAME_RESPONSE_200_DATA_VERDICT_TYPE_0_CONFIDENCE_TYPE_2_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_NAME_RESPONSE_200_DATA_VERDICT_TYPE_0_CONFIDENCE_TYPE_2_TYPE_1_VALUES!r}"
    )
