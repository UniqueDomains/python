from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_related_words_response_200 import ListRelatedWordsResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    word: str,
    *,
    limit: int | Unset = 50,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/words/{word}/related".format(
            word=quote(str(word), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ListRelatedWordsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListRelatedWordsResponse200.from_dict(response.json())

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
) -> Response[Any | ListRelatedWordsResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    word: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    fields: str | Unset = UNSET,
) -> Response[Any | ListRelatedWordsResponse200 | Problem]:
    """A word's synonyms then related words, closest first, with their open names.

     Synonyms (levels 0 and 1) then related words (level 2), closest first. Neighbours with a deny class
    are left out.

    Args:
        word (str):
        limit (int | Unset):  Default: 50.
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListRelatedWordsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        word=word,
        limit=limit,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    word: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    fields: str | Unset = UNSET,
) -> Any | ListRelatedWordsResponse200 | Problem | None:
    """A word's synonyms then related words, closest first, with their open names.

     Synonyms (levels 0 and 1) then related words (level 2), closest first. Neighbours with a deny class
    are left out.

    Args:
        word (str):
        limit (int | Unset):  Default: 50.
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListRelatedWordsResponse200 | Problem
    """

    return sync_detailed(
        word=word,
        client=client,
        limit=limit,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    word: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    fields: str | Unset = UNSET,
) -> Response[Any | ListRelatedWordsResponse200 | Problem]:
    """A word's synonyms then related words, closest first, with their open names.

     Synonyms (levels 0 and 1) then related words (level 2), closest first. Neighbours with a deny class
    are left out.

    Args:
        word (str):
        limit (int | Unset):  Default: 50.
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListRelatedWordsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        word=word,
        limit=limit,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    word: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    fields: str | Unset = UNSET,
) -> Any | ListRelatedWordsResponse200 | Problem | None:
    """A word's synonyms then related words, closest first, with their open names.

     Synonyms (levels 0 and 1) then related words (level 2), closest first. Neighbours with a deny class
    are left out.

    Args:
        word (str):
        limit (int | Unset):  Default: 50.
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListRelatedWordsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            word=word,
            client=client,
            limit=limit,
            fields=fields,
        )
    ).parsed
