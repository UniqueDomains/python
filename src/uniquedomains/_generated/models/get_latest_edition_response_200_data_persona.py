from typing import Literal

GetLatestEditionResponse200DataPersona = Literal["founder", "investor"]

GET_LATEST_EDITION_RESPONSE_200_DATA_PERSONA_VALUES: set[
    GetLatestEditionResponse200DataPersona
] = {
    "founder",
    "investor",
}


def check_get_latest_edition_response_200_data_persona(
    value: str,
) -> GetLatestEditionResponse200DataPersona:
    if value in GET_LATEST_EDITION_RESPONSE_200_DATA_PERSONA_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LATEST_EDITION_RESPONSE_200_DATA_PERSONA_VALUES!r}"
    )
