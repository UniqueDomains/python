from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_cheapest_prices_response_200_data_item_cheapest_renewal_type_0 import (
        ListCheapestPricesResponse200DataItemCheapestRenewalType0,
    )
    from ..models.list_cheapest_prices_response_200_data_item_cheapest_transfer_type_0 import (
        ListCheapestPricesResponse200DataItemCheapestTransferType0,
    )
    from ..models.list_cheapest_prices_response_200_data_item_cheapest_year_1_type_0 import (
        ListCheapestPricesResponse200DataItemCheapestYear1Type0,
    )


T = TypeVar("T", bound="ListCheapestPricesResponse200DataItem")


@_attrs_define
class ListCheapestPricesResponse200DataItem:
    """
    Attributes:
        ending (str):
        cheapest_year_1 (ListCheapestPricesResponse200DataItemCheapestYear1Type0 | None):
        cheapest_renewal (ListCheapestPricesResponse200DataItemCheapestRenewalType0 | None):
        cheapest_transfer (ListCheapestPricesResponse200DataItemCheapestTransferType0 | None):
        trap (bool | None):
    """

    ending: str
    cheapest_year_1: ListCheapestPricesResponse200DataItemCheapestYear1Type0 | None
    cheapest_renewal: ListCheapestPricesResponse200DataItemCheapestRenewalType0 | None
    cheapest_transfer: ListCheapestPricesResponse200DataItemCheapestTransferType0 | None
    trap: bool | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_cheapest_prices_response_200_data_item_cheapest_renewal_type_0 import (
            ListCheapestPricesResponse200DataItemCheapestRenewalType0,
        )
        from ..models.list_cheapest_prices_response_200_data_item_cheapest_transfer_type_0 import (
            ListCheapestPricesResponse200DataItemCheapestTransferType0,
        )
        from ..models.list_cheapest_prices_response_200_data_item_cheapest_year_1_type_0 import (
            ListCheapestPricesResponse200DataItemCheapestYear1Type0,
        )

        ending = self.ending

        cheapest_year_1: dict[str, Any] | None
        if isinstance(
            self.cheapest_year_1,
            ListCheapestPricesResponse200DataItemCheapestYear1Type0,
        ):
            cheapest_year_1 = self.cheapest_year_1.to_dict()
        else:
            cheapest_year_1 = self.cheapest_year_1

        cheapest_renewal: dict[str, Any] | None
        if isinstance(
            self.cheapest_renewal,
            ListCheapestPricesResponse200DataItemCheapestRenewalType0,
        ):
            cheapest_renewal = self.cheapest_renewal.to_dict()
        else:
            cheapest_renewal = self.cheapest_renewal

        cheapest_transfer: dict[str, Any] | None
        if isinstance(
            self.cheapest_transfer,
            ListCheapestPricesResponse200DataItemCheapestTransferType0,
        ):
            cheapest_transfer = self.cheapest_transfer.to_dict()
        else:
            cheapest_transfer = self.cheapest_transfer

        trap: bool | None
        trap = self.trap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ending": ending,
                "cheapestYear1": cheapest_year_1,
                "cheapestRenewal": cheapest_renewal,
                "cheapestTransfer": cheapest_transfer,
                "trap": trap,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_cheapest_prices_response_200_data_item_cheapest_renewal_type_0 import (
            ListCheapestPricesResponse200DataItemCheapestRenewalType0,
        )
        from ..models.list_cheapest_prices_response_200_data_item_cheapest_transfer_type_0 import (
            ListCheapestPricesResponse200DataItemCheapestTransferType0,
        )
        from ..models.list_cheapest_prices_response_200_data_item_cheapest_year_1_type_0 import (
            ListCheapestPricesResponse200DataItemCheapestYear1Type0,
        )

        d = dict(src_dict)
        ending = d.pop("ending")

        def _parse_cheapest_year_1(
            data: object,
        ) -> ListCheapestPricesResponse200DataItemCheapestYear1Type0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cheapest_year_1_type_0 = (
                    ListCheapestPricesResponse200DataItemCheapestYear1Type0.from_dict(
                        data
                    )
                )

                return cheapest_year_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListCheapestPricesResponse200DataItemCheapestYear1Type0 | None, data
            )

        cheapest_year_1 = _parse_cheapest_year_1(d.pop("cheapestYear1"))

        def _parse_cheapest_renewal(
            data: object,
        ) -> ListCheapestPricesResponse200DataItemCheapestRenewalType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cheapest_renewal_type_0 = (
                    ListCheapestPricesResponse200DataItemCheapestRenewalType0.from_dict(
                        data
                    )
                )

                return cheapest_renewal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListCheapestPricesResponse200DataItemCheapestRenewalType0 | None, data
            )

        cheapest_renewal = _parse_cheapest_renewal(d.pop("cheapestRenewal"))

        def _parse_cheapest_transfer(
            data: object,
        ) -> ListCheapestPricesResponse200DataItemCheapestTransferType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cheapest_transfer_type_0 = ListCheapestPricesResponse200DataItemCheapestTransferType0.from_dict(
                    data
                )

                return cheapest_transfer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListCheapestPricesResponse200DataItemCheapestTransferType0 | None, data
            )

        cheapest_transfer = _parse_cheapest_transfer(d.pop("cheapestTransfer"))

        def _parse_trap(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        trap = _parse_trap(d.pop("trap"))

        list_cheapest_prices_response_200_data_item = cls(
            ending=ending,
            cheapest_year_1=cheapest_year_1,
            cheapest_renewal=cheapest_renewal,
            cheapest_transfer=cheapest_transfer,
            trap=trap,
        )

        list_cheapest_prices_response_200_data_item.additional_properties = d
        return list_cheapest_prices_response_200_data_item

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
