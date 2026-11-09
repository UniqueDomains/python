import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_expiring_domains_response_200 import ListExpiringDomainsResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ending: str | Unset = UNSET,
    after: datetime.date | Unset = UNSET,
    before: datetime.date | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ending"] = ending

    json_after: str | Unset = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    json_before: str | Unset = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    params["limit"] = limit

    params["cursor"] = cursor

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/domains/expiring",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ListExpiringDomainsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListExpiringDomainsResponse200.from_dict(response.json())

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
) -> Response[Any | ListExpiringDomainsResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ending: str | Unset = UNSET,
    after: datetime.date | Unset = UNSET,
    before: datetime.date | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | ListExpiringDomainsResponse200 | Problem]:
    """Catalog names expiring or expired, by expiry day.

     Names in `expiring` or `expired` status, ascending by registry expiry, with the verified drop day
    when one is due.

    Args:
        ending (str | Unset):
        after (datetime.date | Unset):
        before (datetime.date | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListExpiringDomainsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        ending=ending,
        after=after,
        before=before,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ending: str | Unset = UNSET,
    after: datetime.date | Unset = UNSET,
    before: datetime.date | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | ListExpiringDomainsResponse200 | Problem | None:
    """Catalog names expiring or expired, by expiry day.

     Names in `expiring` or `expired` status, ascending by registry expiry, with the verified drop day
    when one is due.

    Args:
        ending (str | Unset):
        after (datetime.date | Unset):
        before (datetime.date | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListExpiringDomainsResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        ending=ending,
        after=after,
        before=before,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ending: str | Unset = UNSET,
    after: datetime.date | Unset = UNSET,
    before: datetime.date | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | ListExpiringDomainsResponse200 | Problem]:
    """Catalog names expiring or expired, by expiry day.

     Names in `expiring` or `expired` status, ascending by registry expiry, with the verified drop day
    when one is due.

    Args:
        ending (str | Unset):
        after (datetime.date | Unset):
        before (datetime.date | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListExpiringDomainsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        ending=ending,
        after=after,
        before=before,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ending: str | Unset = UNSET,
    after: datetime.date | Unset = UNSET,
    before: datetime.date | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | ListExpiringDomainsResponse200 | Problem | None:
    """Catalog names expiring or expired, by expiry day.

     Names in `expiring` or `expired` status, ascending by registry expiry, with the verified drop day
    when one is due.

    Args:
        ending (str | Unset):
        after (datetime.date | Unset):
        before (datetime.date | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListExpiringDomainsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            ending=ending,
            after=after,
            before=before,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
