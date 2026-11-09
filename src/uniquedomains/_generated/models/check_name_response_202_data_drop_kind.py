from typing import Literal

CheckNameResponse202DataDropKind = Literal["date", "none"]

CHECK_NAME_RESPONSE_202_DATA_DROP_KIND_VALUES: set[CheckNameResponse202DataDropKind] = {
    "date",
    "none",
}


def check_check_name_response_202_data_drop_kind(
    value: str,
) -> CheckNameResponse202DataDropKind:
    if value in CHECK_NAME_RESPONSE_202_DATA_DROP_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_202_DATA_DROP_KIND_VALUES!r}"
    )
