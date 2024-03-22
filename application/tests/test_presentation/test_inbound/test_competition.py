import pytest
import mock
from presentation.inbound.exceptions import CompetitionInboundError
from presentation.inbound.competition import CompetitionInbound
from tests.test_presentation.test_inbound.factories import CompetitionResponseFactory
from presentation.inbound.entities.competition import CompetitionResponse
import logging
from dataclasses import asdict


class FakeConfiguration:
    FOOTBALL_URI = "Any football uri"
    FOOTBALL_COMPETITION_ENDPOINT = "any competitions"
    X_API_TOKEN = "Any x api token"
    FOOTBALL_TEAM_ENDPOINT = "any teams"


class TestCompetitionInbound:

    @pytest.mark.asyncio
    async def test_check_status_code(self):
        """
        Test case to check the status code of a competition inbound request.

        This method verifies that the status code returned by the
        `_check_status_code` method of the `CompetitionInbound` class
        matches the expected status code.

        Args:
            None

        Returns:
            None
        """
        status = 200
        await CompetitionInbound._check_status_code(status)

    @pytest.mark.asyncio
    async def test_handle_competition_response_raised_error(self, caplog):
        """
        Test case to verify that an error is raised when handling a competition response.

        Args:
            caplog: The pytest fixture for capturing log messages.

        Raises:
            CompetitionInboundError: If an error occurs while handling the competition response.

        """
        mock_response = mock.MagicMock()
        mock_response.status = 400
        mocked_check_status_code = mock.AsyncMock(side_effect=CompetitionInboundError)
        with mock.patch.object(
            CompetitionInbound, "_check_status_code", mocked_check_status_code
        ):
            with caplog.at_level(logging.ERROR):
                with pytest.raises(CompetitionInboundError):
                    await CompetitionInbound._handle_competition_response(mock_response)

                assert "Error fetching" in caplog.text
                mocked_check_status_code.assert_called_once_with(mock_response.status)

    @pytest.mark.asyncio
    async def test_handle_competition_response(self):
        """
        Test case to verify that a competition response is handled correctly.

        Args:
            None

        Returns:
            None
        """
        mock_response = mock.MagicMock()
        mock_response.status = 200
        competition_response = CompetitionResponseFactory()
        mocked_check_status_code = mock.AsyncMock()
        with mock.patch.object(
            CompetitionInbound, "_check_status_code", mocked_check_status_code
        ):
            mock_response.json = mock.AsyncMock(
                return_value=asdict(competition_response)
            )
            response = await CompetitionInbound._handle_competition_response(
                mock_response
            )
            assert response.__class__ == CompetitionResponse
            mocked_check_status_code.assert_called_once_with(mock_response.status)

    @pytest.mark.asyncio
    async def tests_build_competition_get_request_dict(self):
        """
        Test case to verify that a competition get request dictionary is built correctly.

        Args:
            None

        Returns:
            None
        """
        league_code = "Any competition id"
        competition_inbound = CompetitionInbound(FakeConfiguration)
        competition_request_dict = (
            await competition_inbound._build_competition_get_request_dict(league_code)
        )
        assert competition_request_dict == {
            "url": "Any football uri/any competitions/Any competition id",
            "headers": {"X-Auth-Token": "Any x api token"},
        }

    @pytest.mark.asyncio
    async def test_get_competition_response(self, valid_competition_api_response):
        """
        Test case for the get_competition_response method.

        This method tests the functionality of the get_competition_response method in the CompetitionInbound class.
        It verifies that the returned competition response is an instance of the CompetitionResponse class.

        Args:
            valid_competition_response: A fixture that provides a valid competition response.

        Returns:
            None
        """
        league_code = "Any competition id"
        competition_inbound = CompetitionInbound(FakeConfiguration)
        competition_response = await competition_inbound.get_competition(league_code)
        assert competition_response.__class__ == CompetitionResponse

    @pytest.mark.asyncio
    async def test_get_comppetition_valid_response_calls(
        self, valid_competition_api_response
    ):
        """
        Test case to verify that the get_competition method makes the correct calls.

        Args:
            None

        Returns:
            None
        """

        league_code = "Any competition id"

        mocked_handle_competition_response = mock.AsyncMock(
            return_value=CompetitionResponseFactory()
        )
        competition_inbound = CompetitionInbound(FakeConfiguration)
        with mock.patch.object(
            CompetitionInbound,
            "_handle_competition_response",
            mocked_handle_competition_response,
        ):
            await competition_inbound.get_competition(league_code)
            mocked_handle_competition_response.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_comppetition_invalid_response_calls(
        self, invalid_competition_api_response
    ):
        """
        Test case to verify that the get_competition method makes the correct calls.

        Args:
            None

        Returns:
            None
        """

        league_code = "Any competition id"

        mocked_handle_competition_response = mock.AsyncMock(
            return_value=CompetitionResponseFactory()
        )
        competition_inbound = CompetitionInbound(FakeConfiguration)
        with mock.patch.object(
            CompetitionInbound,
            "_handle_competition_response",
            mocked_handle_competition_response,
        ):
            await competition_inbound.get_competition(league_code)
            mocked_handle_competition_response.assert_called_once()
