from typing import Literal

ListDomainChangesResponse200DataItemSubjectKind = Literal["name"]

LIST_DOMAIN_CHANGES_RESPONSE_200_DATA_ITEM_SUBJECT_KIND_VALUES: set[
    ListDomainChangesResponse200DataItemSubjectKind
] = {
    "name",
}


def check_list_domain_changes_response_200_data_item_subject_kind(
    value: str,
) -> ListDomainChangesResponse200DataItemSubjectKind:
    if value in LIST_DOMAIN_CHANGES_RESPONSE_200_DATA_ITEM_SUBJECT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAIN_CHANGES_RESPONSE_200_DATA_ITEM_SUBJECT_KIND_VALUES!r}"
    )
