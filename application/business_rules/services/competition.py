from presentation.inbound.competition import CompetitionInbound
from settings.configuration import Configuration
from presentation.inbound.entities.competition import CompetitionResponse


async def get_competition(league_code: str) -> CompetitionResponse:
    config = Configuration()
    competition_inbound = CompetitionInbound(config)
    return await competition_inbound.get_competition(league_code)
