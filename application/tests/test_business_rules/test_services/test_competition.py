from business_rules.services import competition as competition_service
from settings import configuration
from tests.test_presentation.test_inbound.factories import CompetitionResponseFactory

import mock
import pytest


class TestGetCompetition:
    @pytest.mark.asyncio
    async def test_get_team_success(self):
        competition_response = CompetitionResponseFactory()

        class MockedInbound:
            def __init__(self, config):
                pass

            async def get_competition(self, team_id):
                return competition_response

        with mock.patch(
            "business_rules.services.competition.CompetitionInbound", MockedInbound
        ):
            competition_code = "1"
            response = await competition_service.get_competition(competition_code)
            assert response == competition_response

    @pytest.mark.asyncio
    async def test_get_team_get_team_inbound_called(self):
        with mock.patch(
            "business_rules.services.competition.CompetitionInbound",
            new_callable=mock.MagicMock,
        ) as mock_inbound:
            mock_inbound.return_value.get_competition = mock.AsyncMock()
            await competition_service.get_competition("1")
            assert mock_inbound.return_value.get_competition.called
