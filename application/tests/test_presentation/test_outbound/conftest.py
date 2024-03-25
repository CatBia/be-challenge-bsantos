from fastapi import FastAPI
from typing import Any, Generator
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport
import pytest_asyncio
from main import app
import pytest
import aiohttp
import json
import os


@pytest.fixture(scope="function")
def _app() -> Generator[FastAPI, Any, None]:
    """
    Create test application
    """
    yield app


@pytest_asyncio.fixture(scope="function")
async def client(_app: FastAPI) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
