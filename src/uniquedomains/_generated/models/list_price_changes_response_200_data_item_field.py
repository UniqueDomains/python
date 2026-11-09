from typing import Literal

ListPriceChangesResponse200DataItemField = Literal["purchase", "renewal", "transfer"]

LIST_PRICE_CHANGES_RESPONSE_200_DATA_ITEM_FIELD_VALUES: set[
    ListPriceChangesResponse200DataItemField
] = {
    "purchase",
    "renewal",
    "transfer",
}


def check_list_price_changes_response_200_data_item_field(
    value: str,
) -> ListPriceChangesResponse200DataItemField:
    if value in LIST_PRICE_CHANGES_RESPONSE_200_DATA_ITEM_FIELD_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_PRICE_CHANGES_RESPONSE_200_DATA_ITEM_FIELD_VALUES!r}"
    )
