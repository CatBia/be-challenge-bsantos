import aiohttp
from settings.configuration import Configuration
from presentation.inbound.entities.team import (
    TeamRequest,
    TeamResponse,
)
from presentation.inbound.exceptions import TeamInboundError


class TeamInbound:

    @classmethod
    async def _check_status_code(cls, status: int) -> None:
        if status != 200:
            raise TeamInboundError(f"Error in the request: {status}")

    @classmethod
    async def _handle_team_response(
        cls, response: aiohttp.ClientResponse
    ) -> TeamResponse:
        await cls._check_status_code(response.status)
        content = await response.json()
        return TeamResponse(**content)

    async def _build_team_get_request_dict(self, team_id: str) -> dict:
        team_request = TeamRequest(
            football_uri=Configuration.FOOTBALL_URI.value,
            x_api_token=Configuration.X_API_TOKEN.value,
            team_endpoint=Configuration.FOOTBALL_TEAM_ENDPOINT.value,
        )
        return team_request.get_request_dict(team_id)

    async def get_team(self, team_id: str) -> TeamResponse:
        team_request_dict = await self._build_team_get_request_dict(team_id)
        async with aiohttp.ClientSession() as session:
            received_response = await session.get(**team_request_dict)
            team_response = await self._handle_team_response(received_response)
            return team_response
