from typing import Literal

ListDomainsResponse200DataItemFormatType3Type1 = Literal["hack", "oneWord"]

LIST_DOMAINS_RESPONSE_200_DATA_ITEM_FORMAT_TYPE_3_TYPE_1_VALUES: set[
    ListDomainsResponse200DataItemFormatType3Type1
] = {
    "hack",
    "oneWord",
}


def check_list_domains_response_200_data_item_format_type_3_type_1(
    value: str,
) -> ListDomainsResponse200DataItemFormatType3Type1:
    if value in LIST_DOMAINS_RESPONSE_200_DATA_ITEM_FORMAT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAINS_RESPONSE_200_DATA_ITEM_FORMAT_TYPE_3_TYPE_1_VALUES!r}"
    )
