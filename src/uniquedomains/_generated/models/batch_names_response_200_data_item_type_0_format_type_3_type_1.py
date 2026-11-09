from typing import Literal

BatchNamesResponse200DataItemType0FormatType3Type1 = Literal["hack", "oneWord"]

BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_FORMAT_TYPE_3_TYPE_1_VALUES: set[
    BatchNamesResponse200DataItemType0FormatType3Type1
] = {
    "hack",
    "oneWord",
}


def check_batch_names_response_200_data_item_type_0_format_type_3_type_1(
    value: str,
) -> BatchNamesResponse200DataItemType0FormatType3Type1:
    if value in BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_FORMAT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_FORMAT_TYPE_3_TYPE_1_VALUES!r}"
    )
