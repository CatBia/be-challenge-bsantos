from business_rules.services import team as team_service
from settings import configuration
from tests.test_presentation.test_inbound.factories import TeamResponseFactory

import mock
import pytest


class TestGetTeam:
    @pytest.mark.asyncio
    async def test_get_team_success(self):
        team_response = TeamResponseFactory()

        class MockedInbound:
            def __init__(self, config):
                pass

            async def get_team(self, team_id):
                return team_response

        with mock.patch("business_rules.services.team.TeamInbound", MockedInbound):
            team_id = "1"
            response = await team_service.get_team(team_id)
            assert response == team_response

    @pytest.mark.asyncio
    async def test_get_team_get_team_inbound_called(self):
        with mock.patch(
            "business_rules.services.team.TeamInbound", new_callable=mock.MagicMock
        ) as mock_inbound:
            mock_inbound.return_value.get_team = mock.AsyncMock()
            await team_service.get_team("1")
            assert mock_inbound.return_value.get_team.called
