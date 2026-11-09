from typing import Literal

GetEditionResponse200DataTrendsItemRowsItemVerdictType0Label = Literal[
    "good", "risky", "strong"
]

GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_VERDICT_TYPE_0_LABEL_VALUES: set[
    GetEditionResponse200DataTrendsItemRowsItemVerdictType0Label
] = {
    "good",
    "risky",
    "strong",
}


def check_get_edition_response_200_data_trends_item_rows_item_verdict_type_0_label(
    value: str,
) -> GetEditionResponse200DataTrendsItemRowsItemVerdictType0Label:
    if (
        value
        in GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_VERDICT_TYPE_0_LABEL_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_EDITION_RESPONSE_200_DATA_TRENDS_ITEM_ROWS_ITEM_VERDICT_TYPE_0_LABEL_VALUES!r}"
    )
