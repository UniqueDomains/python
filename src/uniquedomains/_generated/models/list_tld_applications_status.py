from typing import Literal

ListTldApplicationsStatus = Literal[
    "early_warning", "initial_evaluation", "objection_filed", "withdrawn"
]

LIST_TLD_APPLICATIONS_STATUS_VALUES: set[ListTldApplicationsStatus] = {
    "early_warning",
    "initial_evaluation",
    "objection_filed",
    "withdrawn",
}


def check_list_tld_applications_status(value: str) -> ListTldApplicationsStatus:
    if value in LIST_TLD_APPLICATIONS_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLD_APPLICATIONS_STATUS_VALUES!r}"
    )
