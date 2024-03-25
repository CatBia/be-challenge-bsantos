from presentation.inbound.team import TeamInbound
from settings.configuration import Configuration
from presentation.inbound.entities.team import TeamResponse
from persistence.adapters.base import DatabaseManager


async def get_team(team_id: str) -> TeamResponse:
    team_inbound = TeamInbound()
    return await team_inbound.get_team(team_id)


async def get_team_data_by_team_name(
    database_manager: DatabaseManager,
    team_name: str,
    has_players: bool = False,
    has_coach: bool = False,
):
    teams = await database_manager.competition_repo.get_teams_by_team_name(
        team_name=team_name, players=has_players, coach=has_coach
    )
    return teams
