from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_latest_edition_response_200_data_trends_item_rows_item_liquidity_type_1 import (
    GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType1,
    check_get_latest_edition_response_200_data_trends_item_rows_item_liquidity_type_1,
)
from ..models.get_latest_edition_response_200_data_trends_item_rows_item_liquidity_type_2_type_1 import (
    GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType2Type1,
    check_get_latest_edition_response_200_data_trends_item_rows_item_liquidity_type_2_type_1,
)
from ..models.get_latest_edition_response_200_data_trends_item_rows_item_liquidity_type_3_type_1 import (
    GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType3Type1,
    check_get_latest_edition_response_200_data_trends_item_rows_item_liquidity_type_3_type_1,
)
from ..models.get_latest_edition_response_200_data_trends_item_rows_item_match_kind import (
    GetLatestEditionResponse200DataTrendsItemRowsItemMatchKind,
    check_get_latest_edition_response_200_data_trends_item_rows_item_match_kind,
)
from ..models.get_latest_edition_response_200_data_trends_item_rows_item_price_kind_type_1 import (
    GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType1,
    check_get_latest_edition_response_200_data_trends_item_rows_item_price_kind_type_1,
)
from ..models.get_latest_edition_response_200_data_trends_item_rows_item_price_kind_type_2_type_1 import (
    GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType2Type1,
    check_get_latest_edition_response_200_data_trends_item_rows_item_price_kind_type_2_type_1,
)
from ..models.get_latest_edition_response_200_data_trends_item_rows_item_price_kind_type_3_type_1 import (
    GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType3Type1,
    check_get_latest_edition_response_200_data_trends_item_rows_item_price_kind_type_3_type_1,
)
from ..models.get_latest_edition_response_200_data_trends_item_rows_item_rating import (
    GetLatestEditionResponse200DataTrendsItemRowsItemRating,
    check_get_latest_edition_response_200_data_trends_item_rows_item_rating,
)
from ..models.get_latest_edition_response_200_data_trends_item_rows_item_status import (
    GetLatestEditionResponse200DataTrendsItemRowsItemStatus,
    check_get_latest_edition_response_200_data_trends_item_rows_item_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_latest_edition_response_200_data_trends_item_rows_item_ideas_item import (
        GetLatestEditionResponse200DataTrendsItemRowsItemIdeasItem,
    )
    from ..models.get_latest_edition_response_200_data_trends_item_rows_item_verdict_type_0 import (
        GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0,
    )


T = TypeVar("T", bound="GetLatestEditionResponse200DataTrendsItemRowsItem")


@_attrs_define
class GetLatestEditionResponse200DataTrendsItemRowsItem:
    """
    Attributes:
        name (str | Unset):
        word (str | Unset):
        ending (str | Unset):
        match_kind (GetLatestEditionResponse200DataTrendsItemRowsItemMatchKind | Unset):
        relation (None | str | Unset):
        status (GetLatestEditionResponse200DataTrendsItemRowsItemStatus | Unset):
        price (float | None | Unset):
        price_kind (GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType1 |
            GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType2Type1 |
            GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType3Type1 | None | Unset):
        quoted_by (None | str | Unset):
        renewal (float | None | Unset):
        five_year_cost (float | None | Unset): Founder page.
        value (float | None | Unset): Investor page; null past the public cap on Est. profit.
        upside_percent (float | None | Unset): Capped on the public page.
        upside_capped (bool | Unset):
        liquidity (GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType1 |
            GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType2Type1 |
            GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType3Type1 | None | Unset):
        verdict (GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0 | None | Unset):
        rating (GetLatestEditionResponse200DataTrendsItemRowsItemRating | Unset):
        ideas (list[GetLatestEditionResponse200DataTrendsItemRowsItemIdeasItem] | Unset):
    """

    name: str | Unset = UNSET
    word: str | Unset = UNSET
    ending: str | Unset = UNSET
    match_kind: GetLatestEditionResponse200DataTrendsItemRowsItemMatchKind | Unset = (
        UNSET
    )
    relation: None | str | Unset = UNSET
    status: GetLatestEditionResponse200DataTrendsItemRowsItemStatus | Unset = UNSET
    price: float | None | Unset = UNSET
    price_kind: (
        GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType1
        | GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType2Type1
        | GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType3Type1
        | None
        | Unset
    ) = UNSET
    quoted_by: None | str | Unset = UNSET
    renewal: float | None | Unset = UNSET
    five_year_cost: float | None | Unset = UNSET
    value: float | None | Unset = UNSET
    upside_percent: float | None | Unset = UNSET
    upside_capped: bool | Unset = UNSET
    liquidity: (
        GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType1
        | GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType2Type1
        | GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType3Type1
        | None
        | Unset
    ) = UNSET
    verdict: (
        GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0 | None | Unset
    ) = UNSET
    rating: GetLatestEditionResponse200DataTrendsItemRowsItemRating | Unset = UNSET
    ideas: list[GetLatestEditionResponse200DataTrendsItemRowsItemIdeasItem] | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_latest_edition_response_200_data_trends_item_rows_item_verdict_type_0 import (
            GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0,
        )

        name = self.name

        word = self.word

        ending = self.ending

        match_kind: str | Unset = UNSET
        if not isinstance(self.match_kind, Unset):
            match_kind = self.match_kind

        relation: None | str | Unset
        if isinstance(self.relation, Unset):
            relation = UNSET
        else:
            relation = self.relation

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        price: float | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        price_kind: None | str | Unset
        if isinstance(self.price_kind, Unset):
            price_kind = UNSET
        elif (
            isinstance(self.price_kind, str)
            or isinstance(self.price_kind, str)
            or isinstance(self.price_kind, str)
        ):
            price_kind = self.price_kind
        else:
            price_kind = self.price_kind

        quoted_by: None | str | Unset
        if isinstance(self.quoted_by, Unset):
            quoted_by = UNSET
        else:
            quoted_by = self.quoted_by

        renewal: float | None | Unset
        if isinstance(self.renewal, Unset):
            renewal = UNSET
        else:
            renewal = self.renewal

        five_year_cost: float | None | Unset
        if isinstance(self.five_year_cost, Unset):
            five_year_cost = UNSET
        else:
            five_year_cost = self.five_year_cost

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        upside_percent: float | None | Unset
        if isinstance(self.upside_percent, Unset):
            upside_percent = UNSET
        else:
            upside_percent = self.upside_percent

        upside_capped = self.upside_capped

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

        verdict: dict[str, Any] | None | Unset
        if isinstance(self.verdict, Unset):
            verdict = UNSET
        elif isinstance(
            self.verdict, GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0
        ):
            verdict = self.verdict.to_dict()
        else:
            verdict = self.verdict

        rating: str | Unset = UNSET
        if not isinstance(self.rating, Unset):
            rating = self.rating

        ideas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ideas, Unset):
            ideas = []
            for ideas_item_data in self.ideas:
                ideas_item = ideas_item_data.to_dict()
                ideas.append(ideas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if word is not UNSET:
            field_dict["word"] = word
        if ending is not UNSET:
            field_dict["ending"] = ending
        if match_kind is not UNSET:
            field_dict["matchKind"] = match_kind
        if relation is not UNSET:
            field_dict["relation"] = relation
        if status is not UNSET:
            field_dict["status"] = status
        if price is not UNSET:
            field_dict["price"] = price
        if price_kind is not UNSET:
            field_dict["priceKind"] = price_kind
        if quoted_by is not UNSET:
            field_dict["quotedBy"] = quoted_by
        if renewal is not UNSET:
            field_dict["renewal"] = renewal
        if five_year_cost is not UNSET:
            field_dict["fiveYearCost"] = five_year_cost
        if value is not UNSET:
            field_dict["value"] = value
        if upside_percent is not UNSET:
            field_dict["upsidePercent"] = upside_percent
        if upside_capped is not UNSET:
            field_dict["upsideCapped"] = upside_capped
        if liquidity is not UNSET:
            field_dict["liquidity"] = liquidity
        if verdict is not UNSET:
            field_dict["verdict"] = verdict
        if rating is not UNSET:
            field_dict["rating"] = rating
        if ideas is not UNSET:
            field_dict["ideas"] = ideas

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_latest_edition_response_200_data_trends_item_rows_item_ideas_item import (
            GetLatestEditionResponse200DataTrendsItemRowsItemIdeasItem,
        )
        from ..models.get_latest_edition_response_200_data_trends_item_rows_item_verdict_type_0 import (
            GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        word = d.pop("word", UNSET)

        ending = d.pop("ending", UNSET)

        _match_kind = d.pop("matchKind", UNSET)
        match_kind: GetLatestEditionResponse200DataTrendsItemRowsItemMatchKind | Unset
        if isinstance(_match_kind, Unset):
            match_kind = UNSET
        else:
            match_kind = check_get_latest_edition_response_200_data_trends_item_rows_item_match_kind(
                _match_kind
            )

        def _parse_relation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relation = _parse_relation(d.pop("relation", UNSET))

        _status = d.pop("status", UNSET)
        status: GetLatestEditionResponse200DataTrendsItemRowsItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = (
                check_get_latest_edition_response_200_data_trends_item_rows_item_status(
                    _status
                )
            )

        def _parse_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_price_kind(
            data: object,
        ) -> (
            GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType1
            | GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType2Type1
            | GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType3Type1
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
                price_kind_type_1 = check_get_latest_edition_response_200_data_trends_item_rows_item_price_kind_type_1(
                    data
                )

                return price_kind_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                price_kind_type_2_type_1 = check_get_latest_edition_response_200_data_trends_item_rows_item_price_kind_type_2_type_1(
                    data
                )

                return price_kind_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                price_kind_type_3_type_1 = check_get_latest_edition_response_200_data_trends_item_rows_item_price_kind_type_3_type_1(
                    data
                )

                return price_kind_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType1
                | GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType2Type1
                | GetLatestEditionResponse200DataTrendsItemRowsItemPriceKindType3Type1
                | None
                | Unset,
                data,
            )

        price_kind = _parse_price_kind(d.pop("priceKind", UNSET))

        def _parse_quoted_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quoted_by = _parse_quoted_by(d.pop("quotedBy", UNSET))

        def _parse_renewal(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        renewal = _parse_renewal(d.pop("renewal", UNSET))

        def _parse_five_year_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        five_year_cost = _parse_five_year_cost(d.pop("fiveYearCost", UNSET))

        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_upside_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        upside_percent = _parse_upside_percent(d.pop("upsidePercent", UNSET))

        upside_capped = d.pop("upsideCapped", UNSET)

        def _parse_liquidity(
            data: object,
        ) -> (
            GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType1
            | GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType2Type1
            | GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType3Type1
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
                liquidity_type_1 = check_get_latest_edition_response_200_data_trends_item_rows_item_liquidity_type_1(
                    data
                )

                return liquidity_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                liquidity_type_2_type_1 = check_get_latest_edition_response_200_data_trends_item_rows_item_liquidity_type_2_type_1(
                    data
                )

                return liquidity_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                liquidity_type_3_type_1 = check_get_latest_edition_response_200_data_trends_item_rows_item_liquidity_type_3_type_1(
                    data
                )

                return liquidity_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType1
                | GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType2Type1
                | GetLatestEditionResponse200DataTrendsItemRowsItemLiquidityType3Type1
                | None
                | Unset,
                data,
            )

        liquidity = _parse_liquidity(d.pop("liquidity", UNSET))

        def _parse_verdict(
            data: object,
        ) -> (
            GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0 | None | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verdict_type_0 = GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0.from_dict(
                    data
                )

                return verdict_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetLatestEditionResponse200DataTrendsItemRowsItemVerdictType0
                | None
                | Unset,
                data,
            )

        verdict = _parse_verdict(d.pop("verdict", UNSET))

        _rating = d.pop("rating", UNSET)
        rating: GetLatestEditionResponse200DataTrendsItemRowsItemRating | Unset
        if isinstance(_rating, Unset):
            rating = UNSET
        else:
            rating = (
                check_get_latest_edition_response_200_data_trends_item_rows_item_rating(
                    _rating
                )
            )

        _ideas = d.pop("ideas", UNSET)
        ideas: (
            list[GetLatestEditionResponse200DataTrendsItemRowsItemIdeasItem] | Unset
        ) = UNSET
        if _ideas is not UNSET:
            ideas = []
            for ideas_item_data in _ideas:
                ideas_item = GetLatestEditionResponse200DataTrendsItemRowsItemIdeasItem.from_dict(
                    ideas_item_data
                )

                ideas.append(ideas_item)

        get_latest_edition_response_200_data_trends_item_rows_item = cls(
            name=name,
            word=word,
            ending=ending,
            match_kind=match_kind,
            relation=relation,
            status=status,
            price=price,
            price_kind=price_kind,
            quoted_by=quoted_by,
            renewal=renewal,
            five_year_cost=five_year_cost,
            value=value,
            upside_percent=upside_percent,
            upside_capped=upside_capped,
            liquidity=liquidity,
            verdict=verdict,
            rating=rating,
            ideas=ideas,
        )

        get_latest_edition_response_200_data_trends_item_rows_item.additional_properties = d
        return get_latest_edition_response_200_data_trends_item_rows_item

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
