from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_openapi_listing import GetOpenapiListing
from ...models.get_openapi_oas import GetOpenapiOas
from ...models.get_openapi_response_200 import GetOpenapiResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    listing: GetOpenapiListing | Unset = UNSET,
    oas: GetOpenapiOas | Unset = "3.1",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_listing: str | Unset = UNSET
    if not isinstance(listing, Unset):
        json_listing = listing

    params["listing"] = json_listing

    json_oas: str | Unset = UNSET
    if not isinstance(oas, Unset):
        json_oas = oas

    params["oas"] = json_oas

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/meta/openapi.json",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetOpenapiResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = GetOpenapiResponse200.from_dict(response.json())

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
) -> Response[Any | GetOpenapiResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    listing: GetOpenapiListing | Unset = UNSET,
    oas: GetOpenapiOas | Unset = "3.1",
) -> Response[Any | GetOpenapiResponse200 | Problem]:
    """The OpenAPI document of the API, whole or for one listing, in its 3.1 or 3.0 form.

     Built from the typed endpoint catalog, served bare (no envelope). Each RapidAPI listing imports its
    own document with `listing`, in the 3.0 form (`oas=3.0`), the one RapidAPI's import accepts. Not
    counted against the free tier's per-address limits.

    Args:
        listing (GetOpenapiListing | Unset):
        oas (GetOpenapiOas | Unset):  Default: '3.1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetOpenapiResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        listing=listing,
        oas=oas,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    listing: GetOpenapiListing | Unset = UNSET,
    oas: GetOpenapiOas | Unset = "3.1",
) -> Any | GetOpenapiResponse200 | Problem | None:
    """The OpenAPI document of the API, whole or for one listing, in its 3.1 or 3.0 form.

     Built from the typed endpoint catalog, served bare (no envelope). Each RapidAPI listing imports its
    own document with `listing`, in the 3.0 form (`oas=3.0`), the one RapidAPI's import accepts. Not
    counted against the free tier's per-address limits.

    Args:
        listing (GetOpenapiListing | Unset):
        oas (GetOpenapiOas | Unset):  Default: '3.1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetOpenapiResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        listing=listing,
        oas=oas,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    listing: GetOpenapiListing | Unset = UNSET,
    oas: GetOpenapiOas | Unset = "3.1",
) -> Response[Any | GetOpenapiResponse200 | Problem]:
    """The OpenAPI document of the API, whole or for one listing, in its 3.1 or 3.0 form.

     Built from the typed endpoint catalog, served bare (no envelope). Each RapidAPI listing imports its
    own document with `listing`, in the 3.0 form (`oas=3.0`), the one RapidAPI's import accepts. Not
    counted against the free tier's per-address limits.

    Args:
        listing (GetOpenapiListing | Unset):
        oas (GetOpenapiOas | Unset):  Default: '3.1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetOpenapiResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        listing=listing,
        oas=oas,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    listing: GetOpenapiListing | Unset = UNSET,
    oas: GetOpenapiOas | Unset = "3.1",
) -> Any | GetOpenapiResponse200 | Problem | None:
    """The OpenAPI document of the API, whole or for one listing, in its 3.1 or 3.0 form.

     Built from the typed endpoint catalog, served bare (no envelope). Each RapidAPI listing imports its
    own document with `listing`, in the 3.0 form (`oas=3.0`), the one RapidAPI's import accepts. Not
    counted against the free tier's per-address limits.

    Args:
        listing (GetOpenapiListing | Unset):
        oas (GetOpenapiOas | Unset):  Default: '3.1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetOpenapiResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            listing=listing,
            oas=oas,
        )
    ).parsed
