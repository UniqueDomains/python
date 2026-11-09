from typing import Literal

CheckNameResponse202DataShapeType2Type1 = Literal[
    "acronym", "phrase", "properNoun", "single", "twoWords"
]

CHECK_NAME_RESPONSE_202_DATA_SHAPE_TYPE_2_TYPE_1_VALUES: set[
    CheckNameResponse202DataShapeType2Type1
] = {
    "acronym",
    "phrase",
    "properNoun",
    "single",
    "twoWords",
}


def check_check_name_response_202_data_shape_type_2_type_1(
    value: str,
) -> CheckNameResponse202DataShapeType2Type1:
    if value in CHECK_NAME_RESPONSE_202_DATA_SHAPE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_202_DATA_SHAPE_TYPE_2_TYPE_1_VALUES!r}"
    )
