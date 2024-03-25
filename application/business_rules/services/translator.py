from business_rules.entities.football import (
    CompetitionResponseTranslator,
    Competition,
    Coach,
    Team,
    Player,
)
from presentation.inbound.entities.competition import (
    CompetitionResponse,
)
from presentation.inbound.entities.team import TeamResponse
from typing import List


async def _build_coach_entity(
    team_response: TeamResponse,
) -> Coach:
    """
    Build a Coach entity.

    Args:
        team_response: A TeamResponse entity.

    Returns:
        A Coach entity.
    """
    return Coach(
        name=str(team_response.coach.firstName)
        + " "
        + str(team_response.coach.lastName),
        dateOfBirth=team_response.coach.dateOfBirth,
        nationality=team_response.coach.nationality,
    )


async def _build_player_entity(
    team_response: TeamResponse,
) -> Player:
    """
    Build a Player entity.

    Args:
        player_response: A PlayerResponse entity.

    Returns:
        A Player entity.
    """
    players = team_response.squad
    return [
        Player(
            name=player.name,
            position=player.position,
            dateOfBirth=player.dateOfBirth,
            nationality=team_response.area.name,
        )
        for player in players
    ]


async def _build_team_entity(
    team_response: TeamResponse,
) -> Team:
    """
    Build a Team entity.

    Args:
        team_response: A TeamResponse entity.

    Returns:
        A Team entity.
    """
    return Team(
        name=team_response.name,
        areaName=team_response.area.name,
        shortName=team_response.shortName,
        address=team_response.address,
    )


async def _build_competition_entity(
    competition_response: CompetitionResponse,
) -> Competition:
    """
    Build a Competition entity.

    Args:
        competition_response: A CompetitionResponse entity.

    Returns:
        A Competition entity.
    """
    return Competition(
        name=competition_response.name,
        code=competition_response.code,
        areaName=competition_response.area.name,
    )
