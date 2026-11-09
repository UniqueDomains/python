from typing import Literal

ListDomainHacksResponse200DataItemFormatType2Type1 = Literal["hack", "oneWord"]

LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_FORMAT_TYPE_2_TYPE_1_VALUES: set[
    ListDomainHacksResponse200DataItemFormatType2Type1
] = {
    "hack",
    "oneWord",
}


def check_list_domain_hacks_response_200_data_item_format_type_2_type_1(
    value: str,
) -> ListDomainHacksResponse200DataItemFormatType2Type1:
    if value in LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_FORMAT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_FORMAT_TYPE_2_TYPE_1_VALUES!r}"
    )
