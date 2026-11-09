from typing import Literal

ListTldApplicationsSales = Literal["high", "low", "medium", "none"]

LIST_TLD_APPLICATIONS_SALES_VALUES: set[ListTldApplicationsSales] = {
    "high",
    "low",
    "medium",
    "none",
}


def check_list_tld_applications_sales(value: str) -> ListTldApplicationsSales:
    if value in LIST_TLD_APPLICATIONS_SALES_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLD_APPLICATIONS_SALES_VALUES!r}"
    )
