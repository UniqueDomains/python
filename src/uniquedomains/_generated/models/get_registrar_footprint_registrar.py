from typing import Literal

GetRegistrarFootprintRegistrar = Literal[
    "cloudflare",
    "dynadot",
    "godaddy",
    "name.com",
    "namecheap",
    "namesilo",
    "porkbun",
    "spaceship",
    "unstoppable",
]

GET_REGISTRAR_FOOTPRINT_REGISTRAR_VALUES: set[GetRegistrarFootprintRegistrar] = {
    "cloudflare",
    "dynadot",
    "godaddy",
    "name.com",
    "namecheap",
    "namesilo",
    "porkbun",
    "spaceship",
    "unstoppable",
}


def check_get_registrar_footprint_registrar(
    value: str,
) -> GetRegistrarFootprintRegistrar:
    if value in GET_REGISTRAR_FOOTPRINT_REGISTRAR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_REGISTRAR_FOOTPRINT_REGISTRAR_VALUES!r}"
    )
