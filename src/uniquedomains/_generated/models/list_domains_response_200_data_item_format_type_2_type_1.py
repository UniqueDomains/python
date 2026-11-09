from typing import Literal

ListDomainsResponse200DataItemFormatType2Type1 = Literal["hack", "oneWord"]

LIST_DOMAINS_RESPONSE_200_DATA_ITEM_FORMAT_TYPE_2_TYPE_1_VALUES: set[
    ListDomainsResponse200DataItemFormatType2Type1
] = {
    "hack",
    "oneWord",
}


def check_list_domains_response_200_data_item_format_type_2_type_1(
    value: str,
) -> ListDomainsResponse200DataItemFormatType2Type1:
    if value in LIST_DOMAINS_RESPONSE_200_DATA_ITEM_FORMAT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAINS_RESPONSE_200_DATA_ITEM_FORMAT_TYPE_2_TYPE_1_VALUES!r}"
    )
