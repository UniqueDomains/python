from typing import Literal

ProblemCode = Literal[
    "brand",
    "budget_spent",
    "check_unavailable",
    "consumer_day_cap",
    "cursor_invalid",
    "disabled_in_catalog",
    "gate_unavailable",
    "intake_day_cap",
    "internal",
    "invalid_key",
    "invalid_proxy_secret",
    "invalid_word",
    "keyed_only",
    "listing_mismatch",
    "not_a_word",
    "not_found",
    "not_ready",
    "offensive",
    "plan_required",
    "quota_spent",
    "rate_limited",
    "unsupported_field",
    "unsupported_format",
    "validation_failed",
]

PROBLEM_CODE_VALUES: set[ProblemCode] = {
    "brand",
    "budget_spent",
    "check_unavailable",
    "consumer_day_cap",
    "cursor_invalid",
    "disabled_in_catalog",
    "gate_unavailable",
    "intake_day_cap",
    "internal",
    "invalid_key",
    "invalid_proxy_secret",
    "invalid_word",
    "keyed_only",
    "listing_mismatch",
    "not_a_word",
    "not_found",
    "not_ready",
    "offensive",
    "plan_required",
    "quota_spent",
    "rate_limited",
    "unsupported_field",
    "unsupported_format",
    "validation_failed",
}


def check_problem_code(value: str) -> ProblemCode:
    if value in PROBLEM_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROBLEM_CODE_VALUES!r}"
    )
