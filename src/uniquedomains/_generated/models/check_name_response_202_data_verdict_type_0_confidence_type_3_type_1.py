from typing import Literal

CheckNameResponse202DataVerdictType0ConfidenceType3Type1 = Literal[
    "high", "low", "medium"
]

CHECK_NAME_RESPONSE_202_DATA_VERDICT_TYPE_0_CONFIDENCE_TYPE_3_TYPE_1_VALUES: set[
    CheckNameResponse202DataVerdictType0ConfidenceType3Type1
] = {
    "high",
    "low",
    "medium",
}


def check_check_name_response_202_data_verdict_type_0_confidence_type_3_type_1(
    value: str,
) -> CheckNameResponse202DataVerdictType0ConfidenceType3Type1:
    if (
        value
        in CHECK_NAME_RESPONSE_202_DATA_VERDICT_TYPE_0_CONFIDENCE_TYPE_3_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_202_DATA_VERDICT_TYPE_0_CONFIDENCE_TYPE_3_TYPE_1_VALUES!r}"
    )
