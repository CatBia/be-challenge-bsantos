from fastapi import FastAPI
from typing import Any, Generator, List
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport
import pytest_asyncio
from main import app
import pytest
from persistence.adapters.mongodb import (
    MongoManager,
    get_mongo_database_name,
    get_mongo_url,
    get_database,
)
from persistence.repositories.competition import CompetitionRepository
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession
import asyncio
from tests.test_persistence.factories import CompetitionDataFactory, TeamDataFactory


@pytest.fixture(scope="function")
def get_configured_database():
    manager = MongoManager()

    client = AsyncIOMotorClient(get_mongo_url())
    client.get_io_loop = asyncio.get_running_loop
    manager.client = client
    manager.database = get_mongo_database_name()
    database_engine = client[manager.database]
    competition_repo = CompetitionRepository(db_client=database_engine)
    manager.competition_repo = competition_repo

    yield manager
    manager.client.close()


@pytest.fixture(scope="function")
def _app(get_configured_database) -> Generator[FastAPI, Any, None]:
    """
    Create test application.

    Args:
        get_configured_database: A function that returns a configured database.

    Yields:
        FastAPI: The test application instance.
    """
    get_configured_database
    yield app


@pytest_asyncio.fixture(scope="function")
async def db_session(
    _app: FastAPI, get_configured_database
) -> Generator[AsyncIOMotorClientSession, Any, None]:
    """
    A context manager that provides a database session for testing.

    Args:
        app (FastAPI): The FastAPI application instance.
        get_configured_database: A function that returns a configured database instance.

    Yields:
        Nothing
    At the end, we drop the database to clean it up and have a hygienic environment for the next test.

    """
    yield get_configured_database
    get_configured_database.client.drop_database(get_configured_database.database)


@pytest_asyncio.fixture(scope="function")
async def client(_app: FastAPI, db_session) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """
    transport = ASGITransport(app=app)

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_database] = _get_test_db
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


@pytest_asyncio.fixture
async def build_one_competition_data(db_session):
    competition_data = CompetitionDataFactory()
    id_generated = await db_session.client[db_session.database][
        "Competition"
    ].insert_one(competition_data.model_dump())
    return competition_data


@pytest_asyncio.fixture
async def build_repeated_competition_data(db_session):
    competition_data = CompetitionDataFactory()
    id_generated = await db_session.client[db_session.database][
        "Competition"
    ].insert_one(competition_data.model_dump())
    id_generated = await db_session.client[db_session.database][
        "Competition"
    ].insert_one(competition_data.model_dump())
    return competition_data


@pytest_asyncio.fixture
async def build_competition_data_noplayers(db_session):
    teams = TeamDataFactory.create_batch(5, players=None)
    competition_data = CompetitionDataFactory(teams=teams)
    id_generated = await db_session.client[db_session.database][
        "Competition"
    ].insert_one(competition_data.model_dump())
    return competition_data
