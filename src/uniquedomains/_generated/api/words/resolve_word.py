from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.resolve_word_response_200 import ResolveWordResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/words/resolve",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Problem | ResolveWordResponse200 | None:
    if response.status_code == 200:
        response_200 = ResolveWordResponse200.from_dict(response.json())

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
) -> Response[Any | Problem | ResolveWordResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: str,
    fields: str | Unset = UNSET,
) -> Response[Any | Problem | ResolveWordResponse200]:
    """Turns what a caller typed into the catalog word it names, or up to five candidates.

     Tries the spelling as typed, its lowercase, accents stripped, spaces and hyphens removed, one
    inflection suffix stripped, then the lookalike spelling. A miss answers 200 with `candidates` (words
    starting with the query), never 404. Words with a deny class are never a match nor a candidate.

    Args:
        q (str):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem | ResolveWordResponse200]
    """

    kwargs = _get_kwargs(
        q=q,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: str,
    fields: str | Unset = UNSET,
) -> Any | Problem | ResolveWordResponse200 | None:
    """Turns what a caller typed into the catalog word it names, or up to five candidates.

     Tries the spelling as typed, its lowercase, accents stripped, spaces and hyphens removed, one
    inflection suffix stripped, then the lookalike spelling. A miss answers 200 with `candidates` (words
    starting with the query), never 404. Words with a deny class are never a match nor a candidate.

    Args:
        q (str):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem | ResolveWordResponse200
    """

    return sync_detailed(
        client=client,
        q=q,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str,
    fields: str | Unset = UNSET,
) -> Response[Any | Problem | ResolveWordResponse200]:
    """Turns what a caller typed into the catalog word it names, or up to five candidates.

     Tries the spelling as typed, its lowercase, accents stripped, spaces and hyphens removed, one
    inflection suffix stripped, then the lookalike spelling. A miss answers 200 with `candidates` (words
    starting with the query), never 404. Words with a deny class are never a match nor a candidate.

    Args:
        q (str):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem | ResolveWordResponse200]
    """

    kwargs = _get_kwargs(
        q=q,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str,
    fields: str | Unset = UNSET,
) -> Any | Problem | ResolveWordResponse200 | None:
    """Turns what a caller typed into the catalog word it names, or up to five candidates.

     Tries the spelling as typed, its lowercase, accents stripped, spaces and hyphens removed, one
    inflection suffix stripped, then the lookalike spelling. A miss answers 200 with `candidates` (words
    starting with the query), never 404. Words with a deny class are never a match nor a candidate.

    Args:
        q (str):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem | ResolveWordResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            fields=fields,
        )
    ).parsed
