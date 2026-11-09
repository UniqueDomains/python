from typing import Literal

GetEditionResponse200DataPersona = Literal["founder", "investor"]

GET_EDITION_RESPONSE_200_DATA_PERSONA_VALUES: set[GetEditionResponse200DataPersona] = {
    "founder",
    "investor",
}


def check_get_edition_response_200_data_persona(
    value: str,
) -> GetEditionResponse200DataPersona:
    if value in GET_EDITION_RESPONSE_200_DATA_PERSONA_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_EDITION_RESPONSE_200_DATA_PERSONA_VALUES!r}"
    )
