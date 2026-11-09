from typing import Literal

GetAgendaResponse200DataEntriesItemKind = Literal[
    "industry_event", "tld_change", "tld_phase"
]

GET_AGENDA_RESPONSE_200_DATA_ENTRIES_ITEM_KIND_VALUES: set[
    GetAgendaResponse200DataEntriesItemKind
] = {
    "industry_event",
    "tld_change",
    "tld_phase",
}


def check_get_agenda_response_200_data_entries_item_kind(
    value: str,
) -> GetAgendaResponse200DataEntriesItemKind:
    if value in GET_AGENDA_RESPONSE_200_DATA_ENTRIES_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_AGENDA_RESPONSE_200_DATA_ENTRIES_ITEM_KIND_VALUES!r}"
    )
