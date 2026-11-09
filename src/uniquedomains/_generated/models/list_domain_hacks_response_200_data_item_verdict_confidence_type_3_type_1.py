from typing import Literal

ListDomainHacksResponse200DataItemVerdictConfidenceType3Type1 = Literal[
    "high", "low", "medium"
]

LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_VERDICT_CONFIDENCE_TYPE_3_TYPE_1_VALUES: set[
    ListDomainHacksResponse200DataItemVerdictConfidenceType3Type1
] = {
    "high",
    "low",
    "medium",
}


def check_list_domain_hacks_response_200_data_item_verdict_confidence_type_3_type_1(
    value: str,
) -> ListDomainHacksResponse200DataItemVerdictConfidenceType3Type1:
    if (
        value
        in LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_VERDICT_CONFIDENCE_TYPE_3_TYPE_1_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_VERDICT_CONFIDENCE_TYPE_3_TYPE_1_VALUES!r}"
    )
