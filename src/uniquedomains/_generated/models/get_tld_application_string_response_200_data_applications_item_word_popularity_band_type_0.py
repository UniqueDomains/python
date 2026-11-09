from typing import Literal

GetTldApplicationStringResponse200DataApplicationsItemWordPopularityBandType0 = Literal[
    "high", "low", "medium"
]

GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_APPLICATIONS_ITEM_WORD_POPULARITY_BAND_TYPE_0_VALUES: set[
    GetTldApplicationStringResponse200DataApplicationsItemWordPopularityBandType0
] = {
    "high",
    "low",
    "medium",
}


def check_get_tld_application_string_response_200_data_applications_item_word_popularity_band_type_0(
    value: str,
) -> GetTldApplicationStringResponse200DataApplicationsItemWordPopularityBandType0:
    if (
        value
        in GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_APPLICATIONS_ITEM_WORD_POPULARITY_BAND_TYPE_0_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_APPLICATIONS_ITEM_WORD_POPULARITY_BAND_TYPE_0_VALUES!r}"
    )
