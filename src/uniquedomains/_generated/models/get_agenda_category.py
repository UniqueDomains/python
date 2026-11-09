from typing import Literal

GetAgendaCategory = Literal[
    "brand_ip",
    "dns_governance",
    "domaining",
    "hosting_cloud",
    "launches",
    "other_tech",
    "security_privacy",
]

GET_AGENDA_CATEGORY_VALUES: set[GetAgendaCategory] = {
    "brand_ip",
    "dns_governance",
    "domaining",
    "hosting_cloud",
    "launches",
    "other_tech",
    "security_privacy",
}


def check_get_agenda_category(value: str) -> GetAgendaCategory:
    if value in GET_AGENDA_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_AGENDA_CATEGORY_VALUES!r}"
    )
