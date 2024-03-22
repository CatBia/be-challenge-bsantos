import pytest_asyncio
import pytest
import json
import mock
import aiohttp
import os


def competition_raw_api_response():
    """
    Fixture to return a raw competition API response.

    Args:
        None

    Returns:
        dict: A object containing the raw competition API response.
    """
    path = os.path.dirname(os.path.abspath(__file__))
    with open(f"{path}/cassete/competition_PL.json", "r") as _f:
        content = _f.read()
        return json.loads(content)


def team_raw_api_response():
    """
    Fixture to return a raw team API response.

    Args:
        None

    Returns:
        dict: A object containing the raw competition API response.
    """
    path = os.path.dirname(os.path.abspath(__file__))
    with open(f"{path}/cassete/team_90.json", "r") as _f:
        content = _f.read()
        return json.loads(content)


class FakeClientSession:
    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

    async def get(self, *args, **kwargs):
        return self


class ValidFakeClientSession(FakeClientSession):
    async def json(self):
        return competition_raw_api_response()

    @property
    def status(self):
        return 200


class InvalidFakeClientSession(FakeClientSession):
    async def json(self):
        return {"err": "generic_error"}

    @property
    def status(self):
        return 500


class ValidFakeTeamClientSession(FakeClientSession):
    async def json(self):
        return team_raw_api_response()

    @property
    def status(self):
        return 200


class InvalidFakeTeamClientSession(FakeClientSession):
    async def json(self):
        return {"err": "generic_error"}

    @property
    def status(self):
        return 500


@pytest_asyncio.fixture(scope="function")
async def valid_competition_api_response(monkeypatch):
    monkeypatch.setattr(aiohttp, "ClientSession", ValidFakeClientSession)


@pytest_asyncio.fixture(scope="function")
async def invalid_competition_api_response(monkeypatch):
    monkeypatch.setattr(aiohttp, "ClientSession", InvalidFakeClientSession)


@pytest_asyncio.fixture(scope="function")
async def valid_team_api_response(monkeypatch):
    monkeypatch.setattr(aiohttp, "ClientSession", ValidFakeTeamClientSession)


@pytest_asyncio.fixture(scope="function")
async def invalid_team_api_response(monkeypatch):
    monkeypatch.setattr(aiohttp, "ClientSession", InvalidFakeTeamClientSession)
