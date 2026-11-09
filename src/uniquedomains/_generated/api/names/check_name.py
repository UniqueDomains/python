from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.check_name_body import CheckNameBody
from ...models.check_name_response_200 import CheckNameResponse200
from ...models.check_name_response_202 import CheckNameResponse202
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    body: CheckNameBody,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/names/{name}/check".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CheckNameResponse200 | CheckNameResponse202 | Problem | None:
    if response.status_code == 200:
        response_200 = CheckNameResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = CheckNameResponse202.from_dict(response.json())

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
) -> Response[CheckNameResponse200 | CheckNameResponse202 | Problem]:
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
    body: CheckNameBody,
    fields: str | Unset = UNSET,
) -> Response[CheckNameResponse200 | CheckNameResponse202 | Problem]:
    """Reads one name live from its registry and a registrar, stores the answer and returns the keyed name
    resource.

     Billed `Live=1` when the live read answered (200, `checked: true`) or when the registry was asked
    and did not conclude (202); `Live=0` when the answer came from storage (200, `checked: false`).
    Asking `value` or `history` answers 202 with the stored resource so far, `Retry-After: 30` and
    `Location`; the check never runs the appraisal (`POST /names/{name}/appraise` does). 2,000 live
    checks a UTC day for the whole API, 200 per consumer.

    Args:
        name (str):
        fields (str | Unset):
        body (CheckNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckNameResponse200 | CheckNameResponse202 | Problem]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
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
    body: CheckNameBody,
    fields: str | Unset = UNSET,
) -> CheckNameResponse200 | CheckNameResponse202 | Problem | None:
    """Reads one name live from its registry and a registrar, stores the answer and returns the keyed name
    resource.

     Billed `Live=1` when the live read answered (200, `checked: true`) or when the registry was asked
    and did not conclude (202); `Live=0` when the answer came from storage (200, `checked: false`).
    Asking `value` or `history` answers 202 with the stored resource so far, `Retry-After: 30` and
    `Location`; the check never runs the appraisal (`POST /names/{name}/appraise` does). 2,000 live
    checks a UTC day for the whole API, 200 per consumer.

    Args:
        name (str):
        fields (str | Unset):
        body (CheckNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckNameResponse200 | CheckNameResponse202 | Problem
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    body: CheckNameBody,
    fields: str | Unset = UNSET,
) -> Response[CheckNameResponse200 | CheckNameResponse202 | Problem]:
    """Reads one name live from its registry and a registrar, stores the answer and returns the keyed name
    resource.

     Billed `Live=1` when the live read answered (200, `checked: true`) or when the registry was asked
    and did not conclude (202); `Live=0` when the answer came from storage (200, `checked: false`).
    Asking `value` or `history` answers 202 with the stored resource so far, `Retry-After: 30` and
    `Location`; the check never runs the appraisal (`POST /names/{name}/appraise` does). 2,000 live
    checks a UTC day for the whole API, 200 per consumer.

    Args:
        name (str):
        fields (str | Unset):
        body (CheckNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckNameResponse200 | CheckNameResponse202 | Problem]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    body: CheckNameBody,
    fields: str | Unset = UNSET,
) -> CheckNameResponse200 | CheckNameResponse202 | Problem | None:
    """Reads one name live from its registry and a registrar, stores the answer and returns the keyed name
    resource.

     Billed `Live=1` when the live read answered (200, `checked: true`) or when the registry was asked
    and did not conclude (202); `Live=0` when the answer came from storage (200, `checked: false`).
    Asking `value` or `history` answers 202 with the stored resource so far, `Retry-After: 30` and
    `Location`; the check never runs the appraisal (`POST /names/{name}/appraise` does). 2,000 live
    checks a UTC day for the whole API, 200 per consumer.

    Args:
        name (str):
        fields (str | Unset):
        body (CheckNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckNameResponse200 | CheckNameResponse202 | Problem
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
            fields=fields,
        )
    ).parsed
