from typing import Literal

GetNameResponse200DataVerdictType0Rating = Literal["good", "risky", "strong", "unrated"]

GET_NAME_RESPONSE_200_DATA_VERDICT_TYPE_0_RATING_VALUES: set[
    GetNameResponse200DataVerdictType0Rating
] = {
    "good",
    "risky",
    "strong",
    "unrated",
}


def check_get_name_response_200_data_verdict_type_0_rating(
    value: str,
) -> GetNameResponse200DataVerdictType0Rating:
    if value in GET_NAME_RESPONSE_200_DATA_VERDICT_TYPE_0_RATING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_NAME_RESPONSE_200_DATA_VERDICT_TYPE_0_RATING_VALUES!r}"
    )
