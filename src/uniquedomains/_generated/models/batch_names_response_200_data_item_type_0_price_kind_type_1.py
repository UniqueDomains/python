from typing import Literal

BatchNamesResponse200DataItemType0PriceKindType1 = Literal[
    "aftermarket", "backorder", "premium", "registry"
]

BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_PRICE_KIND_TYPE_1_VALUES: set[
    BatchNamesResponse200DataItemType0PriceKindType1
] = {
    "aftermarket",
    "backorder",
    "premium",
    "registry",
}


def check_batch_names_response_200_data_item_type_0_price_kind_type_1(
    value: str,
) -> BatchNamesResponse200DataItemType0PriceKindType1:
    if value in BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_PRICE_KIND_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_PRICE_KIND_TYPE_1_VALUES!r}"
    )
