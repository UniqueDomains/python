from typing import Literal

ListDomainHacksResponse200DataItemShapeType3Type1 = Literal[
    "acronym", "phrase", "properNoun", "single", "twoWords"
]

LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_SHAPE_TYPE_3_TYPE_1_VALUES: set[
    ListDomainHacksResponse200DataItemShapeType3Type1
] = {
    "acronym",
    "phrase",
    "properNoun",
    "single",
    "twoWords",
}


def check_list_domain_hacks_response_200_data_item_shape_type_3_type_1(
    value: str,
) -> ListDomainHacksResponse200DataItemShapeType3Type1:
    if value in LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_SHAPE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_SHAPE_TYPE_3_TYPE_1_VALUES!r}"
    )
