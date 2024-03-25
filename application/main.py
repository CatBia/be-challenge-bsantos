from settings.configuration import Configuration
from fastapi import FastAPI
import logging
import uvicorn
from presentation.outbound.league import league_router
from presentation.outbound.players import player_router
from presentation.outbound.teams import teams_router
from persistence.adapters.mongodb import connect_to_mongo, close_mongo_connection
from settings.configuration import get_logger


app = FastAPI()
app.include_router(league_router)
app.include_router(player_router)
app.include_router(teams_router)
app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

uvicorn_logger = logging.getLogger("uvicorn")
logger = get_logger()

for handler in logger.handlers:
    uvicorn_logger.setLevel(logging.DEBUG)
    uvicorn_logger.addHandler(handler)

if __name__ == "__main__":
    uvicorn.run(app, host=Configuration.HOST.value, port=Configuration.PORT.value)
