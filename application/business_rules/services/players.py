from persistence.repositories.competition import CompetitionRepository
from typing import Optional
from persistence.repositories.exceptions import PlayersNotFound


from persistence.adapters.mongodb import DatabaseManager


async def get_players(
    database_manager: DatabaseManager, league_code: str, team_name: Optional[str] = None
):
    players = await database_manager.competition_repo.get_players_by_league_code(
        league_code=league_code
    )
    if not players:
        raise PlayersNotFound()
    return players


async def get_players_team(
    database_manager: DatabaseManager, team_name: Optional[str] = None
):
    players = await database_manager.competition_repo.get_players_by_team_name(
        team_name=team_name
    )
    if not players:
        raise PlayersNotFound()
    return players
