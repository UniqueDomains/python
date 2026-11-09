from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_word_response_200_data_status import (
    RequestWordResponse200DataStatus,
    check_request_word_response_200_data_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_word_response_200_data_word import (
        RequestWordResponse200DataWord,
    )


T = TypeVar("T", bound="RequestWordResponse200Data")


@_attrs_define
class RequestWordResponse200Data:
    """
    Attributes:
        status (RequestWordResponse200DataStatus):
        request_id (UUID | Unset): On `accepted` and `queued`.
        poll (str | Unset): `/v1/words/requests/<requestId>`; on `accepted`.
        word (RequestWordResponse200DataWord | Unset): On `in_catalog`.
    """

    status: RequestWordResponse200DataStatus
    request_id: UUID | Unset = UNSET
    poll: str | Unset = UNSET
    word: RequestWordResponse200DataWord | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        request_id: str | Unset = UNSET
        if not isinstance(self.request_id, Unset):
            request_id = str(self.request_id)

        poll = self.poll

        word: dict[str, Any] | Unset = UNSET
        if not isinstance(self.word, Unset):
            word = self.word.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if poll is not UNSET:
            field_dict["poll"] = poll
        if word is not UNSET:
            field_dict["word"] = word

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.request_word_response_200_data_word import (
            RequestWordResponse200DataWord,
        )

        d = dict(src_dict)
        status = check_request_word_response_200_data_status(d.pop("status"))

        _request_id = d.pop("requestId", UNSET)
        request_id: UUID | Unset
        if isinstance(_request_id, Unset):
            request_id = UNSET
        else:
            request_id = UUID(_request_id)

        poll = d.pop("poll", UNSET)

        _word = d.pop("word", UNSET)
        word: RequestWordResponse200DataWord | Unset
        if isinstance(_word, Unset):
            word = UNSET
        else:
            word = RequestWordResponse200DataWord.from_dict(_word)

        request_word_response_200_data = cls(
            status=status,
            request_id=request_id,
            poll=poll,
            word=word,
        )

        request_word_response_200_data.additional_properties = d
        return request_word_response_200_data

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
