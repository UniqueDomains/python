from typing import Literal

GetKeyResponse200DataSubscriptionType1 = Literal[
    "BASIC", "CUSTOM", "MEGA", "PRO", "ULTRA"
]

GET_KEY_RESPONSE_200_DATA_SUBSCRIPTION_TYPE_1_VALUES: set[
    GetKeyResponse200DataSubscriptionType1
] = {
    "BASIC",
    "CUSTOM",
    "MEGA",
    "PRO",
    "ULTRA",
}


def check_get_key_response_200_data_subscription_type_1(
    value: str,
) -> GetKeyResponse200DataSubscriptionType1:
    if value in GET_KEY_RESPONSE_200_DATA_SUBSCRIPTION_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_KEY_RESPONSE_200_DATA_SUBSCRIPTION_TYPE_1_VALUES!r}"
    )
