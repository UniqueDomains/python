from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.request_word_response_200 import RequestWordResponse200
from ...models.request_word_response_202 import RequestWordResponse202
from ...types import Response


def _get_kwargs(
    word: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/words/{word}/request".format(
            word=quote(str(word), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | RequestWordResponse200 | RequestWordResponse202 | None:
    if response.status_code == 200:
        response_200 = RequestWordResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = RequestWordResponse202.from_dict(response.json())

        return response_202

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
) -> Response[Problem | RequestWordResponse200 | RequestWordResponse202]:
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
) -> Response[Problem | RequestWordResponse200 | RequestWordResponse202]:
    """Brings a word into the catalog: checks it now and queues an accepted word for the intake.

     Billed `Intake=1` only when the gate accepted the word (202 `accepted`, `Retry-After: 600`, poll the
    request); a word already in the catalog answers 200 `in_catalog`, a queued one 202 `queued` with its
    request id, a refused one 422 with the reason as `code` (`not_a_word`, `brand`, `offensive`), all
    billed `Intake=0`. 10 words a UTC day per consumer and 100 for the whole API, refused words
    included. When the gate cannot answer: 503 `gate_unavailable`, `Retry-After: 60`, never billed.

    Args:
        word (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RequestWordResponse200 | RequestWordResponse202]
    """

    kwargs = _get_kwargs(
        word=word,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    word: str,
    *,
    client: AuthenticatedClient,
) -> Problem | RequestWordResponse200 | RequestWordResponse202 | None:
    """Brings a word into the catalog: checks it now and queues an accepted word for the intake.

     Billed `Intake=1` only when the gate accepted the word (202 `accepted`, `Retry-After: 600`, poll the
    request); a word already in the catalog answers 200 `in_catalog`, a queued one 202 `queued` with its
    request id, a refused one 422 with the reason as `code` (`not_a_word`, `brand`, `offensive`), all
    billed `Intake=0`. 10 words a UTC day per consumer and 100 for the whole API, refused words
    included. When the gate cannot answer: 503 `gate_unavailable`, `Retry-After: 60`, never billed.

    Args:
        word (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RequestWordResponse200 | RequestWordResponse202
    """

    return sync_detailed(
        word=word,
        client=client,
    ).parsed


async def asyncio_detailed(
    word: str,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | RequestWordResponse200 | RequestWordResponse202]:
    """Brings a word into the catalog: checks it now and queues an accepted word for the intake.

     Billed `Intake=1` only when the gate accepted the word (202 `accepted`, `Retry-After: 600`, poll the
    request); a word already in the catalog answers 200 `in_catalog`, a queued one 202 `queued` with its
    request id, a refused one 422 with the reason as `code` (`not_a_word`, `brand`, `offensive`), all
    billed `Intake=0`. 10 words a UTC day per consumer and 100 for the whole API, refused words
    included. When the gate cannot answer: 503 `gate_unavailable`, `Retry-After: 60`, never billed.

    Args:
        word (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RequestWordResponse200 | RequestWordResponse202]
    """

    kwargs = _get_kwargs(
        word=word,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    word: str,
    *,
    client: AuthenticatedClient,
) -> Problem | RequestWordResponse200 | RequestWordResponse202 | None:
    """Brings a word into the catalog: checks it now and queues an accepted word for the intake.

     Billed `Intake=1` only when the gate accepted the word (202 `accepted`, `Retry-After: 600`, poll the
    request); a word already in the catalog answers 200 `in_catalog`, a queued one 202 `queued` with its
    request id, a refused one 422 with the reason as `code` (`not_a_word`, `brand`, `offensive`), all
    billed `Intake=0`. 10 words a UTC day per consumer and 100 for the whole API, refused words
    included. When the gate cannot answer: 503 `gate_unavailable`, `Retry-After: 60`, never billed.

    Args:
        word (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RequestWordResponse200 | RequestWordResponse202
    """

    return (
        await asyncio_detailed(
            word=word,
            client=client,
        )
    ).parsed
