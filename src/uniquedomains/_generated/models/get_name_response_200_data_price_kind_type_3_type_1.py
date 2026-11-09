from typing import Literal

GetNameResponse200DataPriceKindType3Type1 = Literal[
    "aftermarket", "backorder", "premium", "registry"
]

GET_NAME_RESPONSE_200_DATA_PRICE_KIND_TYPE_3_TYPE_1_VALUES: set[
    GetNameResponse200DataPriceKindType3Type1
] = {
    "aftermarket",
    "backorder",
    "premium",
    "registry",
}


def check_get_name_response_200_data_price_kind_type_3_type_1(
    value: str,
) -> GetNameResponse200DataPriceKindType3Type1:
    if value in GET_NAME_RESPONSE_200_DATA_PRICE_KIND_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_NAME_RESPONSE_200_DATA_PRICE_KIND_TYPE_3_TYPE_1_VALUES!r}"
    )
