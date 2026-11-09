from typing import Literal

BatchNamesResponse200DataItemType2Error = Literal["validation_failed"]

BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_2_ERROR_VALUES: set[
    BatchNamesResponse200DataItemType2Error
] = {
    "validation_failed",
}


def check_batch_names_response_200_data_item_type_2_error(
    value: str,
) -> BatchNamesResponse200DataItemType2Error:
    if value in BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_2_ERROR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_2_ERROR_VALUES!r}"
    )
