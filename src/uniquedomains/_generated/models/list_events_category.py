from typing import Literal

ListEventsCategory = Literal[
    "brand_ip",
    "dns_governance",
    "domaining",
    "hosting_cloud",
    "other_tech",
    "security_privacy",
]

LIST_EVENTS_CATEGORY_VALUES: set[ListEventsCategory] = {
    "brand_ip",
    "dns_governance",
    "domaining",
    "hosting_cloud",
    "other_tech",
    "security_privacy",
}


def check_list_events_category(value: str) -> ListEventsCategory:
    if value in LIST_EVENTS_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_EVENTS_CATEGORY_VALUES!r}"
    )
