import pytest
import mock
from presentation.inbound.exceptions import TeamInboundError
from presentation.inbound.team import TeamInbound
from tests.test_presentation.test_inbound.factories import TeamResponseFactory
from presentation.inbound.entities.team import TeamResponse
import logging
from dataclasses import asdict


class TestTeamInbound:

    @pytest.mark.asyncio
    async def test_check_status_code(self):
        """
        Test case to check the status code of a team inbound request.

        This method verifies that the status code returned by the
        `_check_status_code` method of the `TeamInbound` class
        matches the expected status code.

        Args:
            None

        Returns:
            None
        """
        status = 200
        await TeamInbound._check_status_code(status)

    @pytest.mark.asyncio
    async def test_handle_team_response_raised_error(self, caplog):
        """
        Test case to verify that an error is raised when handling a team response.

        Args:
            caplog: The pytest fixture for capturing log messages.

        Raises:
            TeamInboundError: If an error occurs while handling the team response.

        """
        mock_response = mock.MagicMock()
        mock_response.status = 400
        mocked_check_status_code = mock.AsyncMock(side_effect=TeamInboundError)
        with mock.patch.object(
            TeamInbound, "_check_status_code", mocked_check_status_code
        ):
            with caplog.at_level(logging.ERROR):
                with pytest.raises(TeamInboundError):
                    await TeamInbound._handle_team_response(mock_response)

                assert "Error fetching" in caplog.text
                mocked_check_status_code.assert_called_once_with(mock_response.status)

    @pytest.mark.asyncio
    async def test_handle_team_response(self):
        """
        Test case to verify that a team response is handled correctly.

        Args:
            None

        Returns:
            None
        """
        mock_response = mock.MagicMock()
        mock_response.status = 200
        team_response = TeamResponseFactory()
        mocked_check_status_code = mock.AsyncMock()
        with mock.patch.object(
            TeamInbound, "_check_status_code", mocked_check_status_code
        ):
            mock_response.json = mock.AsyncMock(return_value=asdict(team_response))
            response = await TeamInbound._handle_team_response(mock_response)
            assert response.__class__ == TeamResponse
            mocked_check_status_code.assert_called_once_with(mock_response.status)

    @pytest.mark.asyncio
    async def tests_build_team_get_request_dict(self):
        """
        Test case to verify that a team get request dictionary is built correctly.

        Args:
            None

        Returns:
            None
        """
        team_id = "Any team id"
        team_inbound = TeamInbound()
        team_request_dict = await team_inbound._build_team_get_request_dict(team_id)
        assert team_request_dict["url"]
        assert team_request_dict["headers"]["X-Auth-Token"]

    @pytest.mark.asyncio
    async def test_get_team_response(self, valid_team_api_response):
        """
        Test case for the get_team_response method.

        This method tests the functionality of the get_team_response method in the TeamInbound class.
        It verifies that the returned team response is an instance of the TeamResponse class.

        Args:
            valid_team_response: A fixture that provides a valid team response.

        Returns:
            None
        """
        team_id = "Any team id"
        team_inbound = TeamInbound()
        team_response = await team_inbound.get_team(team_id)
        assert team_response.__class__ == TeamResponse

    @pytest.mark.asyncio
    async def test_get_comppetition_valid_response_calls(self, valid_team_api_response):
        """
        Test case to verify that the get_team method makes the correct calls.

        Args:
            None

        Returns:
            None
        """

        team_id = "Any team id"

        mocked_handle_team_response = mock.AsyncMock(return_value=TeamResponseFactory())
        team_inbound = TeamInbound()
        with mock.patch.object(
            TeamInbound,
            "_handle_team_response",
            mocked_handle_team_response,
        ):
            await team_inbound.get_team(team_id)
            mocked_handle_team_response.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_comppetition_invalid_response_calls(
        self, invalid_team_api_response
    ):
        """
        Test case to verify that the get_team method makes the correct calls.

        Args:
            None

        Returns:
            None
        """

        team_id = "Any team id"

        mocked_handle_team_response = mock.AsyncMock(return_value=TeamResponseFactory())
        team_inbound = TeamInbound()
        with mock.patch.object(
            TeamInbound,
            "_handle_team_response",
            mocked_handle_team_response,
        ):
            await team_inbound.get_team(team_id)
            mocked_handle_team_response.assert_called_once()
