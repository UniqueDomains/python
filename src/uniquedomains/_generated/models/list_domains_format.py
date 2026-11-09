from typing import Literal

ListDomainsFormat = Literal["hack", "oneWord"]

LIST_DOMAINS_FORMAT_VALUES: set[ListDomainsFormat] = {
    "hack",
    "oneWord",
}


def check_list_domains_format(value: str) -> ListDomainsFormat:
    if value in LIST_DOMAINS_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAINS_FORMAT_VALUES!r}"
    )
