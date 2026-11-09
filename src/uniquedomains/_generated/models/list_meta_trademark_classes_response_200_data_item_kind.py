from typing import Literal

ListMetaTrademarkClassesResponse200DataItemKind = Literal["goods", "services"]

LIST_META_TRADEMARK_CLASSES_RESPONSE_200_DATA_ITEM_KIND_VALUES: set[
    ListMetaTrademarkClassesResponse200DataItemKind
] = {
    "goods",
    "services",
}


def check_list_meta_trademark_classes_response_200_data_item_kind(
    value: str,
) -> ListMetaTrademarkClassesResponse200DataItemKind:
    if value in LIST_META_TRADEMARK_CLASSES_RESPONSE_200_DATA_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_META_TRADEMARK_CLASSES_RESPONSE_200_DATA_ITEM_KIND_VALUES!r}"
    )
