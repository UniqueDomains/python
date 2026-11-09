from typing import Literal

ListPriceChangesRegistrar = Literal[
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

LIST_PRICE_CHANGES_REGISTRAR_VALUES: set[ListPriceChangesRegistrar] = {
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


def check_list_price_changes_registrar(value: str) -> ListPriceChangesRegistrar:
    if value in LIST_PRICE_CHANGES_REGISTRAR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_PRICE_CHANGES_REGISTRAR_VALUES!r}"
    )
