from typing import Literal

ResolveWordResponse200DataMatchVia = Literal[
    "accent", "case", "exact", "inflected", "lookalike", "two_words"
]

RESOLVE_WORD_RESPONSE_200_DATA_MATCH_VIA_VALUES: set[
    ResolveWordResponse200DataMatchVia
] = {
    "accent",
    "case",
    "exact",
    "inflected",
    "lookalike",
    "two_words",
}


def check_resolve_word_response_200_data_match_via(
    value: str,
) -> ResolveWordResponse200DataMatchVia:
    if value in RESOLVE_WORD_RESPONSE_200_DATA_MATCH_VIA_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESOLVE_WORD_RESPONSE_200_DATA_MATCH_VIA_VALUES!r}"
    )
