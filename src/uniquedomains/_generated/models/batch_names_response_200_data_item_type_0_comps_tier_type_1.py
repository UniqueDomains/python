from typing import Literal

BatchNamesResponse200DataItemType0CompsTierType1 = Literal[
    "market", "related", "same_word", "sold_before", "synonyms"
]

BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_COMPS_TIER_TYPE_1_VALUES: set[
    BatchNamesResponse200DataItemType0CompsTierType1
] = {
    "market",
    "related",
    "same_word",
    "sold_before",
    "synonyms",
}


def check_batch_names_response_200_data_item_type_0_comps_tier_type_1(
    value: str,
) -> BatchNamesResponse200DataItemType0CompsTierType1:
    if value in BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_COMPS_TIER_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_COMPS_TIER_TYPE_1_VALUES!r}"
    )
