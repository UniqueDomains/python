from typing import Literal

BatchNamesResponse200DataItemType0RatingBandType1 = Literal[
    "niche", "prime", "strong", "thin"
]

BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_RATING_BAND_TYPE_1_VALUES: set[
    BatchNamesResponse200DataItemType0RatingBandType1
] = {
    "niche",
    "prime",
    "strong",
    "thin",
}


def check_batch_names_response_200_data_item_type_0_rating_band_type_1(
    value: str,
) -> BatchNamesResponse200DataItemType0RatingBandType1:
    if value in BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_RATING_BAND_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_RATING_BAND_TYPE_1_VALUES!r}"
    )
