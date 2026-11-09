from typing import Literal

ListTldApplicationsPop = Literal["high", "low", "medium"]

LIST_TLD_APPLICATIONS_POP_VALUES: set[ListTldApplicationsPop] = {
    "high",
    "low",
    "medium",
}


def check_list_tld_applications_pop(value: str) -> ListTldApplicationsPop:
    if value in LIST_TLD_APPLICATIONS_POP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLD_APPLICATIONS_POP_VALUES!r}"
    )
