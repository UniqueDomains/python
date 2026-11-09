from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_tlds_response_200_data_item_iana_status_type_0 import (
    ListTldsResponse200DataItemIanaStatusType0,
    check_list_tlds_response_200_data_item_iana_status_type_0,
)
from ..models.list_tlds_response_200_data_item_kind import (
    ListTldsResponse200DataItemKind,
    check_list_tlds_response_200_data_item_kind,
)

if TYPE_CHECKING:
    from ..models.list_tlds_response_200_data_item_insights_type_0 import (
        ListTldsResponse200DataItemInsightsType0,
    )
    from ..models.list_tlds_response_200_data_item_phases_item import (
        ListTldsResponse200DataItemPhasesItem,
    )


T = TypeVar("T", bound="ListTldsResponse200DataItem")


@_attrs_define
class ListTldsResponse200DataItem:
    """
    Attributes:
        tld (str): The ending with its dot (`.ai`).
        slug (str): The bare ending, the row key and cursor key.
        iana_status (ListTldsResponse200DataItemIanaStatusType0 | None):
        kind (ListTldsResponse200DataItemKind): Catalog kind.
        iana_type (None | str):
        registry_operator (None | str):
        registry_country_code (None | str):
        is_brand (bool): Brand TLD (Specification 13).
        is_idn (bool): Internationalised ending.
        delegated_on (datetime.date | None):
        removed_on (datetime.date | None):
        contract_terminated (bool): Registry agreement terminated.
        rdap_server (None | str):
        category (None | str):
        phases (list[ListTldsResponse200DataItemPhasesItem]):
        insights (ListTldsResponse200DataItemInsightsType0 | None):
    """

    tld: str
    slug: str
    iana_status: ListTldsResponse200DataItemIanaStatusType0 | None
    kind: ListTldsResponse200DataItemKind
    iana_type: None | str
    registry_operator: None | str
    registry_country_code: None | str
    is_brand: bool
    is_idn: bool
    delegated_on: datetime.date | None
    removed_on: datetime.date | None
    contract_terminated: bool
    rdap_server: None | str
    category: None | str
    phases: list[ListTldsResponse200DataItemPhasesItem]
    insights: ListTldsResponse200DataItemInsightsType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_tlds_response_200_data_item_insights_type_0 import (
            ListTldsResponse200DataItemInsightsType0,
        )

        tld = self.tld

        slug = self.slug

        iana_status: None | str
        if isinstance(self.iana_status, str):
            iana_status = self.iana_status
        else:
            iana_status = self.iana_status

        kind: str = self.kind

        iana_type: None | str
        iana_type = self.iana_type

        registry_operator: None | str
        registry_operator = self.registry_operator

        registry_country_code: None | str
        registry_country_code = self.registry_country_code

        is_brand = self.is_brand

        is_idn = self.is_idn

        delegated_on: None | str
        if isinstance(self.delegated_on, datetime.date):
            delegated_on = self.delegated_on.isoformat()
        else:
            delegated_on = self.delegated_on

        removed_on: None | str
        if isinstance(self.removed_on, datetime.date):
            removed_on = self.removed_on.isoformat()
        else:
            removed_on = self.removed_on

        contract_terminated = self.contract_terminated

        rdap_server: None | str
        rdap_server = self.rdap_server

        category: None | str
        category = self.category

        phases = []
        for phases_item_data in self.phases:
            phases_item = phases_item_data.to_dict()
            phases.append(phases_item)

        insights: dict[str, Any] | None
        if isinstance(self.insights, ListTldsResponse200DataItemInsightsType0):
            insights = self.insights.to_dict()
        else:
            insights = self.insights

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tld": tld,
                "slug": slug,
                "ianaStatus": iana_status,
                "kind": kind,
                "ianaType": iana_type,
                "registryOperator": registry_operator,
                "registryCountryCode": registry_country_code,
                "isBrand": is_brand,
                "isIdn": is_idn,
                "delegatedOn": delegated_on,
                "removedOn": removed_on,
                "contractTerminated": contract_terminated,
                "rdapServer": rdap_server,
                "category": category,
                "phases": phases,
                "insights": insights,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_tlds_response_200_data_item_insights_type_0 import (
            ListTldsResponse200DataItemInsightsType0,
        )
        from ..models.list_tlds_response_200_data_item_phases_item import (
            ListTldsResponse200DataItemPhasesItem,
        )

        d = dict(src_dict)
        tld = d.pop("tld")

        slug = d.pop("slug")

        def _parse_iana_status(
            data: object,
        ) -> ListTldsResponse200DataItemIanaStatusType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                iana_status_type_0 = (
                    check_list_tlds_response_200_data_item_iana_status_type_0(data)
                )

                return iana_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListTldsResponse200DataItemIanaStatusType0 | None, data)

        iana_status = _parse_iana_status(d.pop("ianaStatus"))

        kind = check_list_tlds_response_200_data_item_kind(d.pop("kind"))

        def _parse_iana_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        iana_type = _parse_iana_type(d.pop("ianaType"))

        def _parse_registry_operator(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        registry_operator = _parse_registry_operator(d.pop("registryOperator"))

        def _parse_registry_country_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        registry_country_code = _parse_registry_country_code(
            d.pop("registryCountryCode")
        )

        is_brand = d.pop("isBrand")

        is_idn = d.pop("isIdn")

        def _parse_delegated_on(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegated_on_type_0 = datetime.date.fromisoformat(data)

                return delegated_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        delegated_on = _parse_delegated_on(d.pop("delegatedOn"))

        def _parse_removed_on(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                removed_on_type_0 = datetime.date.fromisoformat(data)

                return removed_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        removed_on = _parse_removed_on(d.pop("removedOn"))

        contract_terminated = d.pop("contractTerminated")

        def _parse_rdap_server(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rdap_server = _parse_rdap_server(d.pop("rdapServer"))

        def _parse_category(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        category = _parse_category(d.pop("category"))

        phases = []
        _phases = d.pop("phases")
        for phases_item_data in _phases:
            phases_item = ListTldsResponse200DataItemPhasesItem.from_dict(
                phases_item_data
            )

            phases.append(phases_item)

        def _parse_insights(
            data: object,
        ) -> ListTldsResponse200DataItemInsightsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                insights_type_0 = ListTldsResponse200DataItemInsightsType0.from_dict(
                    data
                )

                return insights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListTldsResponse200DataItemInsightsType0 | None, data)

        insights = _parse_insights(d.pop("insights"))

        list_tlds_response_200_data_item = cls(
            tld=tld,
            slug=slug,
            iana_status=iana_status,
            kind=kind,
            iana_type=iana_type,
            registry_operator=registry_operator,
            registry_country_code=registry_country_code,
            is_brand=is_brand,
            is_idn=is_idn,
            delegated_on=delegated_on,
            removed_on=removed_on,
            contract_terminated=contract_terminated,
            rdap_server=rdap_server,
            category=category,
            phases=phases,
            insights=insights,
        )

        list_tlds_response_200_data_item.additional_properties = d
        return list_tlds_response_200_data_item

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
