from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_domain_changes_response_200_data_item_type import (
    ListDomainChangesResponse200DataItemType,
    check_list_domain_changes_response_200_data_item_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_domain_changes_response_200_data_item_after_type_0 import (
        ListDomainChangesResponse200DataItemAfterType0,
    )
    from ..models.list_domain_changes_response_200_data_item_before_type_0 import (
        ListDomainChangesResponse200DataItemBeforeType0,
    )
    from ..models.list_domain_changes_response_200_data_item_subject import (
        ListDomainChangesResponse200DataItemSubject,
    )


T = TypeVar("T", bound="ListDomainChangesResponse200DataItem")


@_attrs_define
class ListDomainChangesResponse200DataItem:
    """
    Attributes:
        id (UUID | Unset):
        name (str | Unset):
        type_ (ListDomainChangesResponse200DataItemType | Unset):
        observed_at (datetime.datetime | Unset):
        subject (ListDomainChangesResponse200DataItemSubject | Unset):
        before (ListDomainChangesResponse200DataItemBeforeType0 | None | Unset):
        after (ListDomainChangesResponse200DataItemAfterType0 | None | Unset):
        expires_at (datetime.datetime | None | Unset):
    """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    type_: ListDomainChangesResponse200DataItemType | Unset = UNSET
    observed_at: datetime.datetime | Unset = UNSET
    subject: ListDomainChangesResponse200DataItemSubject | Unset = UNSET
    before: ListDomainChangesResponse200DataItemBeforeType0 | None | Unset = UNSET
    after: ListDomainChangesResponse200DataItemAfterType0 | None | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_domain_changes_response_200_data_item_after_type_0 import (
            ListDomainChangesResponse200DataItemAfterType0,
        )
        from ..models.list_domain_changes_response_200_data_item_before_type_0 import (
            ListDomainChangesResponse200DataItemBeforeType0,
        )

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        observed_at: str | Unset = UNSET
        if not isinstance(self.observed_at, Unset):
            observed_at = self.observed_at.isoformat()

        subject: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subject, Unset):
            subject = self.subject.to_dict()

        before: dict[str, Any] | None | Unset
        if isinstance(self.before, Unset):
            before = UNSET
        elif isinstance(self.before, ListDomainChangesResponse200DataItemBeforeType0):
            before = self.before.to_dict()
        else:
            before = self.before

        after: dict[str, Any] | None | Unset
        if isinstance(self.after, Unset):
            after = UNSET
        elif isinstance(self.after, ListDomainChangesResponse200DataItemAfterType0):
            after = self.after.to_dict()
        else:
            after = self.after

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if observed_at is not UNSET:
            field_dict["observedAt"] = observed_at
        if subject is not UNSET:
            field_dict["subject"] = subject
        if before is not UNSET:
            field_dict["before"] = before
        if after is not UNSET:
            field_dict["after"] = after
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_domain_changes_response_200_data_item_after_type_0 import (
            ListDomainChangesResponse200DataItemAfterType0,
        )
        from ..models.list_domain_changes_response_200_data_item_before_type_0 import (
            ListDomainChangesResponse200DataItemBeforeType0,
        )
        from ..models.list_domain_changes_response_200_data_item_subject import (
            ListDomainChangesResponse200DataItemSubject,
        )

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ListDomainChangesResponse200DataItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_list_domain_changes_response_200_data_item_type(_type_)

        _observed_at = d.pop("observedAt", UNSET)
        observed_at: datetime.datetime | Unset
        if isinstance(_observed_at, Unset):
            observed_at = UNSET
        else:
            observed_at = datetime.datetime.fromisoformat(_observed_at)

        _subject = d.pop("subject", UNSET)
        subject: ListDomainChangesResponse200DataItemSubject | Unset
        if isinstance(_subject, Unset):
            subject = UNSET
        else:
            subject = ListDomainChangesResponse200DataItemSubject.from_dict(_subject)

        def _parse_before(
            data: object,
        ) -> ListDomainChangesResponse200DataItemBeforeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                before_type_0 = (
                    ListDomainChangesResponse200DataItemBeforeType0.from_dict(data)
                )

                return before_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListDomainChangesResponse200DataItemBeforeType0 | None | Unset, data
            )

        before = _parse_before(d.pop("before", UNSET))

        def _parse_after(
            data: object,
        ) -> ListDomainChangesResponse200DataItemAfterType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                after_type_0 = ListDomainChangesResponse200DataItemAfterType0.from_dict(
                    data
                )

                return after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListDomainChangesResponse200DataItemAfterType0 | None | Unset, data
            )

        after = _parse_after(d.pop("after", UNSET))

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))

        list_domain_changes_response_200_data_item = cls(
            id=id,
            name=name,
            type_=type_,
            observed_at=observed_at,
            subject=subject,
            before=before,
            after=after,
            expires_at=expires_at,
        )

        list_domain_changes_response_200_data_item.additional_properties = d
        return list_domain_changes_response_200_data_item

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
