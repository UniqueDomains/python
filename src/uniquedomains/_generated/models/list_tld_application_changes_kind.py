from typing import Literal

ListTldApplicationChangesKind = Literal["contention_set", "status"]

LIST_TLD_APPLICATION_CHANGES_KIND_VALUES: set[ListTldApplicationChangesKind] = {
    "contention_set",
    "status",
}


def check_list_tld_application_changes_kind(
    value: str,
) -> ListTldApplicationChangesKind:
    if value in LIST_TLD_APPLICATION_CHANGES_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLD_APPLICATION_CHANGES_KIND_VALUES!r}"
    )
