from fastapi import APIRouter, HTTPException, Depends
from persistence.adapters.base import DatabaseManager
from persistence.adapters.mongodb import get_database
from business_rules.services import players as players_service
from persistence.repositories.exceptions import PlayersNotFound

player_router = APIRouter()


@player_router.get("/players")
async def get_players(
    league_code: str,
    team_name: str = None,
    database_manager: DatabaseManager = Depends(get_database),
):
    try:
        players = await players_service.get_players(
            database_manager, league_code, team_name
        )
        return players

    except PlayersNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error getting players")


@player_router.get("/players/team")
async def get_players(
    team_name: str = None,
    database_manager: DatabaseManager = Depends(get_database),
):
    try:
        players = await players_service.get_players_team(database_manager, team_name)
        return players

    except PlayersNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error getting players")
