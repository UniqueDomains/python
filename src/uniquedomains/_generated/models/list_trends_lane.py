from typing import Literal

ListTrendsLane = Literal["weekly", "yearly"]

LIST_TRENDS_LANE_VALUES: set[ListTrendsLane] = {
    "weekly",
    "yearly",
}


def check_list_trends_lane(value: str) -> ListTrendsLane:
    if value in LIST_TRENDS_LANE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TRENDS_LANE_VALUES!r}"
    )
