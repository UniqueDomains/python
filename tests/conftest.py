from __future__ import annotations

from collections.abc import Iterator

import pytest

from uniquedomains import Client

from .fixture_server import FixtureServer, start


@pytest.fixture(scope="session")
def server() -> Iterator[FixtureServer]:
    yield from start()


@pytest.fixture
def fixtures(server: FixtureServer) -> FixtureServer:
    server.reset()
    return server


@pytest.fixture
def base(fixtures: FixtureServer) -> str:
    """The public base on the fixture server."""
    return f"{fixtures.url}/v1"


@pytest.fixture
def ud(base: str, monkeypatch: pytest.MonkeyPatch) -> Iterator[Client]:
    """A keyless client on the fixture server."""
    monkeypatch.delenv("UD_API_KEY", raising=False)
    with Client(base_url=base) as client:
        yield client
