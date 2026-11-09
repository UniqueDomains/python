from typing import Literal

ListMarketSalesSeriesKind = Literal["day", "month", "week"]

LIST_MARKET_SALES_SERIES_KIND_VALUES: set[ListMarketSalesSeriesKind] = {
    "day",
    "month",
    "week",
}


def check_list_market_sales_series_kind(value: str) -> ListMarketSalesSeriesKind:
    if value in LIST_MARKET_SALES_SERIES_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MARKET_SALES_SERIES_KIND_VALUES!r}"
    )
