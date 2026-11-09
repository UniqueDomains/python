from typing import Literal

CheckNameResponse202DataPriceKindType1 = Literal[
    "aftermarket", "backorder", "premium", "registry"
]

CHECK_NAME_RESPONSE_202_DATA_PRICE_KIND_TYPE_1_VALUES: set[
    CheckNameResponse202DataPriceKindType1
] = {
    "aftermarket",
    "backorder",
    "premium",
    "registry",
}


def check_check_name_response_202_data_price_kind_type_1(
    value: str,
) -> CheckNameResponse202DataPriceKindType1:
    if value in CHECK_NAME_RESPONSE_202_DATA_PRICE_KIND_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_202_DATA_PRICE_KIND_TYPE_1_VALUES!r}"
    )
