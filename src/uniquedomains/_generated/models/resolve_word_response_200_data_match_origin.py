from typing import Literal

ResolveWordResponse200DataMatchOrigin = Literal["api", "dictionary", "review", "trend"]

RESOLVE_WORD_RESPONSE_200_DATA_MATCH_ORIGIN_VALUES: set[
    ResolveWordResponse200DataMatchOrigin
] = {
    "api",
    "dictionary",
    "review",
    "trend",
}


def check_resolve_word_response_200_data_match_origin(
    value: str,
) -> ResolveWordResponse200DataMatchOrigin:
    if value in RESOLVE_WORD_RESPONSE_200_DATA_MATCH_ORIGIN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESOLVE_WORD_RESPONSE_200_DATA_MATCH_ORIGIN_VALUES!r}"
    )
