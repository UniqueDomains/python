from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_agenda_category import GetAgendaCategory
from ...models.get_agenda_response_200 import GetAgendaResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    month: str | Unset = UNSET,
    category: GetAgendaCategory | Unset = UNSET,
    country: str | Unset = UNSET,
    tld: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["month"] = month

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category

    params["category"] = json_category

    params["country"] = country

    params["tld"] = tld

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/agenda",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAgendaResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = GetAgendaResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Problem.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = Problem.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetAgendaResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    month: str | Unset = UNSET,
    category: GetAgendaCategory | Unset = UNSET,
    country: str | Unset = UNSET,
    tld: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | GetAgendaResponse200 | Problem]:
    """The whole public agenda of one month: industry events, TLD launch phases and registry changes.

     The dated entries overlapping the month in date order, the registry announcements of the last 30
    days without a day of their own (newest first), and the events without a date. Served whole (no
    cursor).

    Args:
        month (str | Unset):
        category (GetAgendaCategory | Unset):
        country (str | Unset):
        tld (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAgendaResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        month=month,
        category=category,
        country=country,
        tld=tld,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    month: str | Unset = UNSET,
    category: GetAgendaCategory | Unset = UNSET,
    country: str | Unset = UNSET,
    tld: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | GetAgendaResponse200 | Problem | None:
    """The whole public agenda of one month: industry events, TLD launch phases and registry changes.

     The dated entries overlapping the month in date order, the registry announcements of the last 30
    days without a day of their own (newest first), and the events without a date. Served whole (no
    cursor).

    Args:
        month (str | Unset):
        category (GetAgendaCategory | Unset):
        country (str | Unset):
        tld (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAgendaResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        month=month,
        category=category,
        country=country,
        tld=tld,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    month: str | Unset = UNSET,
    category: GetAgendaCategory | Unset = UNSET,
    country: str | Unset = UNSET,
    tld: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | GetAgendaResponse200 | Problem]:
    """The whole public agenda of one month: industry events, TLD launch phases and registry changes.

     The dated entries overlapping the month in date order, the registry announcements of the last 30
    days without a day of their own (newest first), and the events without a date. Served whole (no
    cursor).

    Args:
        month (str | Unset):
        category (GetAgendaCategory | Unset):
        country (str | Unset):
        tld (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAgendaResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        month=month,
        category=category,
        country=country,
        tld=tld,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    month: str | Unset = UNSET,
    category: GetAgendaCategory | Unset = UNSET,
    country: str | Unset = UNSET,
    tld: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | GetAgendaResponse200 | Problem | None:
    """The whole public agenda of one month: industry events, TLD launch phases and registry changes.

     The dated entries overlapping the month in date order, the registry announcements of the last 30
    days without a day of their own (newest first), and the events without a date. Served whole (no
    cursor).

    Args:
        month (str | Unset):
        category (GetAgendaCategory | Unset):
        country (str | Unset):
        tld (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAgendaResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            month=month,
            category=category,
            country=country,
            tld=tld,
            fields=fields,
        )
    ).parsed
