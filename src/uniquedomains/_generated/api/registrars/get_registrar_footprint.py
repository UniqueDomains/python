from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_registrar_footprint_registrar import (
    GetRegistrarFootprintRegistrar,
)
from ...models.get_registrar_footprint_response_200 import (
    GetRegistrarFootprintResponse200,
)
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    registrar: GetRegistrarFootprintRegistrar,
    *,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/registrars/{registrar}/footprint".format(
            registrar=quote(str(registrar), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetRegistrarFootprintResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = GetRegistrarFootprintResponse200.from_dict(response.json())

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
) -> Response[Any | GetRegistrarFootprintResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    registrar: GetRegistrarFootprintRegistrar,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> Response[Any | GetRegistrarFootprintResponse200 | Problem]:
    """Names tracked under the registrar on the latest footprint day, rounded, with its top endings.

     From the scanner's footprint figures, keyed by IANA id; 404 for a registrar with no IANA id or no
    row.

    Args:
        registrar (GetRegistrarFootprintRegistrar):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetRegistrarFootprintResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        registrar=registrar,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    registrar: GetRegistrarFootprintRegistrar,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> Any | GetRegistrarFootprintResponse200 | Problem | None:
    """Names tracked under the registrar on the latest footprint day, rounded, with its top endings.

     From the scanner's footprint figures, keyed by IANA id; 404 for a registrar with no IANA id or no
    row.

    Args:
        registrar (GetRegistrarFootprintRegistrar):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetRegistrarFootprintResponse200 | Problem
    """

    return sync_detailed(
        registrar=registrar,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    registrar: GetRegistrarFootprintRegistrar,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> Response[Any | GetRegistrarFootprintResponse200 | Problem]:
    """Names tracked under the registrar on the latest footprint day, rounded, with its top endings.

     From the scanner's footprint figures, keyed by IANA id; 404 for a registrar with no IANA id or no
    row.

    Args:
        registrar (GetRegistrarFootprintRegistrar):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetRegistrarFootprintResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        registrar=registrar,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    registrar: GetRegistrarFootprintRegistrar,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> Any | GetRegistrarFootprintResponse200 | Problem | None:
    """Names tracked under the registrar on the latest footprint day, rounded, with its top endings.

     From the scanner's footprint figures, keyed by IANA id; 404 for a registrar with no IANA id or no
    row.

    Args:
        registrar (GetRegistrarFootprintRegistrar):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetRegistrarFootprintResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            registrar=registrar,
            client=client,
            fields=fields,
        )
    ).parsed
