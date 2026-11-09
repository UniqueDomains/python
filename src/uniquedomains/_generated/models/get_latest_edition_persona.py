from typing import Literal

GetLatestEditionPersona = Literal["founder", "investor"]

GET_LATEST_EDITION_PERSONA_VALUES: set[GetLatestEditionPersona] = {
    "founder",
    "investor",
}


def check_get_latest_edition_persona(value: str) -> GetLatestEditionPersona:
    if value in GET_LATEST_EDITION_PERSONA_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LATEST_EDITION_PERSONA_VALUES!r}"
    )
