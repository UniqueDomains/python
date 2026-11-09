from typing import Literal

ListDomainsResponse200DataItemVerdictRating = Literal[
    "good", "risky", "strong", "unrated"
]

LIST_DOMAINS_RESPONSE_200_DATA_ITEM_VERDICT_RATING_VALUES: set[
    ListDomainsResponse200DataItemVerdictRating
] = {
    "good",
    "risky",
    "strong",
    "unrated",
}


def check_list_domains_response_200_data_item_verdict_rating(
    value: str,
) -> ListDomainsResponse200DataItemVerdictRating:
    if value in LIST_DOMAINS_RESPONSE_200_DATA_ITEM_VERDICT_RATING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAINS_RESPONSE_200_DATA_ITEM_VERDICT_RATING_VALUES!r}"
    )
