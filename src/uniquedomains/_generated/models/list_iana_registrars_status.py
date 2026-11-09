from typing import Literal

ListIanaRegistrarsStatus = Literal["accredited", "reserved", "terminated"]

LIST_IANA_REGISTRARS_STATUS_VALUES: set[ListIanaRegistrarsStatus] = {
    "accredited",
    "reserved",
    "terminated",
}


def check_list_iana_registrars_status(value: str) -> ListIanaRegistrarsStatus:
    if value in LIST_IANA_REGISTRARS_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_IANA_REGISTRARS_STATUS_VALUES!r}"
    )
