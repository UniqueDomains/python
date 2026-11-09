from typing import Literal

CheckNameResponse202DataCompsTierType2Type1 = Literal[
    "market", "related", "same_word", "sold_before", "synonyms"
]

CHECK_NAME_RESPONSE_202_DATA_COMPS_TIER_TYPE_2_TYPE_1_VALUES: set[
    CheckNameResponse202DataCompsTierType2Type1
] = {
    "market",
    "related",
    "same_word",
    "sold_before",
    "synonyms",
}


def check_check_name_response_202_data_comps_tier_type_2_type_1(
    value: str,
) -> CheckNameResponse202DataCompsTierType2Type1:
    if value in CHECK_NAME_RESPONSE_202_DATA_COMPS_TIER_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_202_DATA_COMPS_TIER_TYPE_2_TYPE_1_VALUES!r}"
    )
