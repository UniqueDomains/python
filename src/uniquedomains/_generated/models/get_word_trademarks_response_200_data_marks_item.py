from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_word_trademarks_response_200_data_marks_item_office import (
    GetWordTrademarksResponse200DataMarksItemOffice,
    check_get_word_trademarks_response_200_data_marks_item_office,
)
from ..models.get_word_trademarks_response_200_data_marks_item_status import (
    GetWordTrademarksResponse200DataMarksItemStatus,
    check_get_word_trademarks_response_200_data_marks_item_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWordTrademarksResponse200DataMarksItem")


@_attrs_define
class GetWordTrademarksResponse200DataMarksItem:
    """
    Attributes:
        office (GetWordTrademarksResponse200DataMarksItemOffice | Unset):
        serial (str | Unset):
        mark (str | Unset):
        registration (None | str | Unset):
        status (GetWordTrademarksResponse200DataMarksItemStatus | Unset):
        owner (None | str | Unset):
        filed (datetime.date | None | Unset):
        registered (datetime.date | None | Unset):
        nice_classes (list[str] | Unset):
        goods (None | str | Unset): At most 500 characters, live trademarks only.
        url (None | str | Unset):
    """

    office: GetWordTrademarksResponse200DataMarksItemOffice | Unset = UNSET
    serial: str | Unset = UNSET
    mark: str | Unset = UNSET
    registration: None | str | Unset = UNSET
    status: GetWordTrademarksResponse200DataMarksItemStatus | Unset = UNSET
    owner: None | str | Unset = UNSET
    filed: datetime.date | None | Unset = UNSET
    registered: datetime.date | None | Unset = UNSET
    nice_classes: list[str] | Unset = UNSET
    goods: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        office: str | Unset = UNSET
        if not isinstance(self.office, Unset):
            office = self.office

        serial = self.serial

        mark = self.mark

        registration: None | str | Unset
        if isinstance(self.registration, Unset):
            registration = UNSET
        else:
            registration = self.registration

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        owner: None | str | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        filed: None | str | Unset
        if isinstance(self.filed, Unset):
            filed = UNSET
        elif isinstance(self.filed, datetime.date):
            filed = self.filed.isoformat()
        else:
            filed = self.filed

        registered: None | str | Unset
        if isinstance(self.registered, Unset):
            registered = UNSET
        elif isinstance(self.registered, datetime.date):
            registered = self.registered.isoformat()
        else:
            registered = self.registered

        nice_classes: list[str] | Unset = UNSET
        if not isinstance(self.nice_classes, Unset):
            nice_classes = self.nice_classes

        goods: None | str | Unset
        if isinstance(self.goods, Unset):
            goods = UNSET
        else:
            goods = self.goods

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if office is not UNSET:
            field_dict["office"] = office
        if serial is not UNSET:
            field_dict["serial"] = serial
        if mark is not UNSET:
            field_dict["mark"] = mark
        if registration is not UNSET:
            field_dict["registration"] = registration
        if status is not UNSET:
            field_dict["status"] = status
        if owner is not UNSET:
            field_dict["owner"] = owner
        if filed is not UNSET:
            field_dict["filed"] = filed
        if registered is not UNSET:
            field_dict["registered"] = registered
        if nice_classes is not UNSET:
            field_dict["niceClasses"] = nice_classes
        if goods is not UNSET:
            field_dict["goods"] = goods
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _office = d.pop("office", UNSET)
        office: GetWordTrademarksResponse200DataMarksItemOffice | Unset
        if isinstance(_office, Unset):
            office = UNSET
        else:
            office = check_get_word_trademarks_response_200_data_marks_item_office(
                _office
            )

        serial = d.pop("serial", UNSET)

        mark = d.pop("mark", UNSET)

        def _parse_registration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration = _parse_registration(d.pop("registration", UNSET))

        _status = d.pop("status", UNSET)
        status: GetWordTrademarksResponse200DataMarksItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_get_word_trademarks_response_200_data_marks_item_status(
                _status
            )

        def _parse_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        def _parse_filed(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                filed_type_0 = datetime.date.fromisoformat(data)

                return filed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        filed = _parse_filed(d.pop("filed", UNSET))

        def _parse_registered(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registered_type_0 = datetime.date.fromisoformat(data)

                return registered_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        registered = _parse_registered(d.pop("registered", UNSET))

        nice_classes = cast(list[str], d.pop("niceClasses", UNSET))

        def _parse_goods(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        goods = _parse_goods(d.pop("goods", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        get_word_trademarks_response_200_data_marks_item = cls(
            office=office,
            serial=serial,
            mark=mark,
            registration=registration,
            status=status,
            owner=owner,
            filed=filed,
            registered=registered,
            nice_classes=nice_classes,
            goods=goods,
            url=url,
        )

        get_word_trademarks_response_200_data_marks_item.additional_properties = d
        return get_word_trademarks_response_200_data_marks_item

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
