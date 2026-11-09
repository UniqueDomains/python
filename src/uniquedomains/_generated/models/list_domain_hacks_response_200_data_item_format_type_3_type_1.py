from typing import Literal

ListDomainHacksResponse200DataItemFormatType3Type1 = Literal["hack", "oneWord"]

LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_FORMAT_TYPE_3_TYPE_1_VALUES: set[
    ListDomainHacksResponse200DataItemFormatType3Type1
] = {
    "hack",
    "oneWord",
}


def check_list_domain_hacks_response_200_data_item_format_type_3_type_1(
    value: str,
) -> ListDomainHacksResponse200DataItemFormatType3Type1:
    if value in LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_FORMAT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_FORMAT_TYPE_3_TYPE_1_VALUES!r}"
    )
