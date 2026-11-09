from typing import Literal

ListTldsIanaStatus = Literal["delegated", "never_delegated", "removed"]

LIST_TLDS_IANA_STATUS_VALUES: set[ListTldsIanaStatus] = {
    "delegated",
    "never_delegated",
    "removed",
}


def check_list_tlds_iana_status(value: str) -> ListTldsIanaStatus:
    if value in LIST_TLDS_IANA_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLDS_IANA_STATUS_VALUES!r}"
    )
