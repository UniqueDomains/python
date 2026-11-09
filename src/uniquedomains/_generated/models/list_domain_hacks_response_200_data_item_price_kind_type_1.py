from typing import Literal

ListDomainHacksResponse200DataItemPriceKindType1 = Literal[
    "auction", "backorder", "marketplace", "premium", "registration"
]

LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_PRICE_KIND_TYPE_1_VALUES: set[
    ListDomainHacksResponse200DataItemPriceKindType1
] = {
    "auction",
    "backorder",
    "marketplace",
    "premium",
    "registration",
}


def check_list_domain_hacks_response_200_data_item_price_kind_type_1(
    value: str,
) -> ListDomainHacksResponse200DataItemPriceKindType1:
    if value in LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_PRICE_KIND_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAIN_HACKS_RESPONSE_200_DATA_ITEM_PRICE_KIND_TYPE_1_VALUES!r}"
    )
