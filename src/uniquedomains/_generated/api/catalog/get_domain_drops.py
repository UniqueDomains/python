import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_domain_drops_response_200 import GetDomainDropsResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    day: datetime.date | Unset = UNSET,
    ending: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_day: str | Unset = UNSET
    if not isinstance(day, Unset):
        json_day = day.isoformat()
    params["day"] = json_day

    params["ending"] = ending

    params["limit"] = limit

    params["cursor"] = cursor

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/domains/drops",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetDomainDropsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = GetDomainDropsResponse200.from_dict(response.json())

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
) -> Response[Any | GetDomainDropsResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    day: datetime.date | Unset = UNSET,
    ending: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | GetDomainDropsResponse200 | Problem]:
    """Names dropping on one day: counts free, names keyed.

     Names in pending delete with a verified drop day. Free: the count, the split by ending and the
    ending and day of five names, never a name. Keyed (Investor plan): the names, by name. `day` runs
    from today (UTC) to today plus 6.

    Args:
        day (datetime.date | Unset):
        ending (str | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDomainDropsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        day=day,
        ending=ending,
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
    day: datetime.date | Unset = UNSET,
    ending: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | GetDomainDropsResponse200 | Problem | None:
    """Names dropping on one day: counts free, names keyed.

     Names in pending delete with a verified drop day. Free: the count, the split by ending and the
    ending and day of five names, never a name. Keyed (Investor plan): the names, by name. `day` runs
    from today (UTC) to today plus 6.

    Args:
        day (datetime.date | Unset):
        ending (str | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDomainDropsResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        day=day,
        ending=ending,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    day: datetime.date | Unset = UNSET,
    ending: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | GetDomainDropsResponse200 | Problem]:
    """Names dropping on one day: counts free, names keyed.

     Names in pending delete with a verified drop day. Free: the count, the split by ending and the
    ending and day of five names, never a name. Keyed (Investor plan): the names, by name. `day` runs
    from today (UTC) to today plus 6.

    Args:
        day (datetime.date | Unset):
        ending (str | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDomainDropsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        day=day,
        ending=ending,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    day: datetime.date | Unset = UNSET,
    ending: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | GetDomainDropsResponse200 | Problem | None:
    """Names dropping on one day: counts free, names keyed.

     Names in pending delete with a verified drop day. Free: the count, the split by ending and the
    ending and day of five names, never a name. Keyed (Investor plan): the names, by name. `day` runs
    from today (UTC) to today plus 6.

    Args:
        day (datetime.date | Unset):
        ending (str | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDomainDropsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            day=day,
            ending=ending,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
