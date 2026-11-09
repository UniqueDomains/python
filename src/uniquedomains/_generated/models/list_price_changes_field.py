from typing import Literal

ListPriceChangesField = Literal["purchase", "renewal", "transfer"]

LIST_PRICE_CHANGES_FIELD_VALUES: set[ListPriceChangesField] = {
    "purchase",
    "renewal",
    "transfer",
}


def check_list_price_changes_field(value: str) -> ListPriceChangesField:
    if value in LIST_PRICE_CHANGES_FIELD_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_PRICE_CHANGES_FIELD_VALUES!r}"
    )
