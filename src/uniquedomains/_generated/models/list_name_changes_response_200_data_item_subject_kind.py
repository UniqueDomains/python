from typing import Literal

ListNameChangesResponse200DataItemSubjectKind = Literal["name"]

LIST_NAME_CHANGES_RESPONSE_200_DATA_ITEM_SUBJECT_KIND_VALUES: set[
    ListNameChangesResponse200DataItemSubjectKind
] = {
    "name",
}


def check_list_name_changes_response_200_data_item_subject_kind(
    value: str,
) -> ListNameChangesResponse200DataItemSubjectKind:
    if value in LIST_NAME_CHANGES_RESPONSE_200_DATA_ITEM_SUBJECT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_NAME_CHANGES_RESPONSE_200_DATA_ITEM_SUBJECT_KIND_VALUES!r}"
    )
