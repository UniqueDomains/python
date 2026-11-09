from typing import Literal

ListTldsResponse200DataItemKind = Literal["root", "second_level", "web3"]

LIST_TLDS_RESPONSE_200_DATA_ITEM_KIND_VALUES: set[ListTldsResponse200DataItemKind] = {
    "root",
    "second_level",
    "web3",
}


def check_list_tlds_response_200_data_item_kind(
    value: str,
) -> ListTldsResponse200DataItemKind:
    if value in LIST_TLDS_RESPONSE_200_DATA_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLDS_RESPONSE_200_DATA_ITEM_KIND_VALUES!r}"
    )
