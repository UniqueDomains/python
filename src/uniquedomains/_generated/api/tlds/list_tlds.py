from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_tlds_iana_status import (
    ListTldsIanaStatus,
)
from ...models.list_tlds_response_200 import ListTldsResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    iana_type: str | Unset = UNSET,
    iana_status: ListTldsIanaStatus | Unset = UNSET,
    country: str | Unset = UNSET,
    is_brand: bool | Unset = UNSET,
    is_idn: bool | Unset = UNSET,
    public_set: bool | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ianaType"] = iana_type

    json_iana_status: str | Unset = UNSET
    if not isinstance(iana_status, Unset):
        json_iana_status = iana_status

    params["ianaStatus"] = json_iana_status

    params["country"] = country

    params["isBrand"] = is_brand

    params["isIdn"] = is_idn

    params["publicSet"] = public_set

    params["limit"] = limit

    params["cursor"] = cursor

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tlds",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ListTldsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListTldsResponse200.from_dict(response.json())

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
) -> Response[Any | ListTldsResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    iana_type: str | Unset = UNSET,
    iana_status: ListTldsIanaStatus | Unset = UNSET,
    country: str | Unset = UNSET,
    is_brand: bool | Unset = UNSET,
    is_idn: bool | Unset = UNSET,
    public_set: bool | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | ListTldsResponse200 | Problem]:
    """Every root TLD with its registry facts and launch phases, alphabetical.

     Root TLDs only, sorted by slug. A public-set row carries `insights`: the website page and its
    12-month market aggregates.

    Args:
        iana_type (str | Unset):
        iana_status (ListTldsIanaStatus | Unset):
        country (str | Unset):
        is_brand (bool | Unset):
        is_idn (bool | Unset):
        public_set (bool | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListTldsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        iana_type=iana_type,
        iana_status=iana_status,
        country=country,
        is_brand=is_brand,
        is_idn=is_idn,
        public_set=public_set,
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
    iana_type: str | Unset = UNSET,
    iana_status: ListTldsIanaStatus | Unset = UNSET,
    country: str | Unset = UNSET,
    is_brand: bool | Unset = UNSET,
    is_idn: bool | Unset = UNSET,
    public_set: bool | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | ListTldsResponse200 | Problem | None:
    """Every root TLD with its registry facts and launch phases, alphabetical.

     Root TLDs only, sorted by slug. A public-set row carries `insights`: the website page and its
    12-month market aggregates.

    Args:
        iana_type (str | Unset):
        iana_status (ListTldsIanaStatus | Unset):
        country (str | Unset):
        is_brand (bool | Unset):
        is_idn (bool | Unset):
        public_set (bool | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListTldsResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        iana_type=iana_type,
        iana_status=iana_status,
        country=country,
        is_brand=is_brand,
        is_idn=is_idn,
        public_set=public_set,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    iana_type: str | Unset = UNSET,
    iana_status: ListTldsIanaStatus | Unset = UNSET,
    country: str | Unset = UNSET,
    is_brand: bool | Unset = UNSET,
    is_idn: bool | Unset = UNSET,
    public_set: bool | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | ListTldsResponse200 | Problem]:
    """Every root TLD with its registry facts and launch phases, alphabetical.

     Root TLDs only, sorted by slug. A public-set row carries `insights`: the website page and its
    12-month market aggregates.

    Args:
        iana_type (str | Unset):
        iana_status (ListTldsIanaStatus | Unset):
        country (str | Unset):
        is_brand (bool | Unset):
        is_idn (bool | Unset):
        public_set (bool | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListTldsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        iana_type=iana_type,
        iana_status=iana_status,
        country=country,
        is_brand=is_brand,
        is_idn=is_idn,
        public_set=public_set,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    iana_type: str | Unset = UNSET,
    iana_status: ListTldsIanaStatus | Unset = UNSET,
    country: str | Unset = UNSET,
    is_brand: bool | Unset = UNSET,
    is_idn: bool | Unset = UNSET,
    public_set: bool | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | ListTldsResponse200 | Problem | None:
    """Every root TLD with its registry facts and launch phases, alphabetical.

     Root TLDs only, sorted by slug. A public-set row carries `insights`: the website page and its
    12-month market aggregates.

    Args:
        iana_type (str | Unset):
        iana_status (ListTldsIanaStatus | Unset):
        country (str | Unset):
        is_brand (bool | Unset):
        is_idn (bool | Unset):
        public_set (bool | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListTldsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            iana_type=iana_type,
            iana_status=iana_status,
            country=country,
            is_brand=is_brand,
            is_idn=is_idn,
            public_set=public_set,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
