from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_key_response_200_data_access import (
    GetKeyResponse200DataAccess,
    check_get_key_response_200_data_access,
)
from ..models.get_key_response_200_data_listing_type_1 import (
    GetKeyResponse200DataListingType1,
    check_get_key_response_200_data_listing_type_1,
)
from ..models.get_key_response_200_data_listing_type_2_type_1 import (
    GetKeyResponse200DataListingType2Type1,
    check_get_key_response_200_data_listing_type_2_type_1,
)
from ..models.get_key_response_200_data_listing_type_3_type_1 import (
    GetKeyResponse200DataListingType3Type1,
    check_get_key_response_200_data_listing_type_3_type_1,
)
from ..models.get_key_response_200_data_plan_type_1 import (
    GetKeyResponse200DataPlanType1,
    check_get_key_response_200_data_plan_type_1,
)
from ..models.get_key_response_200_data_plan_type_2_type_1 import (
    GetKeyResponse200DataPlanType2Type1,
    check_get_key_response_200_data_plan_type_2_type_1,
)
from ..models.get_key_response_200_data_plan_type_3_type_1 import (
    GetKeyResponse200DataPlanType3Type1,
    check_get_key_response_200_data_plan_type_3_type_1,
)
from ..models.get_key_response_200_data_subscription_type_1 import (
    GetKeyResponse200DataSubscriptionType1,
    check_get_key_response_200_data_subscription_type_1,
)
from ..models.get_key_response_200_data_subscription_type_2_type_1 import (
    GetKeyResponse200DataSubscriptionType2Type1,
    check_get_key_response_200_data_subscription_type_2_type_1,
)
from ..models.get_key_response_200_data_subscription_type_3_type_1 import (
    GetKeyResponse200DataSubscriptionType3Type1,
    check_get_key_response_200_data_subscription_type_3_type_1,
)

if TYPE_CHECKING:
    from ..models.get_key_response_200_data_appraisals_type_0 import (
        GetKeyResponse200DataAppraisalsType0,
    )
    from ..models.get_key_response_200_data_calls_type_0 import (
        GetKeyResponse200DataCallsType0,
    )
    from ..models.get_key_response_200_data_intakes_type_0 import (
        GetKeyResponse200DataIntakesType0,
    )
    from ..models.get_key_response_200_data_live_checks_type_0 import (
        GetKeyResponse200DataLiveChecksType0,
    )


T = TypeVar("T", bound="GetKeyResponse200Data")


