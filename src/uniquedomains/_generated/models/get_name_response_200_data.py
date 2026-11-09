from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_name_response_200_data_format_type_1 import (
    GetNameResponse200DataFormatType1,
    check_get_name_response_200_data_format_type_1,
)
from ..models.get_name_response_200_data_format_type_2_type_1 import (
    GetNameResponse200DataFormatType2Type1,
    check_get_name_response_200_data_format_type_2_type_1,
)
from ..models.get_name_response_200_data_format_type_3_type_1 import (
    GetNameResponse200DataFormatType3Type1,
    check_get_name_response_200_data_format_type_3_type_1,
)
from ..models.get_name_response_200_data_shape_type_1 import (
    GetNameResponse200DataShapeType1,
    check_get_name_response_200_data_shape_type_1,
)
from ..models.get_name_response_200_data_shape_type_2_type_1 import (
    GetNameResponse200DataShapeType2Type1,
    check_get_name_response_200_data_shape_type_2_type_1,
)
from ..models.get_name_response_200_data_shape_type_3_type_1 import (
    GetNameResponse200DataShapeType3Type1,
    check_get_name_response_200_data_shape_type_3_type_1,
)
from ..models.get_name_response_200_data_status import (
    GetNameResponse200DataStatus,
    check_get_name_response_200_data_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_name_response_200_data_comps import GetNameResponse200DataComps
    from ..models.get_name_response_200_data_drop import GetNameResponse200DataDrop
    from ..models.get_name_response_200_data_price import GetNameResponse200DataPrice
    from ..models.get_name_response_200_data_rating import GetNameResponse200DataRating
    from ..models.get_name_response_200_data_registry import (
        GetNameResponse200DataRegistry,
    )
    from ..models.get_name_response_200_data_value_type_0 import (
        GetNameResponse200DataValueType0,
    )
    from ..models.get_name_response_200_data_verdict_type_0 import (
        GetNameResponse200DataVerdictType0,
    )
    from ..models.get_name_response_200_data_word_type_0 import (
        GetNameResponse200DataWordType0,
    )


T = TypeVar("T", bound="GetNameResponse200Data")


@_attrs_define
class GetNameResponse200Data:
    """
    Attributes:
        id (None | str): `dom_<uuid>`; null when `tracked` is false.
        name (str):
        ending (str):
        tracked (bool): The catalog stores the name.
        status (GetNameResponse200DataStatus):
        drop (GetNameResponse200DataDrop):
        ownable_now (bool):
        price (GetNameResponse200DataPrice):
        registry (GetNameResponse200DataRegistry):
        rating (GetNameResponse200DataRating):
        comps (GetNameResponse200DataComps):
        lifecycle (None | str | Unset):
        parking (None | str | Unset): The parking or sale venue id.
        length (int | None | Unset):
        format_ (GetNameResponse200DataFormatType1 | GetNameResponse200DataFormatType2Type1 |
            GetNameResponse200DataFormatType3Type1 | None | Unset):
        shape (GetNameResponse200DataShapeType1 | GetNameResponse200DataShapeType2Type1 |
            GetNameResponse200DataShapeType3Type1 | None | Unset):
        word (GetNameResponse200DataWordType0 | None | Unset):
        verdict (GetNameResponse200DataVerdictType0 | None | Unset): Keyed.
        value (GetNameResponse200DataValueType0 | None | Unset): Keyed.
    """

    id: None | str
    name: str
    ending: str
    tracked: bool
    status: GetNameResponse200DataStatus
    drop: GetNameResponse200DataDrop
    ownable_now: bool
    price: GetNameResponse200DataPrice
    registry: GetNameResponse200DataRegistry
    rating: GetNameResponse200DataRating
    comps: GetNameResponse200DataComps
    lifecycle: None | str | Unset = UNSET
    parking: None | str | Unset = UNSET
    length: int | None | Unset = UNSET
    format_: (
        GetNameResponse200DataFormatType1
        | GetNameResponse200DataFormatType2Type1
        | GetNameResponse200DataFormatType3Type1
        | None
        | Unset
    ) = UNSET
    shape: (
        GetNameResponse200DataShapeType1
        | GetNameResponse200DataShapeType2Type1
        | GetNameResponse200DataShapeType3Type1
        | None
        | Unset
    ) = UNSET
    word: GetNameResponse200DataWordType0 | None | Unset = UNSET
    verdict: GetNameResponse200DataVerdictType0 | None | Unset = UNSET
    value: GetNameResponse200DataValueType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_name_response_200_data_value_type_0 import (
            GetNameResponse200DataValueType0,
        )
        from ..models.get_name_response_200_data_verdict_type_0 import (
            GetNameResponse200DataVerdictType0,
        )
        from ..models.get_name_response_200_data_word_type_0 import (
            GetNameResponse200DataWordType0,
        )

        id: None | str
        id = self.id

        name = self.name

        ending = self.ending

        tracked = self.tracked

        status: str = self.status

        drop = self.drop.to_dict()

        ownable_now = self.ownable_now

        price = self.price.to_dict()

        registry = self.registry.to_dict()

        rating = self.rating.to_dict()

        comps = self.comps.to_dict()

        lifecycle: None | str | Unset
        if isinstance(self.lifecycle, Unset):
            lifecycle = UNSET
        else:
            lifecycle = self.lifecycle

        parking: None | str | Unset
        if isinstance(self.parking, Unset):
            parking = UNSET
        else:
            parking = self.parking

        length: int | None | Unset
        if isinstance(self.length, Unset):
            length = UNSET
        else:
            length = self.length

        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        elif (
            isinstance(self.format_, str)
            or isinstance(self.format_, str)
            or isinstance(self.format_, str)
        ):
            format_ = self.format_
        else:
            format_ = self.format_

        shape: None | str | Unset
        if isinstance(self.shape, Unset):
            shape = UNSET
        elif (
            isinstance(self.shape, str)
            or isinstance(self.shape, str)
            or isinstance(self.shape, str)
        ):
            shape = self.shape
        else:
            shape = self.shape

        word: dict[str, Any] | None | Unset
        if isinstance(self.word, Unset):
            word = UNSET
        elif isinstance(self.word, GetNameResponse200DataWordType0):
            word = self.word.to_dict()
        else:
            word = self.word

        verdict: dict[str, Any] | None | Unset
        if isinstance(self.verdict, Unset):
            verdict = UNSET
        elif isinstance(self.verdict, GetNameResponse200DataVerdictType0):
            verdict = self.verdict.to_dict()
        else:
            verdict = self.verdict

        value: dict[str, Any] | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, GetNameResponse200DataValueType0):
            value = self.value.to_dict()
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ending": ending,
                "tracked": tracked,
                "status": status,
                "drop": drop,
                "ownableNow": ownable_now,
                "price": price,
                "registry": registry,
                "rating": rating,
                "comps": comps,
            }
        )
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if parking is not UNSET:
            field_dict["parking"] = parking
        if length is not UNSET:
            field_dict["length"] = length
        if format_ is not UNSET:
            field_dict["format"] = format_
        if shape is not UNSET:
            field_dict["shape"] = shape
        if word is not UNSET:
            field_dict["word"] = word
        if verdict is not UNSET:
            field_dict["verdict"] = verdict
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_name_response_200_data_comps import (
            GetNameResponse200DataComps,
        )
        from ..models.get_name_response_200_data_drop import GetNameResponse200DataDrop
        from ..models.get_name_response_200_data_price import (
            GetNameResponse200DataPrice,
        )
        from ..models.get_name_response_200_data_rating import (
            GetNameResponse200DataRating,
        )
        from ..models.get_name_response_200_data_registry import (
            GetNameResponse200DataRegistry,
        )
        from ..models.get_name_response_200_data_value_type_0 import (
            GetNameResponse200DataValueType0,
        )
        from ..models.get_name_response_200_data_verdict_type_0 import (
            GetNameResponse200DataVerdictType0,
        )
        from ..models.get_name_response_200_data_word_type_0 import (
            GetNameResponse200DataWordType0,
        )

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

        name = d.pop("name")

        ending = d.pop("ending")

        tracked = d.pop("tracked")

        status = check_get_name_response_200_data_status(d.pop("status"))

        drop = GetNameResponse200DataDrop.from_dict(d.pop("drop"))

        ownable_now = d.pop("ownableNow")

        price = GetNameResponse200DataPrice.from_dict(d.pop("price"))

        registry = GetNameResponse200DataRegistry.from_dict(d.pop("registry"))

        rating = GetNameResponse200DataRating.from_dict(d.pop("rating"))

        comps = GetNameResponse200DataComps.from_dict(d.pop("comps"))

        def _parse_lifecycle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lifecycle = _parse_lifecycle(d.pop("lifecycle", UNSET))

        def _parse_parking(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parking = _parse_parking(d.pop("parking", UNSET))

        def _parse_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        length = _parse_length(d.pop("length", UNSET))

        def _parse_format_(
            data: object,
        ) -> (
            GetNameResponse200DataFormatType1
            | GetNameResponse200DataFormatType2Type1
            | GetNameResponse200DataFormatType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_type_1 = check_get_name_response_200_data_format_type_1(data)

                return format_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_type_2_type_1 = (
                    check_get_name_response_200_data_format_type_2_type_1(data)
                )

                return format_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_type_3_type_1 = (
                    check_get_name_response_200_data_format_type_3_type_1(data)
                )

                return format_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetNameResponse200DataFormatType1
                | GetNameResponse200DataFormatType2Type1
                | GetNameResponse200DataFormatType3Type1
                | None
                | Unset,
                data,
            )

        format_ = _parse_format_(d.pop("format", UNSET))

        def _parse_shape(
            data: object,
        ) -> (
            GetNameResponse200DataShapeType1
            | GetNameResponse200DataShapeType2Type1
            | GetNameResponse200DataShapeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_1 = check_get_name_response_200_data_shape_type_1(data)

                return shape_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_2_type_1 = (
                    check_get_name_response_200_data_shape_type_2_type_1(data)
                )

                return shape_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_3_type_1 = (
                    check_get_name_response_200_data_shape_type_3_type_1(data)
                )

                return shape_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetNameResponse200DataShapeType1
                | GetNameResponse200DataShapeType2Type1
                | GetNameResponse200DataShapeType3Type1
                | None
                | Unset,
                data,
            )

        shape = _parse_shape(d.pop("shape", UNSET))

        def _parse_word(data: object) -> GetNameResponse200DataWordType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                word_type_0 = GetNameResponse200DataWordType0.from_dict(data)

                return word_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetNameResponse200DataWordType0 | None | Unset, data)

        word = _parse_word(d.pop("word", UNSET))

        def _parse_verdict(
            data: object,
        ) -> GetNameResponse200DataVerdictType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verdict_type_0 = GetNameResponse200DataVerdictType0.from_dict(data)

                return verdict_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetNameResponse200DataVerdictType0 | None | Unset, data)

        verdict = _parse_verdict(d.pop("verdict", UNSET))

        def _parse_value(
            data: object,
        ) -> GetNameResponse200DataValueType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = GetNameResponse200DataValueType0.from_dict(data)

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetNameResponse200DataValueType0 | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        get_name_response_200_data = cls(
            id=id,
            name=name,
            ending=ending,
            tracked=tracked,
            status=status,
            drop=drop,
            ownable_now=ownable_now,
            price=price,
            registry=registry,
            rating=rating,
            comps=comps,
            lifecycle=lifecycle,
            parking=parking,
            length=length,
            format_=format_,
            shape=shape,
            word=word,
            verdict=verdict,
            value=value,
        )

        get_name_response_200_data.additional_properties = d
        return get_name_response_200_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
