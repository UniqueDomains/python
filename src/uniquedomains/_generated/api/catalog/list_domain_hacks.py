import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_domain_hacks_response_200 import ListDomainHacksResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ending: str | Unset = UNSET,
    status: str | Unset = UNSET,
    length_min: int | Unset = UNSET,
    length_max: int | Unset = UNSET,
    shape: str | Unset = UNSET,
    style: str | Unset = UNSET,
    price_max: float | Unset = UNSET,
    renewal_max: float | Unset = UNSET,
    prefix: str | Unset = UNSET,
    contains: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    expires_before: datetime.date | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ending"] = ending

    params["status"] = status

    params["lengthMin"] = length_min

    params["lengthMax"] = length_max

    params["shape"] = shape

    params["style"] = style

    params["priceMax"] = price_max

    params["renewalMax"] = renewal_max

    params["prefix"] = prefix

    params["contains"] = contains

    params["pos"] = pos

    json_expires_before: str | Unset = UNSET
    if not isinstance(expires_before, Unset):
        json_expires_before = expires_before.isoformat()
    params["expiresBefore"] = json_expires_before

    params["sort"] = sort

    params["limit"] = limit

    params["cursor"] = cursor

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/domains/hacks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ListDomainHacksResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListDomainHacksResponse200.from_dict(response.json())

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
) -> Response[Any | ListDomainHacksResponse200 | Problem]:
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
    status: str | Unset = UNSET,
    length_min: int | Unset = UNSET,
    length_max: int | Unset = UNSET,
    shape: str | Unset = UNSET,
    style: str | Unset = UNSET,
    price_max: float | Unset = UNSET,
    renewal_max: float | Unset = UNSET,
    prefix: str | Unset = UNSET,
    contains: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    expires_before: datetime.date | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | ListDomainHacksResponse200 | Problem]:
    """Domain hacks: names whose ending completes the word.

     The domain hacks list. Free: the public hacks list, at most 20 rows, one page. Keyed: pages in a
    neutral column order with `sort`, else in the engine's own order.

    Args:
        ending (str | Unset):
        status (str | Unset):
        length_min (int | Unset):
        length_max (int | Unset):
        shape (str | Unset):
        style (str | Unset):
        price_max (float | Unset):
        renewal_max (float | Unset):
        prefix (str | Unset):
        contains (str | Unset):
        pos (str | Unset):
        expires_before (datetime.date | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListDomainHacksResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        ending=ending,
        status=status,
        length_min=length_min,
        length_max=length_max,
        shape=shape,
        style=style,
        price_max=price_max,
        renewal_max=renewal_max,
        prefix=prefix,
        contains=contains,
        pos=pos,
        expires_before=expires_before,
        sort=sort,
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
    status: str | Unset = UNSET,
    length_min: int | Unset = UNSET,
    length_max: int | Unset = UNSET,
    shape: str | Unset = UNSET,
    style: str | Unset = UNSET,
    price_max: float | Unset = UNSET,
    renewal_max: float | Unset = UNSET,
    prefix: str | Unset = UNSET,
    contains: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    expires_before: datetime.date | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | ListDomainHacksResponse200 | Problem | None:
    """Domain hacks: names whose ending completes the word.

     The domain hacks list. Free: the public hacks list, at most 20 rows, one page. Keyed: pages in a
    neutral column order with `sort`, else in the engine's own order.

    Args:
        ending (str | Unset):
        status (str | Unset):
        length_min (int | Unset):
        length_max (int | Unset):
        shape (str | Unset):
        style (str | Unset):
        price_max (float | Unset):
        renewal_max (float | Unset):
        prefix (str | Unset):
        contains (str | Unset):
        pos (str | Unset):
        expires_before (datetime.date | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListDomainHacksResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        ending=ending,
        status=status,
        length_min=length_min,
        length_max=length_max,
        shape=shape,
        style=style,
        price_max=price_max,
        renewal_max=renewal_max,
        prefix=prefix,
        contains=contains,
        pos=pos,
        expires_before=expires_before,
        sort=sort,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ending: str | Unset = UNSET,
    status: str | Unset = UNSET,
    length_min: int | Unset = UNSET,
    length_max: int | Unset = UNSET,
    shape: str | Unset = UNSET,
    style: str | Unset = UNSET,
    price_max: float | Unset = UNSET,
    renewal_max: float | Unset = UNSET,
    prefix: str | Unset = UNSET,
    contains: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    expires_before: datetime.date | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | ListDomainHacksResponse200 | Problem]:
    """Domain hacks: names whose ending completes the word.

     The domain hacks list. Free: the public hacks list, at most 20 rows, one page. Keyed: pages in a
    neutral column order with `sort`, else in the engine's own order.

    Args:
        ending (str | Unset):
        status (str | Unset):
        length_min (int | Unset):
        length_max (int | Unset):
        shape (str | Unset):
        style (str | Unset):
        price_max (float | Unset):
        renewal_max (float | Unset):
        prefix (str | Unset):
        contains (str | Unset):
        pos (str | Unset):
        expires_before (datetime.date | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListDomainHacksResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        ending=ending,
        status=status,
        length_min=length_min,
        length_max=length_max,
        shape=shape,
        style=style,
        price_max=price_max,
        renewal_max=renewal_max,
        prefix=prefix,
        contains=contains,
        pos=pos,
        expires_before=expires_before,
        sort=sort,
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
    status: str | Unset = UNSET,
    length_min: int | Unset = UNSET,
    length_max: int | Unset = UNSET,
    shape: str | Unset = UNSET,
    style: str | Unset = UNSET,
    price_max: float | Unset = UNSET,
    renewal_max: float | Unset = UNSET,
    prefix: str | Unset = UNSET,
    contains: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    expires_before: datetime.date | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | ListDomainHacksResponse200 | Problem | None:
    """Domain hacks: names whose ending completes the word.

     The domain hacks list. Free: the public hacks list, at most 20 rows, one page. Keyed: pages in a
    neutral column order with `sort`, else in the engine's own order.

    Args:
        ending (str | Unset):
        status (str | Unset):
        length_min (int | Unset):
        length_max (int | Unset):
        shape (str | Unset):
        style (str | Unset):
        price_max (float | Unset):
        renewal_max (float | Unset):
        prefix (str | Unset):
        contains (str | Unset):
        pos (str | Unset):
        expires_before (datetime.date | Unset):
        sort (str | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListDomainHacksResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            ending=ending,
            status=status,
            length_min=length_min,
            length_max=length_max,
            shape=shape,
            style=style,
            price_max=price_max,
            renewal_max=renewal_max,
            prefix=prefix,
            contains=contains,
            pos=pos,
            expires_before=expires_before,
            sort=sort,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
