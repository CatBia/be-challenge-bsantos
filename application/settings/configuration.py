import os
import logging

get_env = lambda key, other=None: os.environ.get(key, other)


class Configuration:
    FOOTBALL_URI = get_env("FOOTBALL_URI")
    FOOTBALL_COMPETITION_ENDPOINT = get_env("FOOTBALL_COMPETITION_ENDPOINT")
    FOOTBALL_CTEAM_ENDPOINT = get_env("FOOTBALL_TEAM_ENDPOINT")
    X_API_TOKEN = get_env("X_API_TOKEN")
    HOST = get_env("HOST", "0.0.0.0")
    POST = get_env("PORT", 8003)


def get_logger(name: str = "BE_CHALLENGE_BSANTOS") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    return logger
