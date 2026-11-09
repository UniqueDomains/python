from typing import Literal

CheckNameResponse200DataCompsTierType1 = Literal[
    "market", "related", "same_word", "sold_before", "synonyms"
]

CHECK_NAME_RESPONSE_200_DATA_COMPS_TIER_TYPE_1_VALUES: set[
    CheckNameResponse200DataCompsTierType1
] = {
    "market",
    "related",
    "same_word",
    "sold_before",
    "synonyms",
}


def check_check_name_response_200_data_comps_tier_type_1(
    value: str,
) -> CheckNameResponse200DataCompsTierType1:
    if value in CHECK_NAME_RESPONSE_200_DATA_COMPS_TIER_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_200_DATA_COMPS_TIER_TYPE_1_VALUES!r}"
    )
