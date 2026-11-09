from typing import Literal

ListDomainsResponse200DataItemPriceKindType1 = Literal[
    "auction", "backorder", "marketplace", "premium", "registration"
]

LIST_DOMAINS_RESPONSE_200_DATA_ITEM_PRICE_KIND_TYPE_1_VALUES: set[
    ListDomainsResponse200DataItemPriceKindType1
] = {
    "auction",
    "backorder",
    "marketplace",
    "premium",
    "registration",
}


def check_list_domains_response_200_data_item_price_kind_type_1(
    value: str,
) -> ListDomainsResponse200DataItemPriceKindType1:
    if value in LIST_DOMAINS_RESPONSE_200_DATA_ITEM_PRICE_KIND_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAINS_RESPONSE_200_DATA_ITEM_PRICE_KIND_TYPE_1_VALUES!r}"
    )
