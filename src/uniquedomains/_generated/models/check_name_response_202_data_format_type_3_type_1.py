from typing import Literal

CheckNameResponse202DataFormatType3Type1 = Literal["hack", "oneWord"]

CHECK_NAME_RESPONSE_202_DATA_FORMAT_TYPE_3_TYPE_1_VALUES: set[
    CheckNameResponse202DataFormatType3Type1
] = {
    "hack",
    "oneWord",
}


def check_check_name_response_202_data_format_type_3_type_1(
    value: str,
) -> CheckNameResponse202DataFormatType3Type1:
    if value in CHECK_NAME_RESPONSE_202_DATA_FORMAT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_202_DATA_FORMAT_TYPE_3_TYPE_1_VALUES!r}"
    )
