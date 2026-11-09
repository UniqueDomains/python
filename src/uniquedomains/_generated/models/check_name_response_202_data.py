from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_name_response_202_data_format_type_1 import (
    CheckNameResponse202DataFormatType1,
    check_check_name_response_202_data_format_type_1,
)
from ..models.check_name_response_202_data_format_type_2_type_1 import (
    CheckNameResponse202DataFormatType2Type1,
    check_check_name_response_202_data_format_type_2_type_1,
)
from ..models.check_name_response_202_data_format_type_3_type_1 import (
    CheckNameResponse202DataFormatType3Type1,
    check_check_name_response_202_data_format_type_3_type_1,
)
from ..models.check_name_response_202_data_shape_type_1 import (
    CheckNameResponse202DataShapeType1,
    check_check_name_response_202_data_shape_type_1,
)
from ..models.check_name_response_202_data_shape_type_2_type_1 import (
    CheckNameResponse202DataShapeType2Type1,
    check_check_name_response_202_data_shape_type_2_type_1,
)
from ..models.check_name_response_202_data_shape_type_3_type_1 import (
    CheckNameResponse202DataShapeType3Type1,
    check_check_name_response_202_data_shape_type_3_type_1,
)
from ..models.check_name_response_202_data_status import (
    CheckNameResponse202DataStatus,
    check_check_name_response_202_data_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_name_response_202_data_comps import (
        CheckNameResponse202DataComps,
    )
    from ..models.check_name_response_202_data_drop import CheckNameResponse202DataDrop
    from ..models.check_name_response_202_data_price import (
        CheckNameResponse202DataPrice,
    )
    from ..models.check_name_response_202_data_rating import (
        CheckNameResponse202DataRating,
    )
    from ..models.check_name_response_202_data_registry import (
        CheckNameResponse202DataRegistry,
    )
    from ..models.check_name_response_202_data_value_type_0 import (
        CheckNameResponse202DataValueType0,
    )
    from ..models.check_name_response_202_data_verdict_type_0 import (
        CheckNameResponse202DataVerdictType0,
    )
    from ..models.check_name_response_202_data_word_type_0 import (
        CheckNameResponse202DataWordType0,
    )


T = TypeVar("T", bound="CheckNameResponse202Data")


@_attrs_define
class CheckNameResponse202Data:
    """
    Attributes:
        id (None | str): `dom_<uuid>`; null when `tracked` is false.
        name (str):
        ending (str):
        tracked (bool): The catalog stores the name.
        status (CheckNameResponse202DataStatus):
        drop (CheckNameResponse202DataDrop):
        ownable_now (bool):
        price (CheckNameResponse202DataPrice):
        registry (CheckNameResponse202DataRegistry):
        rating (CheckNameResponse202DataRating):
        comps (CheckNameResponse202DataComps):
        lifecycle (None | str | Unset):
        parking (None | str | Unset): The parking or sale venue id.
        length (int | None | Unset):
        format_ (CheckNameResponse202DataFormatType1 | CheckNameResponse202DataFormatType2Type1 |
            CheckNameResponse202DataFormatType3Type1 | None | Unset):
        shape (CheckNameResponse202DataShapeType1 | CheckNameResponse202DataShapeType2Type1 |
            CheckNameResponse202DataShapeType3Type1 | None | Unset):
        word (CheckNameResponse202DataWordType0 | None | Unset):
        verdict (CheckNameResponse202DataVerdictType0 | None | Unset): Keyed.
        value (CheckNameResponse202DataValueType0 | None | Unset): Keyed.
        checked (bool | Unset): The live read answered.
    """

    id: None | str
    name: str
    ending: str
    tracked: bool
    status: CheckNameResponse202DataStatus
    drop: CheckNameResponse202DataDrop
    ownable_now: bool
    price: CheckNameResponse202DataPrice
    registry: CheckNameResponse202DataRegistry
    rating: CheckNameResponse202DataRating
    comps: CheckNameResponse202DataComps
    lifecycle: None | str | Unset = UNSET
    parking: None | str | Unset = UNSET
    length: int | None | Unset = UNSET
    format_: (
        CheckNameResponse202DataFormatType1
        | CheckNameResponse202DataFormatType2Type1
        | CheckNameResponse202DataFormatType3Type1
        | None
        | Unset
    ) = UNSET
    shape: (
        CheckNameResponse202DataShapeType1
        | CheckNameResponse202DataShapeType2Type1
        | CheckNameResponse202DataShapeType3Type1
        | None
        | Unset
    ) = UNSET
    word: CheckNameResponse202DataWordType0 | None | Unset = UNSET
    verdict: CheckNameResponse202DataVerdictType0 | None | Unset = UNSET
    value: CheckNameResponse202DataValueType0 | None | Unset = UNSET
    checked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.check_name_response_202_data_value_type_0 import (
            CheckNameResponse202DataValueType0,
        )
        from ..models.check_name_response_202_data_verdict_type_0 import (
            CheckNameResponse202DataVerdictType0,
        )
        from ..models.check_name_response_202_data_word_type_0 import (
            CheckNameResponse202DataWordType0,
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
        elif isinstance(self.word, CheckNameResponse202DataWordType0):
            word = self.word.to_dict()
        else:
            word = self.word

        verdict: dict[str, Any] | None | Unset
        if isinstance(self.verdict, Unset):
            verdict = UNSET
        elif isinstance(self.verdict, CheckNameResponse202DataVerdictType0):
            verdict = self.verdict.to_dict()
        else:
            verdict = self.verdict

        value: dict[str, Any] | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, CheckNameResponse202DataValueType0):
            value = self.value.to_dict()
        else:
            value = self.value

        checked = self.checked

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
        if checked is not UNSET:
            field_dict["checked"] = checked

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.check_name_response_202_data_comps import (
            CheckNameResponse202DataComps,
        )
        from ..models.check_name_response_202_data_drop import (
            CheckNameResponse202DataDrop,
        )
        from ..models.check_name_response_202_data_price import (
            CheckNameResponse202DataPrice,
        )
        from ..models.check_name_response_202_data_rating import (
            CheckNameResponse202DataRating,
        )
        from ..models.check_name_response_202_data_registry import (
            CheckNameResponse202DataRegistry,
        )
        from ..models.check_name_response_202_data_value_type_0 import (
            CheckNameResponse202DataValueType0,
        )
        from ..models.check_name_response_202_data_verdict_type_0 import (
            CheckNameResponse202DataVerdictType0,
        )
        from ..models.check_name_response_202_data_word_type_0 import (
            CheckNameResponse202DataWordType0,
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

        status = check_check_name_response_202_data_status(d.pop("status"))

        drop = CheckNameResponse202DataDrop.from_dict(d.pop("drop"))

        ownable_now = d.pop("ownableNow")

        price = CheckNameResponse202DataPrice.from_dict(d.pop("price"))

        registry = CheckNameResponse202DataRegistry.from_dict(d.pop("registry"))

        rating = CheckNameResponse202DataRating.from_dict(d.pop("rating"))

        comps = CheckNameResponse202DataComps.from_dict(d.pop("comps"))

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
            CheckNameResponse202DataFormatType1
            | CheckNameResponse202DataFormatType2Type1
            | CheckNameResponse202DataFormatType3Type1
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
                format_type_1 = check_check_name_response_202_data_format_type_1(data)

                return format_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_type_2_type_1 = (
                    check_check_name_response_202_data_format_type_2_type_1(data)
                )

                return format_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_type_3_type_1 = (
                    check_check_name_response_202_data_format_type_3_type_1(data)
                )

                return format_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CheckNameResponse202DataFormatType1
                | CheckNameResponse202DataFormatType2Type1
                | CheckNameResponse202DataFormatType3Type1
                | None
                | Unset,
                data,
            )

        format_ = _parse_format_(d.pop("format", UNSET))

        def _parse_shape(
            data: object,
        ) -> (
            CheckNameResponse202DataShapeType1
            | CheckNameResponse202DataShapeType2Type1
            | CheckNameResponse202DataShapeType3Type1
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
                shape_type_1 = check_check_name_response_202_data_shape_type_1(data)

                return shape_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_2_type_1 = (
                    check_check_name_response_202_data_shape_type_2_type_1(data)
                )

                return shape_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_3_type_1 = (
                    check_check_name_response_202_data_shape_type_3_type_1(data)
                )

                return shape_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CheckNameResponse202DataShapeType1
                | CheckNameResponse202DataShapeType2Type1
                | CheckNameResponse202DataShapeType3Type1
                | None
                | Unset,
                data,
            )

        shape = _parse_shape(d.pop("shape", UNSET))

        def _parse_word(
            data: object,
        ) -> CheckNameResponse202DataWordType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                word_type_0 = CheckNameResponse202DataWordType0.from_dict(data)

                return word_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CheckNameResponse202DataWordType0 | None | Unset, data)

        word = _parse_word(d.pop("word", UNSET))

        def _parse_verdict(
            data: object,
        ) -> CheckNameResponse202DataVerdictType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verdict_type_0 = CheckNameResponse202DataVerdictType0.from_dict(data)

                return verdict_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CheckNameResponse202DataVerdictType0 | None | Unset, data)

        verdict = _parse_verdict(d.pop("verdict", UNSET))

        def _parse_value(
            data: object,
        ) -> CheckNameResponse202DataValueType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = CheckNameResponse202DataValueType0.from_dict(data)

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CheckNameResponse202DataValueType0 | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        checked = d.pop("checked", UNSET)

        check_name_response_202_data = cls(
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
            checked=checked,
        )

        check_name_response_202_data.additional_properties = d
        return check_name_response_202_data

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
