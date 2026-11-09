from typing import Literal

ListWordFitsResponse200DataItemBasis = Literal["default", "rated"]

LIST_WORD_FITS_RESPONSE_200_DATA_ITEM_BASIS_VALUES: set[
    ListWordFitsResponse200DataItemBasis
] = {
    "default",
    "rated",
}


def check_list_word_fits_response_200_data_item_basis(
    value: str,
) -> ListWordFitsResponse200DataItemBasis:
    if value in LIST_WORD_FITS_RESPONSE_200_DATA_ITEM_BASIS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_WORD_FITS_RESPONSE_200_DATA_ITEM_BASIS_VALUES!r}"
    )
