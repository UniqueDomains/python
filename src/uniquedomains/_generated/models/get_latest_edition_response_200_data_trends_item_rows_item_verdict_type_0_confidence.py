from typing import Literal

GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0Confidence = Literal[
    "high", "low", "medium"
]

GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_VERDICT_TYPE_0_CONFIDENCE_VALUES: set[
    GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0Confidence
] = {
    "high",
    "low",
    "medium",
}


def check_get_latest_edition_response_200_data_trends_item_rows_item_verdict_type_0_confidence(
    value: str,
) -> GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0Confidence:
    if (
        value
        in GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_VERDICT_TYPE_0_CONFIDENCE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LATEST_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_VERDICT_TYPE_0_CONFIDENCE_VALUES!r}"
    )
