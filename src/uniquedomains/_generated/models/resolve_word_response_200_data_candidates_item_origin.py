from typing import Literal

ResolveWordResponse200DataCandidatesItemOrigin = Literal[
    "api", "dictionary", "review", "trend"
]

RESOLVE_WORD_RESPONSE_200_DATA_CANDIDATES_ITEM_ORIGIN_VALUES: set[
    ResolveWordResponse200DataCandidatesItemOrigin
] = {
    "api",
    "dictionary",
    "review",
    "trend",
}


def check_resolve_word_response_200_data_candidates_item_origin(
    value: str,
) -> ResolveWordResponse200DataCandidatesItemOrigin:
    if value in RESOLVE_WORD_RESPONSE_200_DATA_CANDIDATES_ITEM_ORIGIN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESOLVE_WORD_RESPONSE_200_DATA_CANDIDATES_ITEM_ORIGIN_VALUES!r}"
    )
