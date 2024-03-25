from fastapi import APIRouter, HTTPException, Depends
from persistence.adapters.base import DatabaseManager
from persistence.adapters.mongodb import get_database
from business_rules.services import team as team_service
from typing import Optional

teams_router = APIRouter()


@teams_router.get("/teams")
async def get_teams(
    team_name: str,
    has_coach: Optional[str] = None,
    has_players: Optional[str] = None,
    database_manager: DatabaseManager = Depends(get_database),
):
    try:
        teams = await team_service.get_team_data_by_team_name(
            database_manager,
            team_name,
            has_coach=True if has_coach else False,
            has_players=True if has_players else False,
        )
        return teams

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error getting ")
