from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_tld_applications_contention import (
    ListTldApplicationsContention,
)
from ...models.list_tld_applications_pop import (
    ListTldApplicationsPop,
)
from ...models.list_tld_applications_response_200 import ListTldApplicationsResponse200
from ...models.list_tld_applications_sales import (
    ListTldApplicationsSales,
)
from ...models.list_tld_applications_status import (
    ListTldApplicationsStatus,
)
from ...models.list_tld_applications_type import (
    ListTldApplicationsType,
)
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    type_: ListTldApplicationsType | Unset = UNSET,
    status: ListTldApplicationsStatus | Unset = UNSET,
    contention: ListTldApplicationsContention | Unset = UNSET,
    word: bool | Unset = UNSET,
    pop: ListTldApplicationsPop | Unset = UNSET,
    sales: ListTldApplicationsSales | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_contention: str | Unset = UNSET
    if not isinstance(contention, Unset):
        json_contention = contention

    params["contention"] = json_contention

    params["word"] = word

    json_pop: str | Unset = UNSET
    if not isinstance(pop, Unset):
        json_pop = pop

    params["pop"] = json_pop

    json_sales: str | Unset = UNSET
    if not isinstance(sales, Unset):
        json_sales = sales

    params["sales"] = json_sales

    params["limit"] = limit

    params["cursor"] = cursor

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tld-applications",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ListTldApplicationsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListTldApplicationsResponse200.from_dict(response.json())

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
) -> Response[Any | ListTldApplicationsResponse200 | Problem]:
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
    type_: ListTldApplicationsType | Unset = UNSET,
    status: ListTldApplicationsStatus | Unset = UNSET,
    contention: ListTldApplicationsContention | Unset = UNSET,
    word: bool | Unset = UNSET,
    pop: ListTldApplicationsPop | Unset = UNSET,
    sales: ListTldApplicationsSales | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | ListTldApplicationsResponse200 | Problem]:
    """The 2026 new gTLD round as ICANN publishes it, A to Z, with two simple bands.

     Keyset on `(string, applicationId)`. `sort`, `dir`, `page` and `view` are refused.

    Args:
        q (str | Unset):
        type_ (ListTldApplicationsType | Unset):
        status (ListTldApplicationsStatus | Unset):
        contention (ListTldApplicationsContention | Unset):
        word (bool | Unset):
        pop (ListTldApplicationsPop | Unset):
        sales (ListTldApplicationsSales | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListTldApplicationsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        q=q,
        type_=type_,
        status=status,
        contention=contention,
        word=word,
        pop=pop,
        sales=sales,
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
    type_: ListTldApplicationsType | Unset = UNSET,
    status: ListTldApplicationsStatus | Unset = UNSET,
    contention: ListTldApplicationsContention | Unset = UNSET,
    word: bool | Unset = UNSET,
    pop: ListTldApplicationsPop | Unset = UNSET,
    sales: ListTldApplicationsSales | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | ListTldApplicationsResponse200 | Problem | None:
    """The 2026 new gTLD round as ICANN publishes it, A to Z, with two simple bands.

     Keyset on `(string, applicationId)`. `sort`, `dir`, `page` and `view` are refused.

    Args:
        q (str | Unset):
        type_ (ListTldApplicationsType | Unset):
        status (ListTldApplicationsStatus | Unset):
        contention (ListTldApplicationsContention | Unset):
        word (bool | Unset):
        pop (ListTldApplicationsPop | Unset):
        sales (ListTldApplicationsSales | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListTldApplicationsResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        q=q,
        type_=type_,
        status=status,
        contention=contention,
        word=word,
        pop=pop,
        sales=sales,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    type_: ListTldApplicationsType | Unset = UNSET,
    status: ListTldApplicationsStatus | Unset = UNSET,
    contention: ListTldApplicationsContention | Unset = UNSET,
    word: bool | Unset = UNSET,
    pop: ListTldApplicationsPop | Unset = UNSET,
    sales: ListTldApplicationsSales | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[Any | ListTldApplicationsResponse200 | Problem]:
    """The 2026 new gTLD round as ICANN publishes it, A to Z, with two simple bands.

     Keyset on `(string, applicationId)`. `sort`, `dir`, `page` and `view` are refused.

    Args:
        q (str | Unset):
        type_ (ListTldApplicationsType | Unset):
        status (ListTldApplicationsStatus | Unset):
        contention (ListTldApplicationsContention | Unset):
        word (bool | Unset):
        pop (ListTldApplicationsPop | Unset):
        sales (ListTldApplicationsSales | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListTldApplicationsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        q=q,
        type_=type_,
        status=status,
        contention=contention,
        word=word,
        pop=pop,
        sales=sales,
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
    type_: ListTldApplicationsType | Unset = UNSET,
    status: ListTldApplicationsStatus | Unset = UNSET,
    contention: ListTldApplicationsContention | Unset = UNSET,
    word: bool | Unset = UNSET,
    pop: ListTldApplicationsPop | Unset = UNSET,
    sales: ListTldApplicationsSales | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Any | ListTldApplicationsResponse200 | Problem | None:
    """The 2026 new gTLD round as ICANN publishes it, A to Z, with two simple bands.

     Keyset on `(string, applicationId)`. `sort`, `dir`, `page` and `view` are refused.

    Args:
        q (str | Unset):
        type_ (ListTldApplicationsType | Unset):
        status (ListTldApplicationsStatus | Unset):
        contention (ListTldApplicationsContention | Unset):
        word (bool | Unset):
        pop (ListTldApplicationsPop | Unset):
        sales (ListTldApplicationsSales | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListTldApplicationsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            type_=type_,
            status=status,
            contention=contention,
            word=word,
            pop=pop,
            sales=sales,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