@_attrs_define
class GetKeyResponse200Data:
    """
    Attributes:
        access (GetKeyResponse200DataAccess):
        plan (GetKeyResponse200DataPlanType1 | GetKeyResponse200DataPlanType2Type1 | GetKeyResponse200DataPlanType3Type1
            | None):
        key_prefix (None | str):
        listing (GetKeyResponse200DataListingType1 | GetKeyResponse200DataListingType2Type1 |
            GetKeyResponse200DataListingType3Type1 | None):
        subscription (GetKeyResponse200DataSubscriptionType1 | GetKeyResponse200DataSubscriptionType2Type1 |
            GetKeyResponse200DataSubscriptionType3Type1 | None):
        month (None | str):
        resets_on (datetime.date | None):
        calls (GetKeyResponse200DataCallsType0 | None):
        live_checks (GetKeyResponse200DataLiveChecksType0 | None):
        appraisals (GetKeyResponse200DataAppraisalsType0 | None):
        intakes (GetKeyResponse200DataIntakesType0 | None):
        investor_endpoints (bool | None):
    """

    access: GetKeyResponse200DataAccess
    plan: (
        GetKeyResponse200DataPlanType1
        | GetKeyResponse200DataPlanType2Type1
        | GetKeyResponse200DataPlanType3Type1
        | None
    )
    key_prefix: None | str
    listing: (
        GetKeyResponse200DataListingType1
        | GetKeyResponse200DataListingType2Type1
        | GetKeyResponse200DataListingType3Type1
        | None
    )
    subscription: (
        GetKeyResponse200DataSubscriptionType1
        | GetKeyResponse200DataSubscriptionType2Type1
        | GetKeyResponse200DataSubscriptionType3Type1
        | None
    )
    month: None | str
    resets_on: datetime.date | None
    calls: GetKeyResponse200DataCallsType0 | None
    live_checks: GetKeyResponse200DataLiveChecksType0 | None
    appraisals: GetKeyResponse200DataAppraisalsType0 | None
    intakes: GetKeyResponse200DataIntakesType0 | None
    investor_endpoints: bool | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_key_response_200_data_appraisals_type_0 import (
            GetKeyResponse200DataAppraisalsType0,
        )
        from ..models.get_key_response_200_data_calls_type_0 import (
            GetKeyResponse200DataCallsType0,
        )
        from ..models.get_key_response_200_data_intakes_type_0 import (
            GetKeyResponse200DataIntakesType0,
        )
        from ..models.get_key_response_200_data_live_checks_type_0 import (
            GetKeyResponse200DataLiveChecksType0,
        )

        access: str = self.access

        plan: None | str
        if (
            isinstance(self.plan, str)
            or isinstance(self.plan, str)
            or isinstance(self.plan, str)
        ):
            plan = self.plan
        else:
            plan = self.plan

        key_prefix: None | str
        key_prefix = self.key_prefix

        listing: None | str
        if (
            isinstance(self.listing, str)
            or isinstance(self.listing, str)
            or isinstance(self.listing, str)
        ):
            listing = self.listing
        else:
            listing = self.listing

        subscription: None | str
        if (
            isinstance(self.subscription, str)
            or isinstance(self.subscription, str)
            or isinstance(self.subscription, str)
        ):
            subscription = self.subscription
        else:
            subscription = self.subscription

        month: None | str
        month = self.month

        resets_on: None | str
        if isinstance(self.resets_on, datetime.date):
            resets_on = self.resets_on.isoformat()
        else:
            resets_on = self.resets_on

        calls: dict[str, Any] | None
        if isinstance(self.calls, GetKeyResponse200DataCallsType0):
            calls = self.calls.to_dict()
        else:
            calls = self.calls

        live_checks: dict[str, Any] | None
        if isinstance(self.live_checks, GetKeyResponse200DataLiveChecksType0):
            live_checks = self.live_checks.to_dict()
        else:
            live_checks = self.live_checks

        appraisals: dict[str, Any] | None
        if isinstance(self.appraisals, GetKeyResponse200DataAppraisalsType0):
            appraisals = self.appraisals.to_dict()
        else:
            appraisals = self.appraisals

        intakes: dict[str, Any] | None
        if isinstance(self.intakes, GetKeyResponse200DataIntakesType0):
            intakes = self.intakes.to_dict()
        else:
            intakes = self.intakes

        investor_endpoints: bool | None
        investor_endpoints = self.investor_endpoints

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access": access,
                "plan": plan,
                "keyPrefix": key_prefix,
                "listing": listing,
                "subscription": subscription,
                "month": month,
                "resetsOn": resets_on,
                "calls": calls,
                "liveChecks": live_checks,
                "appraisals": appraisals,
                "intakes": intakes,
                "investorEndpoints": investor_endpoints,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_key_response_200_data_appraisals_type_0 import (
            GetKeyResponse200DataAppraisalsType0,
        )
        from ..models.get_key_response_200_data_calls_type_0 import (
            GetKeyResponse200DataCallsType0,
        )
        from ..models.get_key_response_200_data_intakes_type_0 import (
            GetKeyResponse200DataIntakesType0,
        )
        from ..models.get_key_response_200_data_live_checks_type_0 import (
            GetKeyResponse200DataLiveChecksType0,
        )

        d = dict(src_dict)
        access = check_get_key_response_200_data_access(d.pop("access"))

        def _parse_plan(
            data: object,
        ) -> (
            GetKeyResponse200DataPlanType1
            | GetKeyResponse200DataPlanType2Type1
            | GetKeyResponse200DataPlanType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                plan_type_1 = check_get_key_response_200_data_plan_type_1(data)

                return plan_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                plan_type_2_type_1 = check_get_key_response_200_data_plan_type_2_type_1(
                    data
                )

                return plan_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                plan_type_3_type_1 = check_get_key_response_200_data_plan_type_3_type_1(
                    data
                )

                return plan_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetKeyResponse200DataPlanType1
                | GetKeyResponse200DataPlanType2Type1
                | GetKeyResponse200DataPlanType3Type1
                | None,
                data,
            )

        plan = _parse_plan(d.pop("plan"))

        def _parse_key_prefix(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        key_prefix = _parse_key_prefix(d.pop("keyPrefix"))

        def _parse_listing(
            data: object,
        ) -> (
            GetKeyResponse200DataListingType1
            | GetKeyResponse200DataListingType2Type1
            | GetKeyResponse200DataListingType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                listing_type_1 = check_get_key_response_200_data_listing_type_1(data)

                return listing_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                listing_type_2_type_1 = (
                    check_get_key_response_200_data_listing_type_2_type_1(data)
                )

                return listing_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                listing_type_3_type_1 = (
                    check_get_key_response_200_data_listing_type_3_type_1(data)
                )

                return listing_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetKeyResponse200DataListingType1
                | GetKeyResponse200DataListingType2Type1
                | GetKeyResponse200DataListingType3Type1
                | None,
                data,
            )

        listing = _parse_listing(d.pop("listing"))

        def _parse_subscription(
            data: object,
        ) -> (
            GetKeyResponse200DataSubscriptionType1
            | GetKeyResponse200DataSubscriptionType2Type1
            | GetKeyResponse200DataSubscriptionType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_type_1 = (
                    check_get_key_response_200_data_subscription_type_1(data)
                )

                return subscription_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_type_2_type_1 = (
                    check_get_key_response_200_data_subscription_type_2_type_1(data)
                )

                return subscription_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_type_3_type_1 = (
                    check_get_key_response_200_data_subscription_type_3_type_1(data)
                )

                return subscription_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetKeyResponse200DataSubscriptionType1
                | GetKeyResponse200DataSubscriptionType2Type1
                | GetKeyResponse200DataSubscriptionType3Type1
                | None,
                data,
            )

        subscription = _parse_subscription(d.pop("subscription"))

        def _parse_month(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        month = _parse_month(d.pop("month"))

        def _parse_resets_on(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resets_on_type_0 = datetime.date.fromisoformat(data)

                return resets_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        resets_on = _parse_resets_on(d.pop("resetsOn"))

        def _parse_calls(data: object) -> GetKeyResponse200DataCallsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                calls_type_0 = GetKeyResponse200DataCallsType0.from_dict(data)

                return calls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetKeyResponse200DataCallsType0 | None, data)

        calls = _parse_calls(d.pop("calls"))

        def _parse_live_checks(
            data: object,
        ) -> GetKeyResponse200DataLiveChecksType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                live_checks_type_0 = GetKeyResponse200DataLiveChecksType0.from_dict(
                    data
                )

                return live_checks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetKeyResponse200DataLiveChecksType0 | None, data)

        live_checks = _parse_live_checks(d.pop("liveChecks"))

        def _parse_appraisals(
            data: object,
        ) -> GetKeyResponse200DataAppraisalsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                appraisals_type_0 = GetKeyResponse200DataAppraisalsType0.from_dict(data)

                return appraisals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetKeyResponse200DataAppraisalsType0 | None, data)

        appraisals = _parse_appraisals(d.pop("appraisals"))

        def _parse_intakes(data: object) -> GetKeyResponse200DataIntakesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                intakes_type_0 = GetKeyResponse200DataIntakesType0.from_dict(data)

                return intakes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetKeyResponse200DataIntakesType0 | None, data)

        intakes = _parse_intakes(d.pop("intakes"))

        def _parse_investor_endpoints(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        investor_endpoints = _parse_investor_endpoints(d.pop("investorEndpoints"))

        get_key_response_200_data = cls(
            access=access,
            plan=plan,
            key_prefix=key_prefix,
            listing=listing,
            subscription=subscription,
            month=month,
            resets_on=resets_on,
            calls=calls,
            live_checks=live_checks,
            appraisals=appraisals,
            intakes=intakes,
            investor_endpoints=investor_endpoints,
        )

        get_key_response_200_data.additional_properties = d
        return get_key_response_200_data

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
