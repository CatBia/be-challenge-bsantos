from presentation.inbound.team import TeamInbound
from settings.configuration import Configuration
from presentation.inbound.entities.team import TeamResponse


async def get_team(team_id: str) -> TeamResponse:
    config = Configuration()
    team_inbound = TeamInbound(config)
    return await team_inbound.get_team(team_id)
