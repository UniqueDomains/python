from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_price_traps_response_200_data_item_cheapest_renewal_elsewhere_type_0 import (
        ListPriceTrapsResponse200DataItemCheapestRenewalElsewhereType0,
    )
    from ..models.list_price_traps_response_200_data_item_cheapest_year_one import (
        ListPriceTrapsResponse200DataItemCheapestYearOne,
    )


T = TypeVar("T", bound="ListPriceTrapsResponse200DataItem")


@_attrs_define
class ListPriceTrapsResponse200DataItem:
    """
    Attributes:
        tld (str): Bare ending.
        multiple (float): The cheapest first year's renewal over that first year, one decimal.
        cheapest_year_one (ListPriceTrapsResponse200DataItemCheapestYearOne):
        cheapest_renewal_elsewhere (ListPriceTrapsResponse200DataItemCheapestRenewalElsewhereType0 | None):
    """

    tld: str
    multiple: float
    cheapest_year_one: ListPriceTrapsResponse200DataItemCheapestYearOne
    cheapest_renewal_elsewhere: (
        ListPriceTrapsResponse200DataItemCheapestRenewalElsewhereType0 | None
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_price_traps_response_200_data_item_cheapest_renewal_elsewhere_type_0 import (
            ListPriceTrapsResponse200DataItemCheapestRenewalElsewhereType0,
        )

        tld = self.tld

        multiple = self.multiple

        cheapest_year_one = self.cheapest_year_one.to_dict()

        cheapest_renewal_elsewhere: dict[str, Any] | None
        if isinstance(
            self.cheapest_renewal_elsewhere,
            ListPriceTrapsResponse200DataItemCheapestRenewalElsewhereType0,
        ):
            cheapest_renewal_elsewhere = self.cheapest_renewal_elsewhere.to_dict()
        else:
            cheapest_renewal_elsewhere = self.cheapest_renewal_elsewhere

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tld": tld,
                "multiple": multiple,
                "cheapestYearOne": cheapest_year_one,
                "cheapestRenewalElsewhere": cheapest_renewal_elsewhere,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_price_traps_response_200_data_item_cheapest_renewal_elsewhere_type_0 import (
            ListPriceTrapsResponse200DataItemCheapestRenewalElsewhereType0,
        )
        from ..models.list_price_traps_response_200_data_item_cheapest_year_one import (
            ListPriceTrapsResponse200DataItemCheapestYearOne,
        )

        d = dict(src_dict)
        tld = d.pop("tld")

        multiple = d.pop("multiple")

        cheapest_year_one = ListPriceTrapsResponse200DataItemCheapestYearOne.from_dict(
            d.pop("cheapestYearOne")
        )

        def _parse_cheapest_renewal_elsewhere(
            data: object,
        ) -> ListPriceTrapsResponse200DataItemCheapestRenewalElsewhereType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cheapest_renewal_elsewhere_type_0 = ListPriceTrapsResponse200DataItemCheapestRenewalElsewhereType0.from_dict(
                    data
                )

                return cheapest_renewal_elsewhere_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListPriceTrapsResponse200DataItemCheapestRenewalElsewhereType0 | None,
                data,
            )

        cheapest_renewal_elsewhere = _parse_cheapest_renewal_elsewhere(
            d.pop("cheapestRenewalElsewhere")
        )

        list_price_traps_response_200_data_item = cls(
            tld=tld,
            multiple=multiple,
            cheapest_year_one=cheapest_year_one,
            cheapest_renewal_elsewhere=cheapest_renewal_elsewhere,
        )

        list_price_traps_response_200_data_item.additional_properties = d
        return list_price_traps_response_200_data_item

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
