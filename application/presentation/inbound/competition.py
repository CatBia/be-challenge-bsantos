import aiohttp
from settings.configuration import Configuration
from presentation.inbound.entities.competition import (
    CompetitionRequest,
    CompetitionResponse,
)
from presentation.inbound.exceptions import CompetitionInboundError


class CompetitionInbound:
    @classmethod
    async def _check_status_code(cls, status: int) -> None:
        if status != 200:
            raise CompetitionInboundError(f"Error in the request: {status}")

    @classmethod
    async def _handle_competition_response(
        cls, response: aiohttp.ClientResponse
    ) -> CompetitionResponse:
        await cls._check_status_code(response.status)
        content = await response.json()
        return CompetitionResponse(**content)

    async def _build_competition_get_request_dict(self, league_code: str) -> dict:
        competition_request = CompetitionRequest(
            football_uri=Configuration.FOOTBALL_URI.value,
            x_api_token=Configuration.X_API_TOKEN.value,
            competition_endpoint=Configuration.FOOTBALL_COMPETITION_ENDPOINT.value,
        )
        return competition_request.get_request_dict(league_code)

    async def get_competition(self, league_code: str) -> CompetitionResponse:
        competition_request_dict = await self._build_competition_get_request_dict(
            league_code
        )
        async with aiohttp.ClientSession() as session:
            received_response = await session.get(**competition_request_dict)
            competition_response = await self._handle_competition_response(
                received_response
            )
            return competition_response
