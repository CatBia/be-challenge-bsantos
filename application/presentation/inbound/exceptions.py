from typing import Optional
from presentation.inbound.constants import COMPETITION_INBOUND_ERROR, TEAM_INBOUND_ERROR
from settings.configuration import get_logger

logger = get_logger()


class CompetitionInboundError(Exception):
    def __init__(
        self, message: Optional[str] = None, details: Optional[str | dict] = None
    ) -> None:
        self.message = message or COMPETITION_INBOUND_ERROR
        self.details = details or {}
        logger.error(self.message)


class TeamInboundError(Exception):
    def __init__(
        self, message: Optional[str] = None, details: Optional[str | dict] = None
    ) -> None:
        self.message = message or TEAM_INBOUND_ERROR
        self.details = details or {}
        logger.error(self.message)
