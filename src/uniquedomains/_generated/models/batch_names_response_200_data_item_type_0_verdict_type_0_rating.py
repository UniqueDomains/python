from typing import Literal

BatchNamesResponse200DataItemType0VerdictType0Rating = Literal[
    "good", "risky", "strong", "unrated"
]

BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_VERDICT_TYPE_0_RATING_VALUES: set[
    BatchNamesResponse200DataItemType0VerdictType0Rating
] = {
    "good",
    "risky",
    "strong",
    "unrated",
}


def check_batch_names_response_200_data_item_type_0_verdict_type_0_rating(
    value: str,
) -> BatchNamesResponse200DataItemType0VerdictType0Rating:
    if value in BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_VERDICT_TYPE_0_RATING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_VERDICT_TYPE_0_RATING_VALUES!r}"
    )
