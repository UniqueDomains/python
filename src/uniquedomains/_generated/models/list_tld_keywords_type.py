from typing import Literal

ListTldKeywordsType = Literal[
    "activity", "audience", "intent", "lexical", "location", "semantic", "tone"
]

LIST_TLD_KEYWORDS_TYPE_VALUES: set[ListTldKeywordsType] = {
    "activity",
    "audience",
    "intent",
    "lexical",
    "location",
    "semantic",
    "tone",
}


def check_list_tld_keywords_type(value: str) -> ListTldKeywordsType:
    if value in LIST_TLD_KEYWORDS_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLD_KEYWORDS_TYPE_VALUES!r}"
    )
