from typing import Literal

GetDomainResponse200DataVerdictType0Rating = Literal[
    "good", "risky", "strong", "unrated"
]

GET_DOMAIN_RESPONSE_200_DATA_VERDICT_TYPE_0_RATING_VALUES: set[
    GetDomainResponse200DataVerdictType0Rating
] = {
    "good",
    "risky",
    "strong",
    "unrated",
}


def check_get_domain_response_200_data_verdict_type_0_rating(
    value: str,
) -> GetDomainResponse200DataVerdictType0Rating:
    if value in GET_DOMAIN_RESPONSE_200_DATA_VERDICT_TYPE_0_RATING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_DOMAIN_RESPONSE_200_DATA_VERDICT_TYPE_0_RATING_VALUES!r}"
    )
