from typing import Literal

GetEventsIcsCategory = Literal[
    "brand_ip",
    "dns_governance",
    "domaining",
    "hosting_cloud",
    "other_tech",
    "security_privacy",
]

GET_EVENTS_ICS_CATEGORY_VALUES: set[GetEventsIcsCategory] = {
    "brand_ip",
    "dns_governance",
    "domaining",
    "hosting_cloud",
    "other_tech",
    "security_privacy",
}


def check_get_events_ics_category(value: str) -> GetEventsIcsCategory:
    if value in GET_EVENTS_ICS_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_EVENTS_ICS_CATEGORY_VALUES!r}"
    )
