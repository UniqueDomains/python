from typing import Literal

GetNameResponse200DataRatingBandType3Type1 = Literal["niche", "prime", "strong", "thin"]

GET_NAME_RESPONSE_200_DATA_RATING_BAND_TYPE_3_TYPE_1_VALUES: set[
    GetNameResponse200DataRatingBandType3Type1
] = {
    "niche",
    "prime",
    "strong",
    "thin",
}


def check_get_name_response_200_data_rating_band_type_3_type_1(
    value: str,
) -> GetNameResponse200DataRatingBandType3Type1:
    if value in GET_NAME_RESPONSE_200_DATA_RATING_BAND_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_NAME_RESPONSE_200_DATA_RATING_BAND_TYPE_3_TYPE_1_VALUES!r}"
    )
