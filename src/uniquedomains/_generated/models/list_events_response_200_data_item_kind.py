from typing import Literal

ListEventsResponse200DataItemKind = Literal["industry_event"]

LIST_EVENTS_RESPONSE_200_DATA_ITEM_KIND_VALUES: set[
    ListEventsResponse200DataItemKind
] = {
    "industry_event",
}


def check_list_events_response_200_data_item_kind(
    value: str,
) -> ListEventsResponse200DataItemKind:
    if value in LIST_EVENTS_RESPONSE_200_DATA_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_EVENTS_RESPONSE_200_DATA_ITEM_KIND_VALUES!r}"
    )
