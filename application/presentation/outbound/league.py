from fastapi import APIRouter, HTTPException
from presentation.outbound.entities.league import LeagueResponse
from business_rules.services import league as league_service

league_router = APIRouter()


@league_router.get("/import-league")
async def import_league(league_code: str) -> LeagueResponse:
    try:
        process_status = await league_service.process_get_import_league(league_code)
        return LeagueResponse(
            status=process_status, message="League imported successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error importing league")
