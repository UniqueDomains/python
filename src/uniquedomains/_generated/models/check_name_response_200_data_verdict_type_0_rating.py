from typing import Literal

CheckNameResponse200DataVerdictType0Rating = Literal[
    "good", "risky", "strong", "unrated"
]

CHECK_NAME_RESPONSE_200_DATA_VERDICT_TYPE_0_RATING_VALUES: set[
    CheckNameResponse200DataVerdictType0Rating
] = {
    "good",
    "risky",
    "strong",
    "unrated",
}


def check_check_name_response_200_data_verdict_type_0_rating(
    value: str,
) -> CheckNameResponse200DataVerdictType0Rating:
    if value in CHECK_NAME_RESPONSE_200_DATA_VERDICT_TYPE_0_RATING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_200_DATA_VERDICT_TYPE_0_RATING_VALUES!r}"
    )
