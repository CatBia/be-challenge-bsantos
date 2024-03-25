import asyncio
from business_rules.services import translator as translator_service
from business_rules.services import team as team_service
from business_rules.services import competition as competition_service
from business_rules.services import footbal as football_services
from presentation.inbound.entities.team import TeamResponse
from presentation.inbound.entities.competition import (
    CompetitionResponse,
    SeasonResponse,
)
from business_rules.entities.football import Team, Player, Coach, Competition
from typing import List
from persistence.entities.football import (
    CompetitionData,
    TeamData,
    PlayerData,
    CoachData,
)
from persistence.adapters.base import DatabaseManager
from presentation.inbound.exceptions import TeamRestrictedError, TeamReachedRateLimit
import time


async def get_team_by_season_data(season: SeasonResponse) -> TeamResponse:
    team_id = season.winner.id
    team_response: TeamResponse = await team_service.get_team(team_id=team_id)
    return team_response


async def translate_team_response_to_player(team_response: TeamResponse) -> Player:
    return await translator_service._build_player_entity(team_response)


async def translate_team_response_to_coach(team_response: TeamResponse) -> Coach:
    return await translator_service._build_coach_entity(team_response)


async def translate_team_response_to_team(team_response: TeamResponse) -> Team:
    return await translator_service._build_team_entity(team_response)


async def translate_competition_response_to_competition(
    competition_response: CompetitionResponse,
) -> Competition:
    return await translator_service._build_competition_entity(competition_response)


async def _process_season_data_to_team_coach_player(
    season: SeasonResponse,
) -> TeamResponse:
    team_response: TeamResponse = await get_team_by_season_data(season)
    team: Team = await translate_team_response_to_team(team_response)
    players: Player = await translate_team_response_to_player(team_response)
    coach: Coach = await translate_team_response_to_coach(team_response)
    return team, players, coach


async def bulk_process_season_data_to_team_coach_player(
    seasons: List[SeasonResponse],
) -> list:
    team_list = []
    MAX_TRIES = 3
    for season in seasons:
        tries = 1
        while tries <= MAX_TRIES:
            try:
                team, players, coach = await _process_season_data_to_team_coach_player(
                    season
                )
                team_list.append([team, players, coach])
                break
            except TeamRestrictedError as e:
                break
            except TeamReachedRateLimit as e:

                time.sleep(60)
                tries += 1

    return team_list


async def create_competition_data_to_football_repository(
    database_manager: DatabaseManager, team_list: list, competition: Competition
) -> None:
    teams = [
        TeamData(
            name=team.name,
            areaName=team.areaName,
            shortName=team.shortName,
            address=team.address,
            players=[
                PlayerData(
                    name=player.name,
                    position=player.position,
                    dateOfBirth=player.dateOfBirth,
                    nationality=player.nationality,
                )
                for player in player_list
            ],
            coach=CoachData(
                name=coach.name,
                dateOfBirth=coach.dateOfBirth,
                nationality=coach.nationality,
            ),
        )
        for team, player_list, coach in team_list
    ]
    competiiton_data = CompetitionData(
        name=competition.name,
        code=competition.code,
        areaName=competition.areaName,
        teams=teams,
    )
    await football_services.create_competition_data(
        database_manager=database_manager, competition_data=competiiton_data
    )


async def get_import_league(database_manager: DatabaseManager, league_code: str) -> str:
    competition_response: CompetitionResponse = (
        await competition_service.get_competition(league_code=league_code)
    )
    competition: Competition = await translate_competition_response_to_competition(
        competition_response
    )
    all_seasons = competition_response.seasons + [competition_response.currentSeason]
    team_list = await bulk_process_season_data_to_team_coach_player(all_seasons)
    await create_competition_data_to_football_repository(
        database_manager=database_manager, competition=competition, team_list=team_list
    )
    return "success"


async def process_get_import_league(
    database_manager: DatabaseManager, league_code: str
) -> str:
    """
    Process the import league request.

    It processes the import league request and returns the status of the request.

    Args:
        league_code: The league code.

    Returns:
        str: The status of the request.
    """
    await get_import_league(database_manager=database_manager, league_code=league_code)
    return "success"
