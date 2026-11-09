from typing import Literal

ListTldApplicationsContention = Literal["none", "set"]

LIST_TLD_APPLICATIONS_CONTENTION_VALUES: set[ListTldApplicationsContention] = {
    "none",
    "set",
}


def check_list_tld_applications_contention(value: str) -> ListTldApplicationsContention:
    if value in LIST_TLD_APPLICATIONS_CONTENTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLD_APPLICATIONS_CONTENTION_VALUES!r}"
    )
