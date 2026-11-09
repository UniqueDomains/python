from typing import Literal

GetMetaFreshnessResponse200DataLanesItemState = Literal["completed", "running"]

GET_META_FRESHNESS_RESPONSE_200_DATA_LANES_ITEM_STATE_VALUES: set[
    GetMetaFreshnessResponse200DataLanesItemState
] = {
    "completed",
    "running",
}


def check_get_meta_freshness_response_200_data_lanes_item_state(
    value: str,
) -> GetMetaFreshnessResponse200DataLanesItemState:
    if value in GET_META_FRESHNESS_RESPONSE_200_DATA_LANES_ITEM_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_META_FRESHNESS_RESPONSE_200_DATA_LANES_ITEM_STATE_VALUES!r}"
    )
