from typing import Literal

ListTldApplicationsResponse200DataItemWordPopularityBandType0 = Literal[
    "high", "low", "medium"
]

LIST_TLD_APPLICATIONS_RESPONSE_200_DATA_ITEM_WORD_POPULARITY_BAND_TYPE_0_VALUES: set[
    ListTldApplicationsResponse200DataItemWordPopularityBandType0
] = {
    "high",
    "low",
    "medium",
}


def check_list_tld_applications_response_200_data_item_word_popularity_band_type_0(
    value: str,
) -> ListTldApplicationsResponse200DataItemWordPopularityBandType0:
    if (
        value
        in LIST_TLD_APPLICATIONS_RESPONSE_200_DATA_ITEM_WORD_POPULARITY_BAND_TYPE_0_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLD_APPLICATIONS_RESPONSE_200_DATA_ITEM_WORD_POPULARITY_BAND_TYPE_0_VALUES!r}"
    )
