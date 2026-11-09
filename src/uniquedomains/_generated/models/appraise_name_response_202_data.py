from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.appraise_name_response_202_data_current_type_0 import (
        AppraiseNameResponse202DataCurrentType0,
    )
    from ..models.appraise_name_response_202_data_history_item import (
        AppraiseNameResponse202DataHistoryItem,
    )


T = TypeVar("T", bound="AppraiseNameResponse202Data")


@_attrs_define
class AppraiseNameResponse202Data:
    """
    Attributes:
        current (AppraiseNameResponse202DataCurrentType0 | None):
        history (list[AppraiseNameResponse202DataHistoryItem]):
    """

    current: AppraiseNameResponse202DataCurrentType0 | None
    history: list[AppraiseNameResponse202DataHistoryItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.appraise_name_response_202_data_current_type_0 import (
            AppraiseNameResponse202DataCurrentType0,
        )

        current: dict[str, Any] | None
        if isinstance(self.current, AppraiseNameResponse202DataCurrentType0):
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
        from ..models.appraise_name_response_202_data_current_type_0 import (
            AppraiseNameResponse202DataCurrentType0,
        )
        from ..models.appraise_name_response_202_data_history_item import (
            AppraiseNameResponse202DataHistoryItem,
        )

        d = dict(src_dict)

        def _parse_current(
            data: object,
        ) -> AppraiseNameResponse202DataCurrentType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_type_0 = AppraiseNameResponse202DataCurrentType0.from_dict(data)

                return current_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AppraiseNameResponse202DataCurrentType0 | None, data)

        current = _parse_current(d.pop("current"))

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = AppraiseNameResponse202DataHistoryItem.from_dict(
                history_item_data
            )

            history.append(history_item)

        appraise_name_response_202_data = cls(
            current=current,
            history=history,
        )

        appraise_name_response_202_data.additional_properties = d
        return appraise_name_response_202_data

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
