from typing import Literal

ListTrendsSort = Literal["day", "slug"]

LIST_TRENDS_SORT_VALUES: set[ListTrendsSort] = {
    "day",
    "slug",
}


def check_list_trends_sort(value: str) -> ListTrendsSort:
    if value in LIST_TRENDS_SORT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TRENDS_SORT_VALUES!r}"
    )
