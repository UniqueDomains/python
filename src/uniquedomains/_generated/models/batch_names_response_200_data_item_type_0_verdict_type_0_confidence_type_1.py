from typing import Literal

BatchNamesResponse200DataItemType0VerdictType0ConfidenceType1 = Literal[
    "high", "low", "medium"
]

BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_VERDICT_TYPE_0_CONFIDENCE_TYPE_1_VALUES: set[
    BatchNamesResponse200DataItemType0VerdictType0ConfidenceType1
] = {
    "high",
    "low",
    "medium",
}


def check_batch_names_response_200_data_item_type_0_verdict_type_0_confidence_type_1(
    value: str,
) -> BatchNamesResponse200DataItemType0VerdictType0ConfidenceType1:
    if (
        value
        in BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_VERDICT_TYPE_0_CONFIDENCE_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_VERDICT_TYPE_0_CONFIDENCE_TYPE_1_VALUES!r}"
    )
