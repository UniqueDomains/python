from typing import Literal

GetDomainResponse200DataNameLabelType0Type = Literal[
    "acronym",
    "blend",
    "brand_like",
    "coinage",
    "compound",
    "dictionary_word",
    "inflected_word",
    "misspelling",
    "numeric_or_junk",
    "personal_name",
    "phrase",
    "place_name",
]

GET_DOMAIN_RESPONSE_200_DATA_NAME_LABEL_TYPE_0_TYPE_VALUES: set[
    GetDomainResponse200DataNameLabelType0Type
] = {
    "acronym",
    "blend",
    "brand_like",
    "coinage",
    "compound",
    "dictionary_word",
    "inflected_word",
    "misspelling",
    "numeric_or_junk",
    "personal_name",
    "phrase",
    "place_name",
}


def check_get_domain_response_200_data_name_label_type_0_type(
    value: str,
) -> GetDomainResponse200DataNameLabelType0Type:
    if value in GET_DOMAIN_RESPONSE_200_DATA_NAME_LABEL_TYPE_0_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_DOMAIN_RESPONSE_200_DATA_NAME_LABEL_TYPE_0_TYPE_VALUES!r}"
    )
