from typing import Literal

GetKeyResponse200DataPlanType3Type1 = Literal["founder", "investor"]

GET_KEY_RESPONSE_200_DATA_PLAN_TYPE_3_TYPE_1_VALUES: set[
    GetKeyResponse200DataPlanType3Type1
] = {
    "founder",
    "investor",
}


def check_get_key_response_200_data_plan_type_3_type_1(
    value: str,
) -> GetKeyResponse200DataPlanType3Type1:
    if value in GET_KEY_RESPONSE_200_DATA_PLAN_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_KEY_RESPONSE_200_DATA_PLAN_TYPE_3_TYPE_1_VALUES!r}"
    )
