from typing import Literal

BatchNamesResponse200DataItemType0CrossLanguageFlagType2Type1 = Literal[
    "avoid", "caution", "none"
]

BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_CROSS_LANGUAGE_FLAG_TYPE_2_TYPE_1_VALUES: set[
    BatchNamesResponse200DataItemType0CrossLanguageFlagType2Type1
] = {
    "avoid",
    "caution",
    "none",
}


def check_batch_names_response_200_data_item_type_0_cross_language_flag_type_2_type_1(
    value: str,
) -> BatchNamesResponse200DataItemType0CrossLanguageFlagType2Type1:
    if (
        value
        in BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_CROSS_LANGUAGE_FLAG_TYPE_2_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_CROSS_LANGUAGE_FLAG_TYPE_2_TYPE_1_VALUES!r}"
    )
