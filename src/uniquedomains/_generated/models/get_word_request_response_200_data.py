from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_word_request_response_200_data_reason import (
    GetWordRequestResponse200DataReason,
    check_get_word_request_response_200_data_reason,
)
from ..models.get_word_request_response_200_data_scan import (
    GetWordRequestResponse200DataScan,
    check_get_word_request_response_200_data_scan,
)
from ..models.get_word_request_response_200_data_status import (
    GetWordRequestResponse200DataStatus,
    check_get_word_request_response_200_data_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_word_request_response_200_data_word_type_0 import (
        GetWordRequestResponse200DataWordType0,
    )


T = TypeVar("T", bound="GetWordRequestResponse200Data")


@_attrs_define
class GetWordRequestResponse200Data:
    """
    Attributes:
        request_id (UUID):
        status (GetWordRequestResponse200DataStatus):
        requested_at (datetime.datetime):
        resolved_at (datetime.datetime | None): Null while queued.
        word (GetWordRequestResponse200DataWordType0 | None | Unset): On `ready`; null when the catalog no longer serves
            the word.
        scan (GetWordRequestResponse200DataScan | Unset): On `ready` with a word: whether the first scan of every ending
            ran.
        reason (GetWordRequestResponse200DataReason | Unset): On `rejected`.
    """

    request_id: UUID
    status: GetWordRequestResponse200DataStatus
    requested_at: datetime.datetime
    resolved_at: datetime.datetime | None
    word: GetWordRequestResponse200DataWordType0 | None | Unset = UNSET
    scan: GetWordRequestResponse200DataScan | Unset = UNSET
    reason: GetWordRequestResponse200DataReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_word_request_response_200_data_word_type_0 import (
            GetWordRequestResponse200DataWordType0,
        )

        request_id = str(self.request_id)

        status: str = self.status

        requested_at = self.requested_at.isoformat()

        resolved_at: None | str
        if isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        word: dict[str, Any] | None | Unset
        if isinstance(self.word, Unset):
            word = UNSET
        elif isinstance(self.word, GetWordRequestResponse200DataWordType0):
            word = self.word.to_dict()
        else:
            word = self.word

        scan: str | Unset = UNSET
        if not isinstance(self.scan, Unset):
            scan = self.scan

        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requestId": request_id,
                "status": status,
                "requestedAt": requested_at,
                "resolvedAt": resolved_at,
            }
        )
        if word is not UNSET:
            field_dict["word"] = word
        if scan is not UNSET:
            field_dict["scan"] = scan
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_word_request_response_200_data_word_type_0 import (
            GetWordRequestResponse200DataWordType0,
        )

        d = dict(src_dict)
        request_id = UUID(d.pop("requestId"))

        status = check_get_word_request_response_200_data_status(d.pop("status"))

        requested_at = datetime.datetime.fromisoformat(d.pop("requestedAt"))

        def _parse_resolved_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = datetime.datetime.fromisoformat(data)

                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        resolved_at = _parse_resolved_at(d.pop("resolvedAt"))

        def _parse_word(
            data: object,
        ) -> GetWordRequestResponse200DataWordType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                word_type_0 = GetWordRequestResponse200DataWordType0.from_dict(data)

                return word_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetWordRequestResponse200DataWordType0 | None | Unset, data)

        word = _parse_word(d.pop("word", UNSET))

        _scan = d.pop("scan", UNSET)
        scan: GetWordRequestResponse200DataScan | Unset
        if isinstance(_scan, Unset):
            scan = UNSET
        else:
            scan = check_get_word_request_response_200_data_scan(_scan)

        _reason = d.pop("reason", UNSET)
        reason: GetWordRequestResponse200DataReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_get_word_request_response_200_data_reason(_reason)

        get_word_request_response_200_data = cls(
            request_id=request_id,
            status=status,
            requested_at=requested_at,
            resolved_at=resolved_at,
            word=word,
            scan=scan,
            reason=reason,
        )

        get_word_request_response_200_data.additional_properties = d
        return get_word_request_response_200_data

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
