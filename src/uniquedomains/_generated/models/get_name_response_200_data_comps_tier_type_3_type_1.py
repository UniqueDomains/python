from typing import Literal

GetNameResponse200DataCompsTierType3Type1 = Literal[
    "market", "related", "same_word", "sold_before", "synonyms"
]

GET_NAME_RESPONSE_200_DATA_COMPS_TIER_TYPE_3_TYPE_1_VALUES: set[
    GetNameResponse200DataCompsTierType3Type1
] = {
    "market",
    "related",
    "same_word",
    "sold_before",
    "synonyms",
}


def check_get_name_response_200_data_comps_tier_type_3_type_1(
    value: str,
) -> GetNameResponse200DataCompsTierType3Type1:
    if value in GET_NAME_RESPONSE_200_DATA_COMPS_TIER_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_NAME_RESPONSE_200_DATA_COMPS_TIER_TYPE_3_TYPE_1_VALUES!r}"
    )
