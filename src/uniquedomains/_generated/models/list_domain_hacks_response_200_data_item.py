from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_domain_hacks_response_200_data_item_format_type_1 import (
    ListDomainHacksResponse200DataItemFormatType1,
    check_list_domain_hacks_response_200_data_item_format_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_format_type_2_type_1 import (
    ListDomainHacksResponse200DataItemFormatType2Type1,
    check_list_domain_hacks_response_200_data_item_format_type_2_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_format_type_3_type_1 import (
    ListDomainHacksResponse200DataItemFormatType3Type1,
    check_list_domain_hacks_response_200_data_item_format_type_3_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_liquidity_type_1 import (
    ListDomainHacksResponse200DataItemLiquidityType1,
    check_list_domain_hacks_response_200_data_item_liquidity_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_liquidity_type_2_type_1 import (
    ListDomainHacksResponse200DataItemLiquidityType2Type1,
    check_list_domain_hacks_response_200_data_item_liquidity_type_2_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_liquidity_type_3_type_1 import (
    ListDomainHacksResponse200DataItemLiquidityType3Type1,
    check_list_domain_hacks_response_200_data_item_liquidity_type_3_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_price_kind_type_1 import (
    ListDomainHacksResponse200DataItemPriceKindType1,
    check_list_domain_hacks_response_200_data_item_price_kind_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_price_kind_type_2_type_1 import (
    ListDomainHacksResponse200DataItemPriceKindType2Type1,
    check_list_domain_hacks_response_200_data_item_price_kind_type_2_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_price_kind_type_3_type_1 import (
    ListDomainHacksResponse200DataItemPriceKindType3Type1,
    check_list_domain_hacks_response_200_data_item_price_kind_type_3_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_rating_band_type_1 import (
    ListDomainHacksResponse200DataItemRatingBandType1,
    check_list_domain_hacks_response_200_data_item_rating_band_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_rating_band_type_2_type_1 import (
    ListDomainHacksResponse200DataItemRatingBandType2Type1,
    check_list_domain_hacks_response_200_data_item_rating_band_type_2_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_rating_band_type_3_type_1 import (
    ListDomainHacksResponse200DataItemRatingBandType3Type1,
    check_list_domain_hacks_response_200_data_item_rating_band_type_3_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_shape_type_1 import (
    ListDomainHacksResponse200DataItemShapeType1,
    check_list_domain_hacks_response_200_data_item_shape_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_shape_type_2_type_1 import (
    ListDomainHacksResponse200DataItemShapeType2Type1,
    check_list_domain_hacks_response_200_data_item_shape_type_2_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_shape_type_3_type_1 import (
    ListDomainHacksResponse200DataItemShapeType3Type1,
    check_list_domain_hacks_response_200_data_item_shape_type_3_type_1,
)
from ..models.list_domain_hacks_response_200_data_item_status import (
    ListDomainHacksResponse200DataItemStatus,
    check_list_domain_hacks_response_200_data_item_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_domain_hacks_response_200_data_item_coverage_type_0 import (
        ListDomainHacksResponse200DataItemCoverageType0,
    )
    from ..models.list_domain_hacks_response_200_data_item_value_type_0 import (
        ListDomainHacksResponse200DataItemValueType0,
    )
    from ..models.list_domain_hacks_response_200_data_item_verdict import (
        ListDomainHacksResponse200DataItemVerdict,
    )


T = TypeVar("T", bound="ListDomainHacksResponse200DataItem")


@_attrs_define
class ListDomainHacksResponse200DataItem:
    """
    Attributes:
        id (str): `dom_<uuid>`.
        name (str):
        ending (str):
        status (ListDomainHacksResponse200DataItemStatus):
        price (float | None): Price today, USD.
        price_kind (ListDomainHacksResponse200DataItemPriceKindType1 |
            ListDomainHacksResponse200DataItemPriceKindType2Type1 | ListDomainHacksResponse200DataItemPriceKindType3Type1 |
            None):
        renewal (float | None):
        rating_band (ListDomainHacksResponse200DataItemRatingBandType1 |
            ListDomainHacksResponse200DataItemRatingBandType2Type1 | ListDomainHacksResponse200DataItemRatingBandType3Type1
            | None): A simple band; the score behind it is never served on a list.
        format_ (ListDomainHacksResponse200DataItemFormatType1 | ListDomainHacksResponse200DataItemFormatType2Type1 |
            ListDomainHacksResponse200DataItemFormatType3Type1 | None):
        shape (ListDomainHacksResponse200DataItemShapeType1 | ListDomainHacksResponse200DataItemShapeType2Type1 |
            ListDomainHacksResponse200DataItemShapeType3Type1 | None):
        length (int | None):
        coverage (ListDomainHacksResponse200DataItemCoverageType0 | None): The same word on other endings: available,
            premium, for sale.
        value (ListDomainHacksResponse200DataItemValueType0 | None | Unset): Keyed: the current estimate, USD.
        upside_percent (float | None | Unset): Keyed.
        liquidity (ListDomainHacksResponse200DataItemLiquidityType1 |
            ListDomainHacksResponse200DataItemLiquidityType2Type1 | ListDomainHacksResponse200DataItemLiquidityType3Type1 |
            None | Unset): Keyed.
        verdict (ListDomainHacksResponse200DataItemVerdict | Unset): Keyed.
    """

    id: str
    name: str
    ending: str
    status: ListDomainHacksResponse200DataItemStatus
    price: float | None
    price_kind: (
        ListDomainHacksResponse200DataItemPriceKindType1
        | ListDomainHacksResponse200DataItemPriceKindType2Type1
        | ListDomainHacksResponse200DataItemPriceKindType3Type1
        | None
    )
    renewal: float | None
    rating_band: (
        ListDomainHacksResponse200DataItemRatingBandType1
        | ListDomainHacksResponse200DataItemRatingBandType2Type1
        | ListDomainHacksResponse200DataItemRatingBandType3Type1
        | None
    )
    format_: (
        ListDomainHacksResponse200DataItemFormatType1
        | ListDomainHacksResponse200DataItemFormatType2Type1
        | ListDomainHacksResponse200DataItemFormatType3Type1
        | None
    )
    shape: (
        ListDomainHacksResponse200DataItemShapeType1
        | ListDomainHacksResponse200DataItemShapeType2Type1
        | ListDomainHacksResponse200DataItemShapeType3Type1
        | None
    )
    length: int | None
    coverage: ListDomainHacksResponse200DataItemCoverageType0 | None
    value: ListDomainHacksResponse200DataItemValueType0 | None | Unset = UNSET
    upside_percent: float | None | Unset = UNSET
    liquidity: (
        ListDomainHacksResponse200DataItemLiquidityType1
        | ListDomainHacksResponse200DataItemLiquidityType2Type1
        | ListDomainHacksResponse200DataItemLiquidityType3Type1
        | None
        | Unset
    ) = UNSET
    verdict: ListDomainHacksResponse200DataItemVerdict | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_domain_hacks_response_200_data_item_coverage_type_0 import (
            ListDomainHacksResponse200DataItemCoverageType0,
        )
        from ..models.list_domain_hacks_response_200_data_item_value_type_0 import (
            ListDomainHacksResponse200DataItemValueType0,
        )

        id = self.id

        name = self.name

        ending = self.ending

        status: str = self.status

        price: float | None
        price = self.price

        price_kind: None | str
        if (
            isinstance(self.price_kind, str)
            or isinstance(self.price_kind, str)
            or isinstance(self.price_kind, str)
        ):
            price_kind = self.price_kind
        else:
            price_kind = self.price_kind

        renewal: float | None
        renewal = self.renewal

        rating_band: None | str
        if (
            isinstance(self.rating_band, str)
            or isinstance(self.rating_band, str)
            or isinstance(self.rating_band, str)
        ):
            rating_band = self.rating_band
        else:
            rating_band = self.rating_band

        format_: None | str
        if (
            isinstance(self.format_, str)
            or isinstance(self.format_, str)
            or isinstance(self.format_, str)
        ):
            format_ = self.format_
        else:
            format_ = self.format_

        shape: None | str
        if (
            isinstance(self.shape, str)
            or isinstance(self.shape, str)
            or isinstance(self.shape, str)
        ):
            shape = self.shape
        else:
            shape = self.shape

        length: int | None
        length = self.length

        coverage: dict[str, Any] | None
        if isinstance(self.coverage, ListDomainHacksResponse200DataItemCoverageType0):
            coverage = self.coverage.to_dict()
        else:
            coverage = self.coverage

        value: dict[str, Any] | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, ListDomainHacksResponse200DataItemValueType0):
            value = self.value.to_dict()
        else:
            value = self.value

        upside_percent: float | None | Unset
        if isinstance(self.upside_percent, Unset):
            upside_percent = UNSET
        else:
            upside_percent = self.upside_percent

        liquidity: None | str | Unset
        if isinstance(self.liquidity, Unset):
            liquidity = UNSET
        elif (
            isinstance(self.liquidity, str)
            or isinstance(self.liquidity, str)
            or isinstance(self.liquidity, str)
        ):
            liquidity = self.liquidity
        else:
            liquidity = self.liquidity

        verdict: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verdict, Unset):
            verdict = self.verdict.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ending": ending,
                "status": status,
                "price": price,
                "priceKind": price_kind,
                "renewal": renewal,
                "ratingBand": rating_band,
                "format": format_,
                "shape": shape,
                "length": length,
                "coverage": coverage,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if upside_percent is not UNSET:
            field_dict["upsidePercent"] = upside_percent
        if liquidity is not UNSET:
            field_dict["liquidity"] = liquidity
        if verdict is not UNSET:
            field_dict["verdict"] = verdict

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_domain_hacks_response_200_data_item_coverage_type_0 import (
            ListDomainHacksResponse200DataItemCoverageType0,
        )
        from ..models.list_domain_hacks_response_200_data_item_value_type_0 import (
            ListDomainHacksResponse200DataItemValueType0,
        )
        from ..models.list_domain_hacks_response_200_data_item_verdict import (
            ListDomainHacksResponse200DataItemVerdict,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        ending = d.pop("ending")

        status = check_list_domain_hacks_response_200_data_item_status(d.pop("status"))

        def _parse_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        price = _parse_price(d.pop("price"))

        def _parse_price_kind(
            data: object,
        ) -> (
            ListDomainHacksResponse200DataItemPriceKindType1
            | ListDomainHacksResponse200DataItemPriceKindType2Type1
            | ListDomainHacksResponse200DataItemPriceKindType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                price_kind_type_1 = (
                    check_list_domain_hacks_response_200_data_item_price_kind_type_1(
                        data
                    )
                )

                return price_kind_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                price_kind_type_2_type_1 = check_list_domain_hacks_response_200_data_item_price_kind_type_2_type_1(
                    data
                )

                return price_kind_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                price_kind_type_3_type_1 = check_list_domain_hacks_response_200_data_item_price_kind_type_3_type_1(
                    data
                )

                return price_kind_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListDomainHacksResponse200DataItemPriceKindType1
                | ListDomainHacksResponse200DataItemPriceKindType2Type1
                | ListDomainHacksResponse200DataItemPriceKindType3Type1
                | None,
                data,
            )

        price_kind = _parse_price_kind(d.pop("priceKind"))

        def _parse_renewal(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        renewal = _parse_renewal(d.pop("renewal"))

        def _parse_rating_band(
            data: object,
        ) -> (
            ListDomainHacksResponse200DataItemRatingBandType1
            | ListDomainHacksResponse200DataItemRatingBandType2Type1
            | ListDomainHacksResponse200DataItemRatingBandType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rating_band_type_1 = (
                    check_list_domain_hacks_response_200_data_item_rating_band_type_1(
                        data
                    )
                )

                return rating_band_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rating_band_type_2_type_1 = check_list_domain_hacks_response_200_data_item_rating_band_type_2_type_1(
                    data
                )

                return rating_band_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rating_band_type_3_type_1 = check_list_domain_hacks_response_200_data_item_rating_band_type_3_type_1(
                    data
                )

                return rating_band_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListDomainHacksResponse200DataItemRatingBandType1
                | ListDomainHacksResponse200DataItemRatingBandType2Type1
                | ListDomainHacksResponse200DataItemRatingBandType3Type1
                | None,
                data,
            )

        rating_band = _parse_rating_band(d.pop("ratingBand"))

        def _parse_format_(
            data: object,
        ) -> (
            ListDomainHacksResponse200DataItemFormatType1
            | ListDomainHacksResponse200DataItemFormatType2Type1
            | ListDomainHacksResponse200DataItemFormatType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_type_1 = (
                    check_list_domain_hacks_response_200_data_item_format_type_1(data)
                )

                return format_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_type_2_type_1 = (
                    check_list_domain_hacks_response_200_data_item_format_type_2_type_1(
                        data
                    )
                )

                return format_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_type_3_type_1 = (
                    check_list_domain_hacks_response_200_data_item_format_type_3_type_1(
                        data
                    )
                )

                return format_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListDomainHacksResponse200DataItemFormatType1
                | ListDomainHacksResponse200DataItemFormatType2Type1
                | ListDomainHacksResponse200DataItemFormatType3Type1
                | None,
                data,
            )

        format_ = _parse_format_(d.pop("format"))

        def _parse_shape(
            data: object,
        ) -> (
            ListDomainHacksResponse200DataItemShapeType1
            | ListDomainHacksResponse200DataItemShapeType2Type1
            | ListDomainHacksResponse200DataItemShapeType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_1 = (
                    check_list_domain_hacks_response_200_data_item_shape_type_1(data)
                )

                return shape_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_2_type_1 = (
                    check_list_domain_hacks_response_200_data_item_shape_type_2_type_1(
                        data
                    )
                )

                return shape_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_3_type_1 = (
                    check_list_domain_hacks_response_200_data_item_shape_type_3_type_1(
                        data
                    )
                )

                return shape_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListDomainHacksResponse200DataItemShapeType1
                | ListDomainHacksResponse200DataItemShapeType2Type1
                | ListDomainHacksResponse200DataItemShapeType3Type1
                | None,
                data,
            )

        shape = _parse_shape(d.pop("shape"))

        def _parse_length(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        length = _parse_length(d.pop("length"))

        def _parse_coverage(
            data: object,
        ) -> ListDomainHacksResponse200DataItemCoverageType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coverage_type_0 = (
                    ListDomainHacksResponse200DataItemCoverageType0.from_dict(data)
                )

                return coverage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListDomainHacksResponse200DataItemCoverageType0 | None, data)

        coverage = _parse_coverage(d.pop("coverage"))

        def _parse_value(
            data: object,
        ) -> ListDomainHacksResponse200DataItemValueType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = ListDomainHacksResponse200DataItemValueType0.from_dict(
                    data
                )

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListDomainHacksResponse200DataItemValueType0 | None | Unset, data
            )

        value = _parse_value(d.pop("value", UNSET))

        def _parse_upside_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        upside_percent = _parse_upside_percent(d.pop("upsidePercent", UNSET))

        def _parse_liquidity(
            data: object,
        ) -> (
            ListDomainHacksResponse200DataItemLiquidityType1
            | ListDomainHacksResponse200DataItemLiquidityType2Type1
            | ListDomainHacksResponse200DataItemLiquidityType3Type1
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
                liquidity_type_1 = (
                    check_list_domain_hacks_response_200_data_item_liquidity_type_1(
                        data
                    )
                )

                return liquidity_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                liquidity_type_2_type_1 = check_list_domain_hacks_response_200_data_item_liquidity_type_2_type_1(
                    data
                )

                return liquidity_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                liquidity_type_3_type_1 = check_list_domain_hacks_response_200_data_item_liquidity_type_3_type_1(
                    data
                )

                return liquidity_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListDomainHacksResponse200DataItemLiquidityType1
                | ListDomainHacksResponse200DataItemLiquidityType2Type1
                | ListDomainHacksResponse200DataItemLiquidityType3Type1
                | None
                | Unset,
                data,
            )

        liquidity = _parse_liquidity(d.pop("liquidity", UNSET))

        _verdict = d.pop("verdict", UNSET)
        verdict: ListDomainHacksResponse200DataItemVerdict | Unset
        if isinstance(_verdict, Unset):
            verdict = UNSET
        else:
            verdict = ListDomainHacksResponse200DataItemVerdict.from_dict(_verdict)

        list_domain_hacks_response_200_data_item = cls(
            id=id,
            name=name,
            ending=ending,
            status=status,
            price=price,
            price_kind=price_kind,
            renewal=renewal,
            rating_band=rating_band,
            format_=format_,
            shape=shape,
            length=length,
            coverage=coverage,
            value=value,
            upside_percent=upside_percent,
            liquidity=liquidity,
            verdict=verdict,
        )

        list_domain_hacks_response_200_data_item.additional_properties = d
        return list_domain_hacks_response_200_data_item

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
