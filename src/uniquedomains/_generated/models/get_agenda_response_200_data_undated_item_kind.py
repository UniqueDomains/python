from typing import Literal

GetAgendaResponse200DataUndatedItemKind = Literal[
    "industry_event", "tld_change", "tld_phase"
]

GET_AGENDA_RESPONSE_200_DATA_UNDATED_ITEM_KIND_VALUES: set[
    GetAgendaResponse200DataUndatedItemKind
] = {
    "industry_event",
    "tld_change",
    "tld_phase",
}


def check_get_agenda_response_200_data_undated_item_kind(
    value: str,
) -> GetAgendaResponse200DataUndatedItemKind:
    if value in GET_AGENDA_RESPONSE_200_DATA_UNDATED_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_AGENDA_RESPONSE_200_DATA_UNDATED_ITEM_KIND_VALUES!r}"
    )
