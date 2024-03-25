import os
import logging
from enum import Enum

get_env = lambda key, other=None: os.environ.get(key, other)


class Configuration(Enum):
    FOOTBALL_URI = get_env("FOOTBALL_URI")
    FOOTBALL_COMPETITION_ENDPOINT = get_env("FOOTBALL_COMPETITION_ENDPOINT")
    FOOTBALL_TEAM_ENDPOINT = get_env("FOOTBALL_TEAM_ENDPOINT")
    X_API_TOKEN = get_env("X_API_TOKEN")
    HOST = get_env("HOST", "0.0.0.0")
    PORT = int(get_env("PORT", 8003))
    MONGO_DB_TEST_URL = "mongodb://admin:pwd@be-db:27017/"
    MONGO_DB_REMOTE_URL = get_env(
        "MONGO_DB_REMOTE_URL",
    )
    ENVIRONMENT = get_env("ENVIRONMENT", "development")
    MONGO_DB_TEST_NAME = "be_challenge_test"
    MONGO_DB_REMOTE_NAME = "be_challenge_bsantos"


def get_logger(name: str = "BE_CHALLENGE_BSANTOS") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    return logger
