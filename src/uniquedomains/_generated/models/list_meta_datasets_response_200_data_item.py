from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListMetaDatasetsResponse200DataItem")


@_attrs_define
class ListMetaDatasetsResponse200DataItem:
    """
    Attributes:
        id (str):
        repository (str):
        url (str):
        endpoint (None | str):
        updated_on (datetime.date | None):
    """

    id: str
    repository: str
    url: str
    endpoint: None | str
    updated_on: datetime.date | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        repository = self.repository

        url = self.url

        endpoint: None | str
        endpoint = self.endpoint

        updated_on: None | str
        if isinstance(self.updated_on, datetime.date):
            updated_on = self.updated_on.isoformat()
        else:
            updated_on = self.updated_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "repository": repository,
                "url": url,
                "endpoint": endpoint,
                "updatedOn": updated_on,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        repository = d.pop("repository")

        url = d.pop("url")

        def _parse_endpoint(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        endpoint = _parse_endpoint(d.pop("endpoint"))

        def _parse_updated_on(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_on_type_0 = datetime.date.fromisoformat(data)

                return updated_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        updated_on = _parse_updated_on(d.pop("updatedOn"))

        list_meta_datasets_response_200_data_item = cls(
            id=id,
            repository=repository,
            url=url,
            endpoint=endpoint,
            updated_on=updated_on,
        )

        list_meta_datasets_response_200_data_item.additional_properties = d
        return list_meta_datasets_response_200_data_item

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
