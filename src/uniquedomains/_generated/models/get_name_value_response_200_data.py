from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_name_value_response_200_data_current_type_0 import (
        GetNameValueResponse200DataCurrentType0,
    )
    from ..models.get_name_value_response_200_data_history_item import (
        GetNameValueResponse200DataHistoryItem,
    )


T = TypeVar("T", bound="GetNameValueResponse200Data")


@_attrs_define
class GetNameValueResponse200Data:
    """
    Attributes:
        current (GetNameValueResponse200DataCurrentType0 | None):
        history (list[GetNameValueResponse200DataHistoryItem]):
    """

    current: GetNameValueResponse200DataCurrentType0 | None
    history: list[GetNameValueResponse200DataHistoryItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_name_value_response_200_data_current_type_0 import (
            GetNameValueResponse200DataCurrentType0,
        )

        current: dict[str, Any] | None
        if isinstance(self.current, GetNameValueResponse200DataCurrentType0):
            current = self.current.to_dict()
        else:
            current = self.current

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current": current,
                "history": history,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_name_value_response_200_data_current_type_0 import (
            GetNameValueResponse200DataCurrentType0,
        )
        from ..models.get_name_value_response_200_data_history_item import (
            GetNameValueResponse200DataHistoryItem,
        )

        d = dict(src_dict)

        def _parse_current(
            data: object,
        ) -> GetNameValueResponse200DataCurrentType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_type_0 = GetNameValueResponse200DataCurrentType0.from_dict(data)

                return current_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetNameValueResponse200DataCurrentType0 | None, data)

        current = _parse_current(d.pop("current"))

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = GetNameValueResponse200DataHistoryItem.from_dict(
                history_item_data
            )

            history.append(history_item)

        get_name_value_response_200_data = cls(
            current=current,
            history=history,
        )

        get_name_value_response_200_data.additional_properties = d
        return get_name_value_response_200_data

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
