from typing import Literal

GetTldApplicationStringResponse200DataApplicationsItemComparableSalesBandType0 = (
    Literal["high", "low", "medium", "none"]
)

GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_APPLICATIONS_ITEM_COMPARABLE_SALES_BAND_TYPE_0_VALUES: set[
    GetTldApplicationStringResponse200DataApplicationsItemComparableSalesBandType0
] = {
    "high",
    "low",
    "medium",
    "none",
}


def check_get_tld_application_string_response_200_data_applications_item_comparable_sales_band_type_0(
    value: str,
) -> GetTldApplicationStringResponse200DataApplicationsItemComparableSalesBandType0:
    if (
        value
        in GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_APPLICATIONS_ITEM_COMPARABLE_SALES_BAND_TYPE_0_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TLD_APPLICATION_STRING_RESPONSE_200_DATA_APPLICATIONS_ITEM_COMPARABLE_SALES_BAND_TYPE_0_VALUES!r}"
    )
