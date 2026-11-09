from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_tld_response_200_data_quality import (
    GetTldResponse200DataQuality,
    check_get_tld_response_200_data_quality,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_tld_response_200_data_market_type_0 import (
        GetTldResponse200DataMarketType0,
    )
    from ..models.get_tld_response_200_data_phases_item import (
        GetTldResponse200DataPhasesItem,
    )
    from ..models.get_tld_response_200_data_registrars_item import (
        GetTldResponse200DataRegistrarsItem,
    )
    from ..models.get_tld_response_200_data_registry import (
        GetTldResponse200DataRegistry,
    )


T = TypeVar("T", bound="GetTldResponse200Data")


@_attrs_define
class GetTldResponse200Data:
    """
    Attributes:
        slug (str):
        registry (GetTldResponse200DataRegistry):
        phases (list[GetTldResponse200DataPhasesItem]):
        market (GetTldResponse200DataMarketType0 | None):
        quality (GetTldResponse200DataQuality | Unset): Simple band of the nightly public score; public-set TLDs only.
        registrars (list[GetTldResponse200DataRegistrarsItem] | Unset):
        github_repo_url (None | str | Unset):
    """

    slug: str
    registry: GetTldResponse200DataRegistry
    phases: list[GetTldResponse200DataPhasesItem]
    market: GetTldResponse200DataMarketType0 | None
    quality: GetTldResponse200DataQuality | Unset = UNSET
    registrars: list[GetTldResponse200DataRegistrarsItem] | Unset = UNSET
    github_repo_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_tld_response_200_data_market_type_0 import (
            GetTldResponse200DataMarketType0,
        )

        slug = self.slug

        registry = self.registry.to_dict()

        phases = []
        for phases_item_data in self.phases:
            phases_item = phases_item_data.to_dict()
            phases.append(phases_item)

        market: dict[str, Any] | None
        if isinstance(self.market, GetTldResponse200DataMarketType0):
            market = self.market.to_dict()
        else:
            market = self.market

        quality: str | Unset = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality

        registrars: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.registrars, Unset):
            registrars = []
            for registrars_item_data in self.registrars:
                registrars_item = registrars_item_data.to_dict()
                registrars.append(registrars_item)

        github_repo_url: None | str | Unset
        if isinstance(self.github_repo_url, Unset):
            github_repo_url = UNSET
        else:
            github_repo_url = self.github_repo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "registry": registry,
                "phases": phases,
                "market": market,
            }
        )
        if quality is not UNSET:
            field_dict["quality"] = quality
        if registrars is not UNSET:
            field_dict["registrars"] = registrars
        if github_repo_url is not UNSET:
            field_dict["githubRepoUrl"] = github_repo_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_tld_response_200_data_market_type_0 import (
            GetTldResponse200DataMarketType0,
        )
        from ..models.get_tld_response_200_data_phases_item import (
            GetTldResponse200DataPhasesItem,
        )
        from ..models.get_tld_response_200_data_registrars_item import (
            GetTldResponse200DataRegistrarsItem,
        )
        from ..models.get_tld_response_200_data_registry import (
            GetTldResponse200DataRegistry,
        )

        d = dict(src_dict)
        slug = d.pop("slug")

        registry = GetTldResponse200DataRegistry.from_dict(d.pop("registry"))

        phases = []
        _phases = d.pop("phases")
        for phases_item_data in _phases:
            phases_item = GetTldResponse200DataPhasesItem.from_dict(phases_item_data)

            phases.append(phases_item)

        def _parse_market(data: object) -> GetTldResponse200DataMarketType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                market_type_0 = GetTldResponse200DataMarketType0.from_dict(data)

                return market_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetTldResponse200DataMarketType0 | None, data)

        market = _parse_market(d.pop("market"))

        _quality = d.pop("quality", UNSET)
        quality: GetTldResponse200DataQuality | Unset
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = check_get_tld_response_200_data_quality(_quality)

        _registrars = d.pop("registrars", UNSET)
        registrars: list[GetTldResponse200DataRegistrarsItem] | Unset = UNSET
        if _registrars is not UNSET:
            registrars = []
            for registrars_item_data in _registrars:
                registrars_item = GetTldResponse200DataRegistrarsItem.from_dict(
                    registrars_item_data
                )

                registrars.append(registrars_item)

        def _parse_github_repo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        github_repo_url = _parse_github_repo_url(d.pop("githubRepoUrl", UNSET))

        get_tld_response_200_data = cls(
            slug=slug,
            registry=registry,
            phases=phases,
            market=market,
            quality=quality,
            registrars=registrars,
            github_repo_url=github_repo_url,
        )

        get_tld_response_200_data.additional_properties = d
        return get_tld_response_200_data

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
