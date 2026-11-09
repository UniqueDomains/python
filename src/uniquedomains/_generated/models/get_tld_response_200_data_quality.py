from typing import Literal

GetTldResponse200DataQuality = Literal["niche", "prime", "strong", "thin"]

GET_TLD_RESPONSE_200_DATA_QUALITY_VALUES: set[GetTldResponse200DataQuality] = {
    "niche",
    "prime",
    "strong",
    "thin",
}


def check_get_tld_response_200_data_quality(value: str) -> GetTldResponse200DataQuality:
    if value in GET_TLD_RESPONSE_200_DATA_QUALITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TLD_RESPONSE_200_DATA_QUALITY_VALUES!r}"
    )
