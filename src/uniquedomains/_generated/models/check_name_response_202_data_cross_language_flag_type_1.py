from typing import Literal

CheckNameResponse202DataCrossLanguageFlagType1 = Literal["avoid", "caution", "none"]

CHECK_NAME_RESPONSE_202_DATA_CROSS_LANGUAGE_FLAG_TYPE_1_VALUES: set[
    CheckNameResponse202DataCrossLanguageFlagType1
] = {
    "avoid",
    "caution",
    "none",
}


def check_check_name_response_202_data_cross_language_flag_type_1(
    value: str,
) -> CheckNameResponse202DataCrossLanguageFlagType1:
    if value in CHECK_NAME_RESPONSE_202_DATA_CROSS_LANGUAGE_FLAG_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_202_DATA_CROSS_LANGUAGE_FLAG_TYPE_1_VALUES!r}"
    )
