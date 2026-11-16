from typing import Literal

CheckNameResponse200DataCrossLanguageFlagType2Type1 = Literal[
    "avoid", "caution", "none"
]

CHECK_NAME_RESPONSE_200_DATA_CROSS_LANGUAGE_FLAG_TYPE_2_TYPE_1_VALUES: set[
    CheckNameResponse200DataCrossLanguageFlagType2Type1
] = {
    "avoid",
    "caution",
    "none",
}


def check_check_name_response_200_data_cross_language_flag_type_2_type_1(
    value: str,
) -> CheckNameResponse200DataCrossLanguageFlagType2Type1:
    if value in CHECK_NAME_RESPONSE_200_DATA_CROSS_LANGUAGE_FLAG_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_200_DATA_CROSS_LANGUAGE_FLAG_TYPE_2_TYPE_1_VALUES!r}"
    )
