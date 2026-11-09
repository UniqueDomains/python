from typing import Literal

ListRegistrarPricesRegistrar = Literal[
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

LIST_REGISTRAR_PRICES_REGISTRAR_VALUES: set[ListRegistrarPricesRegistrar] = {
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


def check_list_registrar_prices_registrar(value: str) -> ListRegistrarPricesRegistrar:
    if value in LIST_REGISTRAR_PRICES_REGISTRAR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_REGISTRAR_PRICES_REGISTRAR_VALUES!r}"
    )
