from typing import Literal

ListTldPhasesResponse200DataItemPhase = Literal[
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

LIST_TLD_PHASES_RESPONSE_200_DATA_ITEM_PHASE_VALUES: set[
    ListTldPhasesResponse200DataItemPhase
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


def check_list_tld_phases_response_200_data_item_phase(
    value: str,
) -> ListTldPhasesResponse200DataItemPhase:
    if value in LIST_TLD_PHASES_RESPONSE_200_DATA_ITEM_PHASE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLD_PHASES_RESPONSE_200_DATA_ITEM_PHASE_VALUES!r}"
    )
