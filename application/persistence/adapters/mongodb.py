from settings.configuration import Configuration
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from persistence.adapters.base import DatabaseManager
from persistence.repositories.competition import (
    CompetitionManager,
    CompetitionRepository,
)
from persistence.repositories.access import AccessRepository


class MongoManager(DatabaseManager):
    client: AsyncIOMotorClient = None
    database: AsyncIOMotorDatabase = None
    competition_repo: CompetitionManager = None
    access_repo: AccessRepository = None


db = MongoManager()


def get_mongodb_remote_url() -> str:
    return Configuration.MONGO_DB_REMOTE_URL.value


def get_mongodb_test_url() -> str:
    return Configuration.MONGO_DB_TEST_URL.value


def get_mongo_url() -> str:
    if Configuration.ENVIRONMENT.value == "TEST":
        return get_mongodb_test_url()
    return get_mongodb_remote_url()


def get_mongo_database_name() -> str:
    """
    Get Mongo Database Name
    Return the main mongo database name

    Returns:
        str: Mongo database name
    """
    if Configuration.ENVIRONMENT.value == "TEST":
        return Configuration.MONGO_DB_TEST_NAME.value
    return Configuration.MONGO_DB_REMOTE_NAME.value


def get_database() -> MongoManager:
    return db


async def connect_to_mongo():
    """
    The function `connect_to_mongo` connects to a MongoDB database and initializes repositories.
    """
    MONGODB_URL = get_mongo_url()
    MONGO_DB = get_mongo_database_name()
    db.client = AsyncIOMotorClient(MONGODB_URL)
    db.database = db.client[MONGO_DB]
    db.competition_repo = CompetitionRepository(db.database)
    db.access_repo = AccessRepository(db.database)
    return db


async def close_mongo_connection():
    """
    The function `close_mongo_connection` closes the connection with MongoDB.
    """
    db.client.close()
