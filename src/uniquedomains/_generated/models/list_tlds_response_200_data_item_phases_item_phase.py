from typing import Literal

ListTldsResponse200DataItemPhasesItemPhase = Literal[
    "approved_launch",
    "claims",
    "contract_termination",
    "delegation",
    "exclusive_registration",
    "general_availability",
    "limited_registration",
    "qualified_launch",
    "removal",
    "sunrise",
]

LIST_TLDS_RESPONSE_200_DATA_ITEM_PHASES_ITEM_PHASE_VALUES: set[
    ListTldsResponse200DataItemPhasesItemPhase
] = {
    "approved_launch",
    "claims",
    "contract_termination",
    "delegation",
    "exclusive_registration",
    "general_availability",
    "limited_registration",
    "qualified_launch",
    "removal",
    "sunrise",
}


def check_list_tlds_response_200_data_item_phases_item_phase(
    value: str,
) -> ListTldsResponse200DataItemPhasesItemPhase:
    if value in LIST_TLDS_RESPONSE_200_DATA_ITEM_PHASES_ITEM_PHASE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLDS_RESPONSE_200_DATA_ITEM_PHASES_ITEM_PHASE_VALUES!r}"
    )
