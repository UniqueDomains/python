from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_tld_applications_response_200_data_item_comparable_sales_band_type_0 import (
    ListTldApplicationsResponse200DataItemComparableSalesBandType0,
    check_list_tld_applications_response_200_data_item_comparable_sales_band_type_0,
)
from ..models.list_tld_applications_response_200_data_item_status_key_type_0 import (
    ListTldApplicationsResponse200DataItemStatusKeyType0,
    check_list_tld_applications_response_200_data_item_status_key_type_0,
)
from ..models.list_tld_applications_response_200_data_item_type_key_type_0 import (
    ListTldApplicationsResponse200DataItemTypeKeyType0,
    check_list_tld_applications_response_200_data_item_type_key_type_0,
)
from ..models.list_tld_applications_response_200_data_item_word_popularity_band_type_0 import (
    ListTldApplicationsResponse200DataItemWordPopularityBandType0,
    check_list_tld_applications_response_200_data_item_word_popularity_band_type_0,
)

T = TypeVar("T", bound="ListTldApplicationsResponse200DataItem")


@_attrs_define
class ListTldApplicationsResponse200DataItem:
    """
    Attributes:
        application_id (str): ICANN application id, the row key.
        string (str): Applied-for string, ASCII (A-label for IDNs), lowercased.
        u_label (None | str):
        applicant (str): Applicant as ICANN names it.
        applicant_country_code (None | str):
        type_ (None | str):
        status (None | str):
        contention_set (None | str):
        announced_on (datetime.date | None):
        word_popularity_band (ListTldApplicationsResponse200DataItemWordPopularityBandType0 | None):
        comparable_sales_band (ListTldApplicationsResponse200DataItemComparableSalesBandType0 | None):
        type_key (ListTldApplicationsResponse200DataItemTypeKeyType0 | None):
        status_key (ListTldApplicationsResponse200DataItemStatusKeyType0 | None):
        set_size (int): Applications in the row's contention set; 0 when uncontested.
        applicant_count (int): Applications the same applicant filed in the round.
        in_word_corpus (bool | None):
    """

    application_id: str
    string: str
    u_label: None | str
    applicant: str
    applicant_country_code: None | str
    type_: None | str
    status: None | str
    contention_set: None | str
    announced_on: datetime.date | None
    word_popularity_band: (
        ListTldApplicationsResponse200DataItemWordPopularityBandType0 | None
    )
    comparable_sales_band: (
        ListTldApplicationsResponse200DataItemComparableSalesBandType0 | None
    )
    type_key: ListTldApplicationsResponse200DataItemTypeKeyType0 | None
    status_key: ListTldApplicationsResponse200DataItemStatusKeyType0 | None
    set_size: int
    applicant_count: int
    in_word_corpus: bool | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_id = self.application_id

        string = self.string

        u_label: None | str
        u_label = self.u_label

        applicant = self.applicant

        applicant_country_code: None | str
        applicant_country_code = self.applicant_country_code

        type_: None | str
        type_ = self.type_

        status: None | str
        status = self.status

        contention_set: None | str
        contention_set = self.contention_set

        announced_on: None | str
        if isinstance(self.announced_on, datetime.date):
            announced_on = self.announced_on.isoformat()
        else:
            announced_on = self.announced_on

        word_popularity_band: None | str
        if isinstance(self.word_popularity_band, str):
            word_popularity_band = self.word_popularity_band
        else:
            word_popularity_band = self.word_popularity_band

        comparable_sales_band: None | str
        if isinstance(self.comparable_sales_band, str):
            comparable_sales_band = self.comparable_sales_band
        else:
            comparable_sales_band = self.comparable_sales_band

        type_key: None | str
        if isinstance(self.type_key, str):
            type_key = self.type_key
        else:
            type_key = self.type_key

        status_key: None | str
        if isinstance(self.status_key, str):
            status_key = self.status_key
        else:
            status_key = self.status_key

        set_size = self.set_size

        applicant_count = self.applicant_count

        in_word_corpus: bool | None
        in_word_corpus = self.in_word_corpus

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applicationId": application_id,
                "string": string,
                "uLabel": u_label,
                "applicant": applicant,
                "applicantCountryCode": applicant_country_code,
                "type": type_,
                "status": status,
                "contentionSet": contention_set,
                "announcedOn": announced_on,
                "wordPopularityBand": word_popularity_band,
                "comparableSalesBand": comparable_sales_band,
                "typeKey": type_key,
                "statusKey": status_key,
                "setSize": set_size,
                "applicantCount": applicant_count,
                "inWordCorpus": in_word_corpus,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        application_id = d.pop("applicationId")

        string = d.pop("string")

        def _parse_u_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        u_label = _parse_u_label(d.pop("uLabel"))

        applicant = d.pop("applicant")

        def _parse_applicant_country_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        applicant_country_code = _parse_applicant_country_code(
            d.pop("applicantCountryCode")
        )

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        def _parse_contention_set(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        contention_set = _parse_contention_set(d.pop("contentionSet"))

        def _parse_announced_on(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                announced_on_type_0 = datetime.date.fromisoformat(data)

                return announced_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        announced_on = _parse_announced_on(d.pop("announcedOn"))

        def _parse_word_popularity_band(
            data: object,
        ) -> ListTldApplicationsResponse200DataItemWordPopularityBandType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                word_popularity_band_type_0 = check_list_tld_applications_response_200_data_item_word_popularity_band_type_0(
                    data
                )

                return word_popularity_band_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListTldApplicationsResponse200DataItemWordPopularityBandType0 | None,
                data,
            )

        word_popularity_band = _parse_word_popularity_band(d.pop("wordPopularityBand"))

        def _parse_comparable_sales_band(
            data: object,
        ) -> ListTldApplicationsResponse200DataItemComparableSalesBandType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                comparable_sales_band_type_0 = check_list_tld_applications_response_200_data_item_comparable_sales_band_type_0(
                    data
                )

                return comparable_sales_band_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListTldApplicationsResponse200DataItemComparableSalesBandType0 | None,
                data,
            )

        comparable_sales_band = _parse_comparable_sales_band(
            d.pop("comparableSalesBand")
        )

        def _parse_type_key(
            data: object,
        ) -> ListTldApplicationsResponse200DataItemTypeKeyType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_key_type_0 = (
                    check_list_tld_applications_response_200_data_item_type_key_type_0(
                        data
                    )
                )

                return type_key_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListTldApplicationsResponse200DataItemTypeKeyType0 | None, data)

        type_key = _parse_type_key(d.pop("typeKey"))

        def _parse_status_key(
            data: object,
        ) -> ListTldApplicationsResponse200DataItemStatusKeyType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_key_type_0 = check_list_tld_applications_response_200_data_item_status_key_type_0(
                    data
                )

                return status_key_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListTldApplicationsResponse200DataItemStatusKeyType0 | None, data
            )

        status_key = _parse_status_key(d.pop("statusKey"))

        set_size = d.pop("setSize")

        applicant_count = d.pop("applicantCount")

        def _parse_in_word_corpus(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        in_word_corpus = _parse_in_word_corpus(d.pop("inWordCorpus"))

        list_tld_applications_response_200_data_item = cls(
            application_id=application_id,
            string=string,
            u_label=u_label,
            applicant=applicant,
            applicant_country_code=applicant_country_code,
            type_=type_,
            status=status,
            contention_set=contention_set,
            announced_on=announced_on,
            word_popularity_band=word_popularity_band,
            comparable_sales_band=comparable_sales_band,
            type_key=type_key,
            status_key=status_key,
            set_size=set_size,
            applicant_count=applicant_count,
            in_word_corpus=in_word_corpus,
        )

        list_tld_applications_response_200_data_item.additional_properties = d
        return list_tld_applications_response_200_data_item

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
