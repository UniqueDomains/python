from typing import Literal

ListTldApplicationsType = Literal["brand", "community", "geographic", "standard"]

LIST_TLD_APPLICATIONS_TYPE_VALUES: set[ListTldApplicationsType] = {
    "brand",
    "community",
    "geographic",
    "standard",
}


def check_list_tld_applications_type(value: str) -> ListTldApplicationsType:
    if value in LIST_TLD_APPLICATIONS_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLD_APPLICATIONS_TYPE_VALUES!r}"
    )
