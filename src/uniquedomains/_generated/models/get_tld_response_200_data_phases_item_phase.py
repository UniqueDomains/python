from typing import Literal

GetTldResponse200DataPhasesItemPhase = Literal[
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

GET_TLD_RESPONSE_200_DATA_PHASES_ITEM_PHASE_VALUES: set[
    GetTldResponse200DataPhasesItemPhase
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


def check_get_tld_response_200_data_phases_item_phase(
    value: str,
) -> GetTldResponse200DataPhasesItemPhase:
    if value in GET_TLD_RESPONSE_200_DATA_PHASES_ITEM_PHASE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TLD_RESPONSE_200_DATA_PHASES_ITEM_PHASE_VALUES!r}"
    )
