from typing import Literal

GetNameResponse200DataFormatType1 = Literal["hack", "oneWord"]

GET_NAME_RESPONSE_200_DATA_FORMAT_TYPE_1_VALUES: set[
    GetNameResponse200DataFormatType1
] = {
    "hack",
    "oneWord",
}


def check_get_name_response_200_data_format_type_1(
    value: str,
) -> GetNameResponse200DataFormatType1:
    if value in GET_NAME_RESPONSE_200_DATA_FORMAT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_NAME_RESPONSE_200_DATA_FORMAT_TYPE_1_VALUES!r}"
    )
