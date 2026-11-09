from typing import Literal

CheckNameResponse200DataDropKind = Literal["date", "none"]

CHECK_NAME_RESPONSE_200_DATA_DROP_KIND_VALUES: set[CheckNameResponse200DataDropKind] = {
    "date",
    "none",
}


def check_check_name_response_200_data_drop_kind(
    value: str,
) -> CheckNameResponse200DataDropKind:
    if value in CHECK_NAME_RESPONSE_200_DATA_DROP_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_200_DATA_DROP_KIND_VALUES!r}"
    )
