from typing import Literal

GetAgendaIcsCategory = Literal[
    "brand_ip",
    "dns_governance",
    "domaining",
    "hosting_cloud",
    "launches",
    "other_tech",
    "security_privacy",
]

GET_AGENDA_ICS_CATEGORY_VALUES: set[GetAgendaIcsCategory] = {
    "brand_ip",
    "dns_governance",
    "domaining",
    "hosting_cloud",
    "launches",
    "other_tech",
    "security_privacy",
}


def check_get_agenda_ics_category(value: str) -> GetAgendaIcsCategory:
    if value in GET_AGENDA_ICS_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_AGENDA_ICS_CATEGORY_VALUES!r}"
    )
