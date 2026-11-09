from typing import Literal

GetDomainResponse200DataRatingBandType1 = Literal["niche", "prime", "strong", "thin"]

GET_DOMAIN_RESPONSE_200_DATA_RATING_BAND_TYPE_1_VALUES: set[
    GetDomainResponse200DataRatingBandType1
] = {
    "niche",
    "prime",
    "strong",
    "thin",
}


def check_get_domain_response_200_data_rating_band_type_1(
    value: str,
) -> GetDomainResponse200DataRatingBandType1:
    if value in GET_DOMAIN_RESPONSE_200_DATA_RATING_BAND_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_DOMAIN_RESPONSE_200_DATA_RATING_BAND_TYPE_1_VALUES!r}"
    )
