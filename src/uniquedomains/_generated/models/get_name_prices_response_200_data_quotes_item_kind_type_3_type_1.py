from typing import Literal

GetNamePricesResponse200DataQuotesItemKindType3Type1 = Literal[
    "aftermarket", "backorder", "registry"
]

GET_NAME_PRICES_RESPONSE_200_DATA_QUOTES_ITEM_KIND_TYPE_3_TYPE_1_VALUES: set[
    GetNamePricesResponse200DataQuotesItemKindType3Type1
] = {
    "aftermarket",
    "backorder",
    "registry",
}


def check_get_name_prices_response_200_data_quotes_item_kind_type_3_type_1(
    value: str,
) -> GetNamePricesResponse200DataQuotesItemKindType3Type1:
    if value in GET_NAME_PRICES_RESPONSE_200_DATA_QUOTES_ITEM_KIND_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_NAME_PRICES_RESPONSE_200_DATA_QUOTES_ITEM_KIND_TYPE_3_TYPE_1_VALUES!r}"
    )
