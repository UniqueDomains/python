from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_name_dns_response_200_data_mx_item import (
        GetNameDnsResponse200DataMxItem,
    )


T = TypeVar("T", bound="GetNameDnsResponse200Data")


@_attrs_define
class GetNameDnsResponse200Data:
    """
    Attributes:
        read (bool):
        ns (list[str]):
        a (list[str]):
        aaaa (list[str]):
        cname (list[str]):
        mx (list[GetNameDnsResponse200DataMxItem]):
        has_website (bool | None):
        parking (None | str):
    """

    read: bool
    ns: list[str]
    a: list[str]
    aaaa: list[str]
    cname: list[str]
    mx: list[GetNameDnsResponse200DataMxItem]
    has_website: bool | None
    parking: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        read = self.read

        ns = self.ns

        a = self.a

        aaaa = self.aaaa

        cname = self.cname

        mx = []
        for mx_item_data in self.mx:
            mx_item = mx_item_data.to_dict()
            mx.append(mx_item)

        has_website: bool | None
        has_website = self.has_website

        parking: None | str
        parking = self.parking

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "read": read,
                "ns": ns,
                "a": a,
                "aaaa": aaaa,
                "cname": cname,
                "mx": mx,
                "hasWebsite": has_website,
                "parking": parking,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_name_dns_response_200_data_mx_item import (
            GetNameDnsResponse200DataMxItem,
        )

        d = dict(src_dict)
        read = d.pop("read")

        ns = cast(list[str], d.pop("ns"))

        a = cast(list[str], d.pop("a"))

        aaaa = cast(list[str], d.pop("aaaa"))

        cname = cast(list[str], d.pop("cname"))

        mx = []
        _mx = d.pop("mx")
        for mx_item_data in _mx:
            mx_item = GetNameDnsResponse200DataMxItem.from_dict(mx_item_data)

            mx.append(mx_item)

        def _parse_has_website(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        has_website = _parse_has_website(d.pop("hasWebsite"))

        def _parse_parking(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parking = _parse_parking(d.pop("parking"))

        get_name_dns_response_200_data = cls(
            read=read,
            ns=ns,
            a=a,
            aaaa=aaaa,
            cname=cname,
            mx=mx,
            has_website=has_website,
            parking=parking,
        )

        get_name_dns_response_200_data.additional_properties = d
        return get_name_dns_response_200_data

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
