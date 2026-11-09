"""The Python client for the Unique Domains API: domain names, words, TLDs, registrar prices, the domain market,
trends and the agenda (https://unique.domains/api).

    from uniquedomains import Client

    ud = Client()  # free and keyless; a member key from UD_API_KEY when set
    answer = ud.names.get_name("get.plumbing")
    print(answer.data.status, answer.rate_limit)
"""

from ._answer import Answer, TextAnswer
from ._client import Client, RapidApi, find_listing, listings_serving
from ._errors import (
    AnswerShapeError,
    ApiProblemError,
    AuthError,
    ListingMismatchError,
    NotFoundError,
    NotReadyError,
    PlanRequiredError,
    QuotaError,
    RateLimitError,
    UniqueDomainsError,
    ValidationError,
    WordRejectedError,
)
from ._headers import Quota, QuotaUnit, RateLimit
from ._listings import LISTINGS
from ._operations import API_DOCUMENT_VERSION, API_PUBLIC_BASE, OPERATIONS
from ._retry import Retry
from ._version import __version__

__all__ = [
    "API_DOCUMENT_VERSION",
    "API_PUBLIC_BASE",
    "LISTINGS",
    "OPERATIONS",
    "Answer",
    "AnswerShapeError",
    "ApiProblemError",
    "AuthError",
    "Client",
    "ListingMismatchError",
    "NotFoundError",
    "NotReadyError",
    "PlanRequiredError",
    "Quota",
    "QuotaError",
    "QuotaUnit",
    "RapidApi",
    "RateLimit",
    "RateLimitError",
    "Retry",
    "TextAnswer",
    "UniqueDomainsError",
    "ValidationError",
    "WordRejectedError",
    "__version__",
    "find_listing",
    "listings_serving",
]
