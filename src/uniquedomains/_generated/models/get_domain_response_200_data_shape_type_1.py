from typing import Literal

GetDomainResponse200DataShapeType1 = Literal[
    "acronym", "phrase", "properNoun", "single", "twoWords"
]

GET_DOMAIN_RESPONSE_200_DATA_SHAPE_TYPE_1_VALUES: set[
    GetDomainResponse200DataShapeType1
] = {
    "acronym",
    "phrase",
    "properNoun",
    "single",
    "twoWords",
}


def check_get_domain_response_200_data_shape_type_1(
    value: str,
) -> GetDomainResponse200DataShapeType1:
    if value in GET_DOMAIN_RESPONSE_200_DATA_SHAPE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_DOMAIN_RESPONSE_200_DATA_SHAPE_TYPE_1_VALUES!r}"
    )
