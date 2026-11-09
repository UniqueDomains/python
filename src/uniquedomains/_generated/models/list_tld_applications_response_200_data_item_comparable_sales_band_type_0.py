from typing import Literal

ListTldApplicationsResponse200DataItemComparableSalesBandType0 = Literal[
    "high", "low", "medium", "none"
]

LIST_TLD_APPLICATIONS_RESPONSE_200_DATA_ITEM_COMPARABLE_SALES_BAND_TYPE_0_VALUES: set[
    ListTldApplicationsResponse200DataItemComparableSalesBandType0
] = {
    "high",
    "low",
    "medium",
    "none",
}


def check_list_tld_applications_response_200_data_item_comparable_sales_band_type_0(
    value: str,
) -> ListTldApplicationsResponse200DataItemComparableSalesBandType0:
    if (
        value
        in LIST_TLD_APPLICATIONS_RESPONSE_200_DATA_ITEM_COMPARABLE_SALES_BAND_TYPE_0_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TLD_APPLICATIONS_RESPONSE_200_DATA_ITEM_COMPARABLE_SALES_BAND_TYPE_0_VALUES!r}"
    )
