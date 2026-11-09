from typing import Literal

BatchNamesResponse200DataItemType0DropKind = Literal["date", "none"]

BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_DROP_KIND_VALUES: set[
    BatchNamesResponse200DataItemType0DropKind
] = {
    "date",
    "none",
}


def check_batch_names_response_200_data_item_type_0_drop_kind(
    value: str,
) -> BatchNamesResponse200DataItemType0DropKind:
    if value in BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_DROP_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_DROP_KIND_VALUES!r}"
    )
