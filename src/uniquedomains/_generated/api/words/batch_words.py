from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_words_body import BatchWordsBody
from ...models.batch_words_response_200 import BatchWordsResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BatchWordsBody,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/words/batch",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BatchWordsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = BatchWordsResponse200.from_dict(response.json())

        return response_200

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
) -> Response[BatchWordsResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BatchWordsBody,
    fields: str | Unset = UNSET,
) -> Response[BatchWordsResponse200 | Problem]:
    """Up to 100 word profiles in one call.

     One entry per key, in the request's order: the profile of `GET /words/{word}`, or `{ word, found:
    false }` for a key the catalog does not answer (unknown, disabled, or never shown). Billed one
    request per key sent, misses included.

    Args:
        fields (str | Unset):
        body (BatchWordsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchWordsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BatchWordsBody,
    fields: str | Unset = UNSET,
) -> BatchWordsResponse200 | Problem | None:
    """Up to 100 word profiles in one call.

     One entry per key, in the request's order: the profile of `GET /words/{word}`, or `{ word, found:
    false }` for a key the catalog does not answer (unknown, disabled, or never shown). Billed one
    request per key sent, misses included.

    Args:
        fields (str | Unset):
        body (BatchWordsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchWordsResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BatchWordsBody,
    fields: str | Unset = UNSET,
) -> Response[BatchWordsResponse200 | Problem]:
    """Up to 100 word profiles in one call.

     One entry per key, in the request's order: the profile of `GET /words/{word}`, or `{ word, found:
    false }` for a key the catalog does not answer (unknown, disabled, or never shown). Billed one
    request per key sent, misses included.

    Args:
        fields (str | Unset):
        body (BatchWordsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchWordsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BatchWordsBody,
    fields: str | Unset = UNSET,
) -> BatchWordsResponse200 | Problem | None:
    """Up to 100 word profiles in one call.

     One entry per key, in the request's order: the profile of `GET /words/{word}`, or `{ word, found:
    false }` for a key the catalog does not answer (unknown, disabled, or never shown). Billed one
    request per key sent, misses included.

    Args:
        fields (str | Unset):
        body (BatchWordsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchWordsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            fields=fields,
        )
    ).parsed
