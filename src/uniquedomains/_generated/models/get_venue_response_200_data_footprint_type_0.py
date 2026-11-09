from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetVenueResponse200DataFootprintType0")


@_attrs_define
class GetVenueResponse200DataFootprintType0:
    """
    Attributes:
        names (int): Scanned names parked at the venue, rounded (to 100, to 10 under 1,000).
        listed (int | None):
        parked (int | None):
        arrivals_week (int): Names that arrived over the last seven days.
        departures_week (int): Names that left over the last seven days.
    """

    names: int
    listed: int | None
    parked: int | None
    arrivals_week: int
    departures_week: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        names = self.names

        listed: int | None
        listed = self.listed

        parked: int | None
        parked = self.parked

        arrivals_week = self.arrivals_week

        departures_week = self.departures_week

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "names": names,
                "listed": listed,
                "parked": parked,
                "arrivalsWeek": arrivals_week,
                "departuresWeek": departures_week,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        names = d.pop("names")

        def _parse_listed(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        listed = _parse_listed(d.pop("listed"))

        def _parse_parked(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        parked = _parse_parked(d.pop("parked"))

        arrivals_week = d.pop("arrivalsWeek")

        departures_week = d.pop("departuresWeek")

        get_venue_response_200_data_footprint_type_0 = cls(
            names=names,
            listed=listed,
            parked=parked,
            arrivals_week=arrivals_week,
            departures_week=departures_week,
        )

        get_venue_response_200_data_footprint_type_0.additional_properties = d
        return get_venue_response_200_data_footprint_type_0

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
