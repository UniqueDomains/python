from typing import Literal

CheckNameResponse200DataShapeType1 = Literal[
    "acronym", "phrase", "properNoun", "single", "twoWords"
]

CHECK_NAME_RESPONSE_200_DATA_SHAPE_TYPE_1_VALUES: set[
    CheckNameResponse200DataShapeType1
] = {
    "acronym",
    "phrase",
    "properNoun",
    "single",
    "twoWords",
}


def check_check_name_response_200_data_shape_type_1(
    value: str,
) -> CheckNameResponse200DataShapeType1:
    if value in CHECK_NAME_RESPONSE_200_DATA_SHAPE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_200_DATA_SHAPE_TYPE_1_VALUES!r}"
    )
