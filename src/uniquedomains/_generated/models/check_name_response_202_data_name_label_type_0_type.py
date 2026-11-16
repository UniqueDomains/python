from typing import Literal

CheckNameResponse202DataNameLabelType0Type = Literal[
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

CHECK_NAME_RESPONSE_202_DATA_NAME_LABEL_TYPE_0_TYPE_VALUES: set[
    CheckNameResponse202DataNameLabelType0Type
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


def check_check_name_response_202_data_name_label_type_0_type(
    value: str,
) -> CheckNameResponse202DataNameLabelType0Type:
    if value in CHECK_NAME_RESPONSE_202_DATA_NAME_LABEL_TYPE_0_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_NAME_RESPONSE_202_DATA_NAME_LABEL_TYPE_0_TYPE_VALUES!r}"
    )
