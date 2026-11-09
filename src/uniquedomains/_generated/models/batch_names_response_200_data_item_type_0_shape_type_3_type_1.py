from typing import Literal

BatchNamesResponse200DataItemType0ShapeType3Type1 = Literal[
    "acronym", "phrase", "properNoun", "single", "twoWords"
]

BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_SHAPE_TYPE_3_TYPE_1_VALUES: set[
    BatchNamesResponse200DataItemType0ShapeType3Type1
] = {
    "acronym",
    "phrase",
    "properNoun",
    "single",
    "twoWords",
}


def check_batch_names_response_200_data_item_type_0_shape_type_3_type_1(
    value: str,
) -> BatchNamesResponse200DataItemType0ShapeType3Type1:
    if value in BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_SHAPE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_SHAPE_TYPE_3_TYPE_1_VALUES!r}"
    )
