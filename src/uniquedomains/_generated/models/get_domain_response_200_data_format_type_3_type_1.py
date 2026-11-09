from typing import Literal

GetDomainResponse200DataFormatType3Type1 = Literal["hack", "oneWord"]

GET_DOMAIN_RESPONSE_200_DATA_FORMAT_TYPE_3_TYPE_1_VALUES: set[
    GetDomainResponse200DataFormatType3Type1
] = {
    "hack",
    "oneWord",
}


def check_get_domain_response_200_data_format_type_3_type_1(
    value: str,
) -> GetDomainResponse200DataFormatType3Type1:
    if value in GET_DOMAIN_RESPONSE_200_DATA_FORMAT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_DOMAIN_RESPONSE_200_DATA_FORMAT_TYPE_3_TYPE_1_VALUES!r}"
    )
