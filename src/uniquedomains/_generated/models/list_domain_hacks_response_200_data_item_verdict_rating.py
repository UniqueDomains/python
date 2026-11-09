from typing import Literal

ListDomainHacksResponse200DataItemVerdictRating = Literal[
    "good", "risky", "strong", "unrated"
]

LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_VERDICT_RATING_VALUES: set[
    ListDomainHacksResponse200DataItemVerdictRating
] = {
    "good",
    "risky",
    "strong",
    "unrated",
}


def check_list_domain_hacks_response_200_data_item_verdict_rating(
    value: str,
) -> ListDomainHacksResponse200DataItemVerdictRating:
    if value in LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_VERDICT_RATING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_VERDICT_RATING_VALUES!r}"
    )
