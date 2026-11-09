from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tld_response_200 import GetTldResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tld: str,
    *,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tlds/{tld}".format(
            tld=quote(str(tld), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetTldResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = GetTldResponse200.from_dict(response.json())

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
) -> Response[Any | GetTldResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tld: str,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> Response[Any | GetTldResponse200 | Problem]:
    """One TLD in full: registry facts, phases, market, quality band and registrar prices.

     A public-set TLD with its figures computed carries the website insight bundle without its name
    sample, news, description words and topics. Any other TLD answers its registry facts and phases, and
    its market on a paid subscription. A removed or terminated TLD is 404.

    Args:
        tld (str):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTldResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        tld=tld,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tld: str,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> Any | GetTldResponse200 | Problem | None:
    """One TLD in full: registry facts, phases, market, quality band and registrar prices.

     A public-set TLD with its figures computed carries the website insight bundle without its name
    sample, news, description words and topics. Any other TLD answers its registry facts and phases, and
    its market on a paid subscription. A removed or terminated TLD is 404.

    Args:
        tld (str):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTldResponse200 | Problem
    """

    return sync_detailed(
        tld=tld,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    tld: str,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> Response[Any | GetTldResponse200 | Problem]:
    """One TLD in full: registry facts, phases, market, quality band and registrar prices.

     A public-set TLD with its figures computed carries the website insight bundle without its name
    sample, news, description words and topics. Any other TLD answers its registry facts and phases, and
    its market on a paid subscription. A removed or terminated TLD is 404.

    Args:
        tld (str):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTldResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        tld=tld,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tld: str,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> Any | GetTldResponse200 | Problem | None:
    """One TLD in full: registry facts, phases, market, quality band and registrar prices.

     A public-set TLD with its figures computed carries the website insight bundle without its name
    sample, news, description words and topics. Any other TLD answers its registry facts and phases, and
    its market on a paid subscription. A removed or terminated TLD is 404.

    Args:
        tld (str):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTldResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            tld=tld,
            client=client,
            fields=fields,
        )
    ).parsed
