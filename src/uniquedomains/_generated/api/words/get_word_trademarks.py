from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_word_trademarks_office import (
    GetWordTrademarksOffice,
)
from ...models.get_word_trademarks_response_200 import GetWordTrademarksResponse200
from ...models.get_word_trademarks_status import (
    GetWordTrademarksStatus,
)
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    word: str,
    *,
    office: GetWordTrademarksOffice | Unset = UNSET,
    status: GetWordTrademarksStatus | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_office: str | Unset = UNSET
    if not isinstance(office, Unset):
        json_office = office

    params["office"] = json_office

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/words/{word}/trademarks".format(
            word=quote(str(word), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetWordTrademarksResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = GetWordTrademarksResponse200.from_dict(response.json())

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
) -> Response[Any | GetWordTrademarksResponse200 | Problem]:
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
    office: GetWordTrademarksOffice | Unset = UNSET,
    status: GetWordTrademarksStatus | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | GetWordTrademarksResponse200 | Problem]:
    """A word's trademark counts and its exact-match marks.

     Live US and EU trademark counts with their classes, and up to 50 exact-match trademarks (live first,
    newest filing first) before the `office` and `status` filters. Zero live trademarks means no exact
    match was found, never that a name is safe.

    Args:
        word (str):
        office (GetWordTrademarksOffice | Unset):
        status (GetWordTrademarksStatus | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetWordTrademarksResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        word=word,
        office=office,
        status=status,
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
    office: GetWordTrademarksOffice | Unset = UNSET,
    status: GetWordTrademarksStatus | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | GetWordTrademarksResponse200 | Problem | None:
    """A word's trademark counts and its exact-match marks.

     Live US and EU trademark counts with their classes, and up to 50 exact-match trademarks (live first,
    newest filing first) before the `office` and `status` filters. Zero live trademarks means no exact
    match was found, never that a name is safe.

    Args:
        word (str):
        office (GetWordTrademarksOffice | Unset):
        status (GetWordTrademarksStatus | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetWordTrademarksResponse200 | Problem
    """

    return sync_detailed(
        word=word,
        client=client,
        office=office,
        status=status,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    word: str,
    *,
    client: AuthenticatedClient,
    office: GetWordTrademarksOffice | Unset = UNSET,
    status: GetWordTrademarksStatus | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | GetWordTrademarksResponse200 | Problem]:
    """A word's trademark counts and its exact-match marks.

     Live US and EU trademark counts with their classes, and up to 50 exact-match trademarks (live first,
    newest filing first) before the `office` and `status` filters. Zero live trademarks means no exact
    match was found, never that a name is safe.

    Args:
        word (str):
        office (GetWordTrademarksOffice | Unset):
        status (GetWordTrademarksStatus | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetWordTrademarksResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        word=word,
        office=office,
        status=status,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    word: str,
    *,
    client: AuthenticatedClient,
    office: GetWordTrademarksOffice | Unset = UNSET,
    status: GetWordTrademarksStatus | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | GetWordTrademarksResponse200 | Problem | None:
    """A word's trademark counts and its exact-match marks.

     Live US and EU trademark counts with their classes, and up to 50 exact-match trademarks (live first,
    newest filing first) before the `office` and `status` filters. Zero live trademarks means no exact
    match was found, never that a name is safe.

    Args:
        word (str):
        office (GetWordTrademarksOffice | Unset):
        status (GetWordTrademarksStatus | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetWordTrademarksResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            word=word,
            client=client,
            office=office,
            status=status,
            fields=fields,
        )
    ).parsed
