from typing import Literal

CheckNameBodyBlocksItem = Literal[
    "availability", "dns", "history", "prices", "registry", "value"
]

CHECK_NAME_BODY_BLOCKS_ITEM_VALUES: set[CheckNameBodyBlocksItem] = {
    "availability",
    "dns",
    "history",
    "prices",
    "registry",
    "value",
}


def check_check_name_body_blocks_item(value: str) -> CheckNameBodyBlocksItem:
    if value in CHECK_NAME_BODY_BLOCKS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_BODY_BLOCKS_ITEM_VALUES!r}"
    )
