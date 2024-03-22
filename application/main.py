from settings.configuration import Configuration
from fastapi import FastAPI
import logging
import uvicorn
from presentation.outbound.league import league_router

from settings.configuration import get_logger

configuration = Configuration()

app = FastAPI()
app.include_router(league_router)

uvicorn_logger = logging.getLogger("uvicorn")
logger = get_logger()

for handler in logger.handlers:
    uvicorn_logger.setLevel(logging.DEBUG)
    uvicorn_logger.addHandler(handler)

if __name__ == "__main__":
    uvicorn.run(app, host=configuration.HOST, port=configuration.PORT)
