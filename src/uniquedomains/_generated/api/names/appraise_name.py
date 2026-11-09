from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appraise_name_response_200 import AppraiseNameResponse200
from ...models.appraise_name_response_202 import AppraiseNameResponse202
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/names/{name}/appraise".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppraiseNameResponse200 | AppraiseNameResponse202 | Problem | None:
    if response.status_code == 200:
        response_200 = AppraiseNameResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = AppraiseNameResponse202.from_dict(response.json())

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
) -> Response[AppraiseNameResponse200 | AppraiseNameResponse202 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> Response[AppraiseNameResponse200 | AppraiseNameResponse202 | Problem]:
    """Runs the appraisal of one stored name when its estimate is missing, and returns the value resource.

     A fresh estimate answers 200 with `Appraisal=0` and no run. A run this call started answers 200 with
    `Appraisal=1`; a run another call holds answers 202 with `Retry-After: 30` and `Appraisal=0`, and a
    run another call finished meanwhile 200 with `Appraisal=0`. The name must be stored: run `POST
    /names/{name}/check` first. 5,000 runs a UTC day for the whole API.

    Args:
        name (str):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppraiseNameResponse200 | AppraiseNameResponse202 | Problem]
    """

    kwargs = _get_kwargs(
        name=name,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> AppraiseNameResponse200 | AppraiseNameResponse202 | Problem | None:
    """Runs the appraisal of one stored name when its estimate is missing, and returns the value resource.

     A fresh estimate answers 200 with `Appraisal=0` and no run. A run this call started answers 200 with
    `Appraisal=1`; a run another call holds answers 202 with `Retry-After: 30` and `Appraisal=0`, and a
    run another call finished meanwhile 200 with `Appraisal=0`. The name must be stored: run `POST
    /names/{name}/check` first. 5,000 runs a UTC day for the whole API.

    Args:
        name (str):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppraiseNameResponse200 | AppraiseNameResponse202 | Problem
    """

    return sync_detailed(
        name=name,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> Response[AppraiseNameResponse200 | AppraiseNameResponse202 | Problem]:
    """Runs the appraisal of one stored name when its estimate is missing, and returns the value resource.

     A fresh estimate answers 200 with `Appraisal=0` and no run. A run this call started answers 200 with
    `Appraisal=1`; a run another call holds answers 202 with `Retry-After: 30` and `Appraisal=0`, and a
    run another call finished meanwhile 200 with `Appraisal=0`. The name must be stored: run `POST
    /names/{name}/check` first. 5,000 runs a UTC day for the whole API.

    Args:
        name (str):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppraiseNameResponse200 | AppraiseNameResponse202 | Problem]
    """

    kwargs = _get_kwargs(
        name=name,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> AppraiseNameResponse200 | AppraiseNameResponse202 | Problem | None:
    """Runs the appraisal of one stored name when its estimate is missing, and returns the value resource.

     A fresh estimate answers 200 with `Appraisal=0` and no run. A run this call started answers 200 with
    `Appraisal=1`; a run another call holds answers 202 with `Retry-After: 30` and `Appraisal=0`, and a
    run another call finished meanwhile 200 with `Appraisal=0`. The name must be stored: run `POST
    /names/{name}/check` first. 5,000 runs a UTC day for the whole API.

    Args:
        name (str):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppraiseNameResponse200 | AppraiseNameResponse202 | Problem
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            fields=fields,
        )
    ).parsed
