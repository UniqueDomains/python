from typing import Literal

ListRegistrarChangesRegistrar = Literal[
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

LIST_REGISTRAR_CHANGES_REGISTRAR_VALUES: set[ListRegistrarChangesRegistrar] = {
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


def check_list_registrar_changes_registrar(value: str) -> ListRegistrarChangesRegistrar:
    if value in LIST_REGISTRAR_CHANGES_REGISTRAR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_REGISTRAR_CHANGES_REGISTRAR_VALUES!r}"
    )
