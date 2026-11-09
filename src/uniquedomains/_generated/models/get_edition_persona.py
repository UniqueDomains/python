from typing import Literal

GetEditionPersona = Literal["founder", "investor"]

GET_EDITION_PERSONA_VALUES: set[GetEditionPersona] = {
    "founder",
    "investor",
}


def check_get_edition_persona(value: str) -> GetEditionPersona:
    if value in GET_EDITION_PERSONA_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_EDITION_PERSONA_VALUES!r}"
    )
