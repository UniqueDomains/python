from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_tld_application_string_response_200_data_applications_item import (
        GetTldApplicationStringResponse200DataApplicationsItem,
    )
    from ..models.get_tld_application_string_response_200_data_changes_item import (
        GetTldApplicationStringResponse200DataChangesItem,
    )


T = TypeVar("T", bound="GetTldApplicationStringResponse200Data")


@_attrs_define
class GetTldApplicationStringResponse200Data:
    """
    Attributes:
        string (str):
        applications (list[GetTldApplicationStringResponse200DataApplicationsItem]):
        changes (list[GetTldApplicationStringResponse200DataChangesItem]):
    """

    string: str
    applications: list[GetTldApplicationStringResponse200DataApplicationsItem]
    changes: list[GetTldApplicationStringResponse200DataChangesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        string = self.string

        applications = []
        for applications_item_data in self.applications:
            applications_item = applications_item_data.to_dict()
            applications.append(applications_item)

        changes = []
        for changes_item_data in self.changes:
            changes_item = changes_item_data.to_dict()
            changes.append(changes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "string": string,
                "applications": applications,
                "changes": changes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_tld_application_string_response_200_data_applications_item import (
            GetTldApplicationStringResponse200DataApplicationsItem,
        )
        from ..models.get_tld_application_string_response_200_data_changes_item import (
            GetTldApplicationStringResponse200DataChangesItem,
        )

        d = dict(src_dict)
        string = d.pop("string")

        applications = []
        _applications = d.pop("applications")
        for applications_item_data in _applications:
            applications_item = (
                GetTldApplicationStringResponse200DataApplicationsItem.from_dict(
                    applications_item_data
                )
            )

            applications.append(applications_item)

        changes = []
        _changes = d.pop("changes")
        for changes_item_data in _changes:
            changes_item = GetTldApplicationStringResponse200DataChangesItem.from_dict(
                changes_item_data
            )

            changes.append(changes_item)

        get_tld_application_string_response_200_data = cls(
            string=string,
            applications=applications,
            changes=changes,
        )

        get_tld_application_string_response_200_data.additional_properties = d
        return get_tld_application_string_response_200_data

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
