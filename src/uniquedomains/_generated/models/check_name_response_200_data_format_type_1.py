from typing import Literal

CheckNameResponse200DataFormatType1 = Literal["hack", "oneWord"]

CHECK_NAME_RESPONSE_200_DATA_FORMAT_TYPE_1_VALUES: set[
    CheckNameResponse200DataFormatType1
] = {
    "hack",
    "oneWord",
}


def check_check_name_response_200_data_format_type_1(
    value: str,
) -> CheckNameResponse200DataFormatType1:
    if value in CHECK_NAME_RESPONSE_200_DATA_FORMAT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_200_DATA_FORMAT_TYPE_1_VALUES!r}"
    )
