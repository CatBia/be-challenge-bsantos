from presentation.inbound.competition import CompetitionInbound
from settings.configuration import Configuration
from presentation.inbound.entities.competition import CompetitionResponse


async def get_competition(league_code: str) -> CompetitionResponse:
    competition_inbound = CompetitionInbound()
    return await competition_inbound.get_competition(league_code)
