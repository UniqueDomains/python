from typing import Literal

ListDomainsResponse200DataItemRatingBandType3Type1 = Literal[
    "niche", "prime", "strong", "thin"
]

LIST_DOMAINS_RESPONSE_200_DATA_ITEM_RATING_BAND_TYPE_3_TYPE_1_VALUES: set[
    ListDomainsResponse200DataItemRatingBandType3Type1
] = {
    "niche",
    "prime",
    "strong",
    "thin",
}


def check_list_domains_response_200_data_item_rating_band_type_3_type_1(
    value: str,
) -> ListDomainsResponse200DataItemRatingBandType3Type1:
    if value in LIST_DOMAINS_RESPONSE_200_DATA_ITEM_RATING_BAND_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DOMAINS_RESPONSE_200_DATA_ITEM_RATING_BAND_TYPE_3_TYPE_1_VALUES!r}"
    )
