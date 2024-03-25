from fastapi import APIRouter, HTTPException, Depends
from presentation.outbound.entities.league import LeagueResponse
from business_rules.services import league as league_service
from persistence.adapters.base import DatabaseManager
from persistence.adapters.mongodb import get_database

league_router = APIRouter()


@league_router.get("/import-league")
async def import_league(
    league_code: str, database_manager: DatabaseManager = Depends(get_database)
) -> LeagueResponse:
    try:
        process_status = await league_service.process_get_import_league(
            database_manager=database_manager, league_code=league_code
        )

        return LeagueResponse(
            status=process_status, message="League imported successfully"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error importing league")
