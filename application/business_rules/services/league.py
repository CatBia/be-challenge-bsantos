import asyncio
from business_rules.services import translator as translator_service
from business_rules.services import team as team_service
from business_rules.services import competition as competition_service
from presentation.inbound.entities.team import TeamResponse
from presentation.inbound.entities.competition import (
    CompetitionResponse,
    SeasonResponse,
)
from business_rules.entities.football import Team, Player, Coach, Competition
from typing import List


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
) -> List[TeamResponse]:
    team_list = []
    player_list = []
    coach_list = []
    for season in seasons:
        team, players, coach = await _process_season_data_to_team_coach_player(season)
        team_list.append(team)
        player_list.append(players)
        coach_list.append(coach)


async def get_import_league(league_code: str) -> str:
    competition_response: CompetitionResponse = (
        await competition_service.get_competition(league_code)
    )
    competition: Competition = await translate_competition_response_to_competition(
        competition_response
    )
    all_seasons = competition_response.seasons + [competition_response.current_season]
    team_list, player_list, coach_list = (
        await bulk_process_season_data_to_team_coach_player(all_seasons)
    )
    return "success"


async def process_get_import_league(league_code: str) -> str:
    """
    Process the import league request.

    It processes the import league request and returns the status of the request.

    Args:
        league_code: The league code.

    Returns:
        str: The status of the request.
    """
    task = asyncio.create_task(get_import_league(league_code))
    asyncio.gather(task)
    return "success"
