from typing import Literal

GetNameResponse200DataCrossLanguageFlagType3Type1 = Literal["avoid", "caution", "none"]

GET_NAME_RESPONSE_200_DATA_CROSS_LANGUAGE_FLAG_TYPE_3_TYPE_1_VALUES: set[
    GetNameResponse200DataCrossLanguageFlagType3Type1
] = {
    "avoid",
    "caution",
    "none",
}


def check_get_name_response_200_data_cross_language_flag_type_3_type_1(
    value: str,
) -> GetNameResponse200DataCrossLanguageFlagType3Type1:
    if value in GET_NAME_RESPONSE_200_DATA_CROSS_LANGUAGE_FLAG_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_NAME_RESPONSE_200_DATA_CROSS_LANGUAGE_FLAG_TYPE_3_TYPE_1_VALUES!r}"
    )
