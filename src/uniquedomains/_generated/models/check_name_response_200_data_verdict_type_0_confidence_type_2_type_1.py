from typing import Literal

CheckNameResponse200DataVerdictType0ConfidenceType2Type1 = Literal[
    "high", "low", "medium"
]

CHECK_NAME_RESPONSE_200_DATA_VERDICT_TYPE_0_CONFIDENCE_TYPE_2_TYPE_1_VALUES: set[
    CheckNameResponse200DataVerdictType0ConfidenceType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_check_name_response_200_data_verdict_type_0_confidence_type_2_type_1(
    value: str,
) -> CheckNameResponse200DataVerdictType0ConfidenceType2Type1:
    if (
        value
        in CHECK_NAME_RESPONSE_200_DATA_VERDICT_TYPE_0_CONFIDENCE_TYPE_2_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_200_DATA_VERDICT_TYPE_0_CONFIDENCE_TYPE_2_TYPE_1_VALUES!r}"
    )
