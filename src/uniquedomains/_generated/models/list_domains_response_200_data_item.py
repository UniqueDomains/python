from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_domains_response_200_data_item_format_type_1 import (
    ListDomainsResponse200DataItemFormatType1,
    check_list_domains_response_200_data_item_format_type_1,
)
from ..models.list_domains_response_200_data_item_format_type_2_type_1 import (
    ListDomainsResponse200DataItemFormatType2Type1,
    check_list_domains_response_200_data_item_format_type_2_type_1,
)
from ..models.list_domains_response_200_data_item_format_type_3_type_1 import (
    ListDomainsResponse200DataItemFormatType3Type1,
    check_list_domains_response_200_data_item_format_type_3_type_1,
)
from ..models.list_domains_response_200_data_item_liquidity_type_1 import (
    ListDomainsResponse200DataItemLiquidityType1,
    check_list_domains_response_200_data_item_liquidity_type_1,
)
from ..models.list_domains_response_200_data_item_liquidity_type_2_type_1 import (
    ListDomainsResponse200DataItemLiquidityType2Type1,
    check_list_domains_response_200_data_item_liquidity_type_2_type_1,
)
from ..models.list_domains_response_200_data_item_liquidity_type_3_type_1 import (
    ListDomainsResponse200DataItemLiquidityType3Type1,
    check_list_domains_response_200_data_item_liquidity_type_3_type_1,
)
from ..models.list_domains_response_200_data_item_price_kind_type_1 import (
    ListDomainsResponse200DataItemPriceKindType1,
    check_list_domains_response_200_data_item_price_kind_type_1,
)
from ..models.list_domains_response_200_data_item_price_kind_type_2_type_1 import (
    ListDomainsResponse200DataItemPriceKindType2Type1,
    check_list_domains_response_200_data_item_price_kind_type_2_type_1,
)
from ..models.list_domains_response_200_data_item_price_kind_type_3_type_1 import (
    ListDomainsResponse200DataItemPriceKindType3Type1,
    check_list_domains_response_200_data_item_price_kind_type_3_type_1,
)
from ..models.list_domains_response_200_data_item_rating_band_type_1 import (
    ListDomainsResponse200DataItemRatingBandType1,
    check_list_domains_response_200_data_item_rating_band_type_1,
)
from ..models.list_domains_response_200_data_item_rating_band_type_2_type_1 import (
    ListDomainsResponse200DataItemRatingBandType2Type1,
    check_list_domains_response_200_data_item_rating_band_type_2_type_1,
)
from ..models.list_domains_response_200_data_item_rating_band_type_3_type_1 import (
    ListDomainsResponse200DataItemRatingBandType3Type1,
    check_list_domains_response_200_data_item_rating_band_type_3_type_1,
)
from ..models.list_domains_response_200_data_item_shape_type_1 import (
    ListDomainsResponse200DataItemShapeType1,
    check_list_domains_response_200_data_item_shape_type_1,
)
from ..models.list_domains_response_200_data_item_shape_type_2_type_1 import (
    ListDomainsResponse200DataItemShapeType2Type1,
    check_list_domains_response_200_data_item_shape_type_2_type_1,
)
from ..models.list_domains_response_200_data_item_shape_type_3_type_1 import (
    ListDomainsResponse200DataItemShapeType3Type1,
    check_list_domains_response_200_data_item_shape_type_3_type_1,
)
from ..models.list_domains_response_200_data_item_status import (
    ListDomainsResponse200DataItemStatus,
    check_list_domains_response_200_data_item_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_domains_response_200_data_item_coverage_type_0 import (
        ListDomainsResponse200DataItemCoverageType0,
    )
    from ..models.list_domains_response_200_data_item_value_type_0 import (
        ListDomainsResponse200DataItemValueType0,
    )
    from ..models.list_domains_response_200_data_item_verdict import (
        ListDomainsResponse200DataItemVerdict,
    )


T = TypeVar("T", bound="ListDomainsResponse200DataItem")


@_attrs_define
class ListDomainsResponse200DataItem:
    """
    Attributes:
        id (str): `dom_<uuid>`.
        name (str):
        ending (str):
        status (ListDomainsResponse200DataItemStatus):
        price (float | None): Price today, USD.
        price_kind (ListDomainsResponse200DataItemPriceKindType1 | ListDomainsResponse200DataItemPriceKindType2Type1 |
            ListDomainsResponse200DataItemPriceKindType3Type1 | None):
        renewal (float | None):
        rating_band (ListDomainsResponse200DataItemRatingBandType1 | ListDomainsResponse200DataItemRatingBandType2Type1
            | ListDomainsResponse200DataItemRatingBandType3Type1 | None): A simple band; the score behind it is never served
            on a list.
        format_ (ListDomainsResponse200DataItemFormatType1 | ListDomainsResponse200DataItemFormatType2Type1 |
            ListDomainsResponse200DataItemFormatType3Type1 | None):
        shape (ListDomainsResponse200DataItemShapeType1 | ListDomainsResponse200DataItemShapeType2Type1 |
            ListDomainsResponse200DataItemShapeType3Type1 | None):
        length (int | None):
        coverage (ListDomainsResponse200DataItemCoverageType0 | None): The same word on other endings: available,
            premium, for sale.
        value (ListDomainsResponse200DataItemValueType0 | None | Unset): Keyed: the current estimate, USD.
        upside_percent (float | None | Unset): Keyed.
        liquidity (ListDomainsResponse200DataItemLiquidityType1 | ListDomainsResponse200DataItemLiquidityType2Type1 |
            ListDomainsResponse200DataItemLiquidityType3Type1 | None | Unset): Keyed.
        verdict (ListDomainsResponse200DataItemVerdict | Unset): Keyed.
    """

    id: str
    name: str
    ending: str
    status: ListDomainsResponse200DataItemStatus
    price: float | None
    price_kind: (
        ListDomainsResponse200DataItemPriceKindType1
        | ListDomainsResponse200DataItemPriceKindType2Type1
        | ListDomainsResponse200DataItemPriceKindType3Type1
        | None
    )
    renewal: float | None
    rating_band: (
        ListDomainsResponse200DataItemRatingBandType1
        | ListDomainsResponse200DataItemRatingBandType2Type1
        | ListDomainsResponse200DataItemRatingBandType3Type1
        | None
    )
    format_: (
        ListDomainsResponse200DataItemFormatType1
        | ListDomainsResponse200DataItemFormatType2Type1
        | ListDomainsResponse200DataItemFormatType3Type1
        | None
    )
    shape: (
        ListDomainsResponse200DataItemShapeType1
        | ListDomainsResponse200DataItemShapeType2Type1
        | ListDomainsResponse200DataItemShapeType3Type1
        | None
    )
    length: int | None
    coverage: ListDomainsResponse200DataItemCoverageType0 | None
    value: ListDomainsResponse200DataItemValueType0 | None | Unset = UNSET
    upside_percent: float | None | Unset = UNSET
    liquidity: (
        ListDomainsResponse200DataItemLiquidityType1
        | ListDomainsResponse200DataItemLiquidityType2Type1
        | ListDomainsResponse200DataItemLiquidityType3Type1
        | None
        | Unset
    ) = UNSET
    verdict: ListDomainsResponse200DataItemVerdict | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_domains_response_200_data_item_coverage_type_0 import (
            ListDomainsResponse200DataItemCoverageType0,
        )
        from ..models.list_domains_response_200_data_item_value_type_0 import (
            ListDomainsResponse200DataItemValueType0,
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
        if isinstance(self.coverage, ListDomainsResponse200DataItemCoverageType0):
            coverage = self.coverage.to_dict()
        else:
            coverage = self.coverage

        value: dict[str, Any] | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, ListDomainsResponse200DataItemValueType0):
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
        from ..models.list_domains_response_200_data_item_coverage_type_0 import (
            ListDomainsResponse200DataItemCoverageType0,
        )
        from ..models.list_domains_response_200_data_item_value_type_0 import (
            ListDomainsResponse200DataItemValueType0,
        )
        from ..models.list_domains_response_200_data_item_verdict import (
            ListDomainsResponse200DataItemVerdict,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        ending = d.pop("ending")

        status = check_list_domains_response_200_data_item_status(d.pop("status"))

        def _parse_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        price = _parse_price(d.pop("price"))

        def _parse_price_kind(
            data: object,
        ) -> (
            ListDomainsResponse200DataItemPriceKindType1
            | ListDomainsResponse200DataItemPriceKindType2Type1
            | ListDomainsResponse200DataItemPriceKindType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                price_kind_type_1 = (
                    check_list_domains_response_200_data_item_price_kind_type_1(data)
                )

                return price_kind_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                price_kind_type_2_type_1 = (
                    check_list_domains_response_200_data_item_price_kind_type_2_type_1(
                        data
                    )
                )

                return price_kind_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                price_kind_type_3_type_1 = (
                    check_list_domains_response_200_data_item_price_kind_type_3_type_1(
                        data
                    )
                )

                return price_kind_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListDomainsResponse200DataItemPriceKindType1
                | ListDomainsResponse200DataItemPriceKindType2Type1
                | ListDomainsResponse200DataItemPriceKindType3Type1
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
            ListDomainsResponse200DataItemRatingBandType1
            | ListDomainsResponse200DataItemRatingBandType2Type1
            | ListDomainsResponse200DataItemRatingBandType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rating_band_type_1 = (
                    check_list_domains_response_200_data_item_rating_band_type_1(data)
                )

                return rating_band_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rating_band_type_2_type_1 = (
                    check_list_domains_response_200_data_item_rating_band_type_2_type_1(
                        data
                    )
                )

                return rating_band_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rating_band_type_3_type_1 = (
                    check_list_domains_response_200_data_item_rating_band_type_3_type_1(
                        data
                    )
                )

                return rating_band_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListDomainsResponse200DataItemRatingBandType1
                | ListDomainsResponse200DataItemRatingBandType2Type1
                | ListDomainsResponse200DataItemRatingBandType3Type1
                | None,
                data,
            )

        rating_band = _parse_rating_band(d.pop("ratingBand"))

        def _parse_format_(
            data: object,
        ) -> (
            ListDomainsResponse200DataItemFormatType1
            | ListDomainsResponse200DataItemFormatType2Type1
            | ListDomainsResponse200DataItemFormatType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_type_1 = check_list_domains_response_200_data_item_format_type_1(
                    data
                )

                return format_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_type_2_type_1 = (
                    check_list_domains_response_200_data_item_format_type_2_type_1(data)
                )

                return format_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_type_3_type_1 = (
                    check_list_domains_response_200_data_item_format_type_3_type_1(data)
                )

                return format_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListDomainsResponse200DataItemFormatType1
                | ListDomainsResponse200DataItemFormatType2Type1
                | ListDomainsResponse200DataItemFormatType3Type1
                | None,
                data,
            )

        format_ = _parse_format_(d.pop("format"))

        def _parse_shape(
            data: object,
        ) -> (
            ListDomainsResponse200DataItemShapeType1
            | ListDomainsResponse200DataItemShapeType2Type1
            | ListDomainsResponse200DataItemShapeType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_1 = check_list_domains_response_200_data_item_shape_type_1(
                    data
                )

                return shape_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_2_type_1 = (
                    check_list_domains_response_200_data_item_shape_type_2_type_1(data)
                )

                return shape_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shape_type_3_type_1 = (
                    check_list_domains_response_200_data_item_shape_type_3_type_1(data)
                )

                return shape_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListDomainsResponse200DataItemShapeType1
                | ListDomainsResponse200DataItemShapeType2Type1
                | ListDomainsResponse200DataItemShapeType3Type1
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
        ) -> ListDomainsResponse200DataItemCoverageType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coverage_type_0 = ListDomainsResponse200DataItemCoverageType0.from_dict(
                    data
                )

                return coverage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListDomainsResponse200DataItemCoverageType0 | None, data)

        coverage = _parse_coverage(d.pop("coverage"))

        def _parse_value(
            data: object,
        ) -> ListDomainsResponse200DataItemValueType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = ListDomainsResponse200DataItemValueType0.from_dict(data)

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListDomainsResponse200DataItemValueType0 | None | Unset, data)

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
            ListDomainsResponse200DataItemLiquidityType1
            | ListDomainsResponse200DataItemLiquidityType2Type1
            | ListDomainsResponse200DataItemLiquidityType3Type1
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
                    check_list_domains_response_200_data_item_liquidity_type_1(data)
                )

                return liquidity_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                liquidity_type_2_type_1 = (
                    check_list_domains_response_200_data_item_liquidity_type_2_type_1(
                        data
                    )
                )

                return liquidity_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                liquidity_type_3_type_1 = (
                    check_list_domains_response_200_data_item_liquidity_type_3_type_1(
                        data
                    )
                )

                return liquidity_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListDomainsResponse200DataItemLiquidityType1
                | ListDomainsResponse200DataItemLiquidityType2Type1
                | ListDomainsResponse200DataItemLiquidityType3Type1
                | None
                | Unset,
                data,
            )

        liquidity = _parse_liquidity(d.pop("liquidity", UNSET))

        _verdict = d.pop("verdict", UNSET)
        verdict: ListDomainsResponse200DataItemVerdict | Unset
        if isinstance(_verdict, Unset):
            verdict = UNSET
        else:
            verdict = ListDomainsResponse200DataItemVerdict.from_dict(_verdict)

        list_domains_response_200_data_item = cls(
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

        list_domains_response_200_data_item.additional_properties = d
        return list_domains_response_200_data_item

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
