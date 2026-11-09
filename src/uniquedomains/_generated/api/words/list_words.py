from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_words_origin import ListWordsOrigin
from ...models.list_words_response_200 import ListWordsResponse200
from ...models.list_words_shape import ListWordsShape
from ...models.list_words_style import ListWordsStyle
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    contains: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    shape: ListWordsShape | Unset = UNSET,
    min_length: int | Unset = UNSET,
    max_length: int | Unset = UNSET,
    popularity_min: int | Unset = UNSET,
    popularity_max: int | Unset = UNSET,
    sentiment_min: int | Unset = UNSET,
    sentiment_max: int | Unset = UNSET,
    style: ListWordsStyle | Unset = UNSET,
    syllables: int | Unset = UNSET,
    origin: ListWordsOrigin | Unset = UNSET,
    category: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["contains"] = contains

    params["pos"] = pos

    json_shape: str | Unset = UNSET
    if not isinstance(shape, Unset):
        json_shape = shape

    params["shape"] = json_shape

    params["minLength"] = min_length

    params["maxLength"] = max_length

    params["popularityMin"] = popularity_min

    params["popularityMax"] = popularity_max

    params["sentimentMin"] = sentiment_min

    params["sentimentMax"] = sentiment_max

    json_style: str | Unset = UNSET
    if not isinstance(style, Unset):
        json_style = style

    params["style"] = json_style

    params["syllables"] = syllables

    json_origin: str | Unset = UNSET
    if not isinstance(origin, Unset):
        json_origin = origin

    params["origin"] = json_origin

    params["category"] = category

    params["limit"] = limit

    params["cursor"] = cursor

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/words",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ListWordsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListWordsResponse200.from_dict(response.json())

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
) -> Response[Any | ListWordsResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    contains: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    shape: ListWordsShape | Unset = UNSET,
    min_length: int | Unset = UNSET,
    max_length: int | Unset = UNSET,
    popularity_min: int | Unset = UNSET,
    popularity_max: int | Unset = UNSET,
    sentiment_min: int | Unset = UNSET,
    sentiment_max: int | Unset = UNSET,
    style: ListWordsStyle | Unset = UNSET,
    syllables: int | Unset = UNSET,
    origin: ListWordsOrigin | Unset = UNSET,
    category: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | ListWordsResponse200 | Problem]:
    """Searches the catalog's words by text and facets, alphabetically.

     Enabled words only, every word with a deny class left out. Alphabetical order only, keyset-paged by
    `(word, id)`. Popularity and sentiment are numeric ranges on the stored 0 to 100 scale.

    Args:
        q (str | Unset):
        contains (str | Unset):
        pos (str | Unset):
        shape (ListWordsShape | Unset):
        min_length (int | Unset):
        max_length (int | Unset):
        popularity_min (int | Unset):
        popularity_max (int | Unset):
        sentiment_min (int | Unset):
        sentiment_max (int | Unset):
        style (ListWordsStyle | Unset):
        syllables (int | Unset):
        origin (ListWordsOrigin | Unset):
        category (str | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListWordsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        q=q,
        contains=contains,
        pos=pos,
        shape=shape,
        min_length=min_length,
        max_length=max_length,
        popularity_min=popularity_min,
        popularity_max=popularity_max,
        sentiment_min=sentiment_min,
        sentiment_max=sentiment_max,
        style=style,
        syllables=syllables,
        origin=origin,
        category=category,
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
    q: str | Unset = UNSET,
    contains: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    shape: ListWordsShape | Unset = UNSET,
    min_length: int | Unset = UNSET,
    max_length: int | Unset = UNSET,
    popularity_min: int | Unset = UNSET,
    popularity_max: int | Unset = UNSET,
    sentiment_min: int | Unset = UNSET,
    sentiment_max: int | Unset = UNSET,
    style: ListWordsStyle | Unset = UNSET,
    syllables: int | Unset = UNSET,
    origin: ListWordsOrigin | Unset = UNSET,
    category: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | ListWordsResponse200 | Problem | None:
    """Searches the catalog's words by text and facets, alphabetically.

     Enabled words only, every word with a deny class left out. Alphabetical order only, keyset-paged by
    `(word, id)`. Popularity and sentiment are numeric ranges on the stored 0 to 100 scale.

    Args:
        q (str | Unset):
        contains (str | Unset):
        pos (str | Unset):
        shape (ListWordsShape | Unset):
        min_length (int | Unset):
        max_length (int | Unset):
        popularity_min (int | Unset):
        popularity_max (int | Unset):
        sentiment_min (int | Unset):
        sentiment_max (int | Unset):
        style (ListWordsStyle | Unset):
        syllables (int | Unset):
        origin (ListWordsOrigin | Unset):
        category (str | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListWordsResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        q=q,
        contains=contains,
        pos=pos,
        shape=shape,
        min_length=min_length,
        max_length=max_length,
        popularity_min=popularity_min,
        popularity_max=popularity_max,
        sentiment_min=sentiment_min,
        sentiment_max=sentiment_max,
        style=style,
        syllables=syllables,
        origin=origin,
        category=category,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    contains: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    shape: ListWordsShape | Unset = UNSET,
    min_length: int | Unset = UNSET,
    max_length: int | Unset = UNSET,
    popularity_min: int | Unset = UNSET,
    popularity_max: int | Unset = UNSET,
    sentiment_min: int | Unset = UNSET,
    sentiment_max: int | Unset = UNSET,
    style: ListWordsStyle | Unset = UNSET,
    syllables: int | Unset = UNSET,
    origin: ListWordsOrigin | Unset = UNSET,
    category: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | ListWordsResponse200 | Problem]:
    """Searches the catalog's words by text and facets, alphabetically.

     Enabled words only, every word with a deny class left out. Alphabetical order only, keyset-paged by
    `(word, id)`. Popularity and sentiment are numeric ranges on the stored 0 to 100 scale.

    Args:
        q (str | Unset):
        contains (str | Unset):
        pos (str | Unset):
        shape (ListWordsShape | Unset):
        min_length (int | Unset):
        max_length (int | Unset):
        popularity_min (int | Unset):
        popularity_max (int | Unset):
        sentiment_min (int | Unset):
        sentiment_max (int | Unset):
        style (ListWordsStyle | Unset):
        syllables (int | Unset):
        origin (ListWordsOrigin | Unset):
        category (str | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListWordsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        q=q,
        contains=contains,
        pos=pos,
        shape=shape,
        min_length=min_length,
        max_length=max_length,
        popularity_min=popularity_min,
        popularity_max=popularity_max,
        sentiment_min=sentiment_min,
        sentiment_max=sentiment_max,
        style=style,
        syllables=syllables,
        origin=origin,
        category=category,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    contains: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    shape: ListWordsShape | Unset = UNSET,
    min_length: int | Unset = UNSET,
    max_length: int | Unset = UNSET,
    popularity_min: int | Unset = UNSET,
    popularity_max: int | Unset = UNSET,
    sentiment_min: int | Unset = UNSET,
    sentiment_max: int | Unset = UNSET,
    style: ListWordsStyle | Unset = UNSET,
    syllables: int | Unset = UNSET,
    origin: ListWordsOrigin | Unset = UNSET,
    category: str | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | ListWordsResponse200 | Problem | None:
    """Searches the catalog's words by text and facets, alphabetically.

     Enabled words only, every word with a deny class left out. Alphabetical order only, keyset-paged by
    `(word, id)`. Popularity and sentiment are numeric ranges on the stored 0 to 100 scale.

    Args:
        q (str | Unset):
        contains (str | Unset):
        pos (str | Unset):
        shape (ListWordsShape | Unset):
        min_length (int | Unset):
        max_length (int | Unset):
        popularity_min (int | Unset):
        popularity_max (int | Unset):
        sentiment_min (int | Unset):
        sentiment_max (int | Unset):
        style (ListWordsStyle | Unset):
        syllables (int | Unset):
        origin (ListWordsOrigin | Unset):
        category (str | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListWordsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            contains=contains,
            pos=pos,
            shape=shape,
            min_length=min_length,
            max_length=max_length,
            popularity_min=popularity_min,
            popularity_max=popularity_max,
            sentiment_min=sentiment_min,
            sentiment_max=sentiment_max,
            style=style,
            syllables=syllables,
            origin=origin,
            category=category,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
