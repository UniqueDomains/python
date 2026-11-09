from typing import Literal

ListRelatedWordsResponse200DataItemRelation = Literal["related", "synonym"]

LIST_RELATED_WORDS_RESPONSE_200_DATA_ITEM_RELATION_VALUES: set[
    ListRelatedWordsResponse200DataItemRelation
] = {
    "related",
    "synonym",
}


def check_list_related_words_response_200_data_item_relation(
    value: str,
) -> ListRelatedWordsResponse200DataItemRelation:
    if value in LIST_RELATED_WORDS_RESPONSE_200_DATA_ITEM_RELATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_RELATED_WORDS_RESPONSE_200_DATA_ITEM_RELATION_VALUES!r}"
    )
