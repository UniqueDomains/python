from typing import Literal

CheckNameResponse200DataPriceKindType3Type1 = Literal[
    "aftermarket", "backorder", "premium", "registry"
]

CHECK_NAME_RESPONSE_200_DATA_PRICE_KIND_TYPE_3_TYPE_1_VALUES: set[
    CheckNameResponse200DataPriceKindType3Type1
] = {
    "aftermarket",
    "backorder",
    "premium",
    "registry",
}


def check_check_name_response_200_data_price_kind_type_3_type_1(
    value: str,
) -> CheckNameResponse200DataPriceKindType3Type1:
    if value in CHECK_NAME_RESPONSE_200_DATA_PRICE_KIND_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_200_DATA_PRICE_KIND_TYPE_3_TYPE_1_VALUES!r}"
    )
