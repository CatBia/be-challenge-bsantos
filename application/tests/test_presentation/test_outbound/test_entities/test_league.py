from tests.test_presentation.test_outbound.factories import LeagueResponseFactory
from presentation.outbound.entities.league import LeagueResponse
import pytest


class TestLeagueResponse:
    @pytest.mark.parametrize(
        "status, message",
        [
            ("success", "League imported successfully"),
            ("error", "Error importing league"),
        ],
    )
    def test_league_response_entity_is_created(self, status, message):
        """
        Test case to verify that a LeagueResponse entity is created correctly.

        It creates a LeagueResponse entity using the LeagueResponseFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        any_league_response = LeagueResponseFactory(status=status, message=message)
        assert any_league_response.__class__ == LeagueResponse
        assert any_league_response.status == status
        assert any_league_response.message == message
