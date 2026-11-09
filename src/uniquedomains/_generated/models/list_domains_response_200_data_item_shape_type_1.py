from typing import Literal

ListDomainsResponse200DataItemShapeType1 = Literal[
    "acronym", "phrase", "properNoun", "single", "twoWords"
]

LIST_DOMAINS_RESPONSE_200_DATA_ITEM_SHAPE_TYPE_1_VALUES: set[
    ListDomainsResponse200DataItemShapeType1
] = {
    "acronym",
    "phrase",
    "properNoun",
    "single",
    "twoWords",
}


def check_list_domains_response_200_data_item_shape_type_1(
    value: str,
) -> ListDomainsResponse200DataItemShapeType1:
    if value in LIST_DOMAINS_RESPONSE_200_DATA_ITEM_SHAPE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAINS_RESPONSE_200_DATA_ITEM_SHAPE_TYPE_1_VALUES!r}"
    )
