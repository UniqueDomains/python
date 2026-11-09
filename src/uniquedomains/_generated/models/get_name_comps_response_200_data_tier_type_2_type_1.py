from typing import Literal

GetNameCompsResponse200DataTierType2Type1 = Literal[
    "market", "related", "same_word", "sold_before", "synonyms"
]

GET_NAME_COMPS_RESPONSE_200_DATA_TIER_TYPE_2_TYPE_1_VALUES: set[
    GetNameCompsResponse200DataTierType2Type1
] = {
    "market",
    "related",
    "same_word",
    "sold_before",
    "synonyms",
}


def check_get_name_comps_response_200_data_tier_type_2_type_1(
    value: str,
) -> GetNameCompsResponse200DataTierType2Type1:
    if value in GET_NAME_COMPS_RESPONSE_200_DATA_TIER_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_NAME_COMPS_RESPONSE_200_DATA_TIER_TYPE_2_TYPE_1_VALUES!r}"
    )
