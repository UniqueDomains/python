from typing import Literal

BatchNamesResponse200DataItemType0NameLabelType0Type = Literal[
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

BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_NAME_LABEL_TYPE_0_TYPE_VALUES: set[
    BatchNamesResponse200DataItemType0NameLabelType0Type
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


def check_batch_names_response_200_data_item_type_0_name_label_type_0_type(
    value: str,
) -> BatchNamesResponse200DataItemType0NameLabelType0Type:
    if value in BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_NAME_LABEL_TYPE_0_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_NAMES_RESPONSE_200_DATA_ITEM_TYPE_0_NAME_LABEL_TYPE_0_TYPE_VALUES!r}"
    )
