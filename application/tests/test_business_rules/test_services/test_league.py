import pytest
from business_rules.services import league as league_service
from tests.test_presentation.test_inbound.factories import (
    SeasonResponseFactory,
    TeamResponseFactory,
    PlayerResponseFactory,
    CoachResponseFactory,
)
import mock
import asyncio


class TestGetTeamBySeasonData:
    @pytest.mark.asyncio
    async def test_get_team_by_season_data_get_team_service_called(self):
        """
        Test case to verify if the get_team_by_season_data function calls the get_team service method.
        """
        season = SeasonResponseFactory()
        mock_team_service = mock.MagicMock()
        mock_team_service.get_team = mock.AsyncMock(return_value=TeamResponseFactory())
        with mock.patch(
            "business_rules.services.league.team_service", mock_team_service
        ):
            await league_service.get_team_by_season_data(season)
            assert mock_team_service.get_team.called


class TestTranslateTeamResponseToPlayer:
    @pytest.mark.asyncio
    async def test_translate_team_response_to_player_called(self):
        """
        Test case to verify if the _build_player_entity method of the translator service is called
        when translating a team response to a player.
        """
        team_response = TeamResponseFactory()
        mock_translator_service = mock.MagicMock()
        mock_translator_service._build_player_entity = mock.AsyncMock()
        with mock.patch(
            "business_rules.services.league.translator_service", mock_translator_service
        ):
            await league_service.translate_team_response_to_player(team_response)
            assert mock_translator_service._build_player_entity.called


class TestTranslateTeamResponseToCoach:
    @pytest.mark.asyncio
    async def test_translate_team_response_to_coach_called():
        """
        Test case to verify if the _build_coach_entity method of the translator service is called
        when translating a team response to a coach entity.
        """
        team_response = TeamResponseFactory()
        mock_translator_service = mock.MagicMock()
        mock_translator_service._build_coach_entity = mock.AsyncMock()
        with mock.patch(
            "business_rules.services.league.translator_service", mock_translator_service
        ):
            await league_service.translate_team_response_to_coach(team_response)
            assert mock_translator_service._build_coach_entity.called


class TestTranslateTeamResponseToTeam:
    @pytest.mark.asyncio
    async def test_translate_team_response_to_team_called(self):
        """
        Test case to verify if the _build_team_entity method of the translator service is called
        when translating a team response to a team entity.
        """
        team_response = TeamResponseFactory()
        mock_translator_service = mock.MagicMock()
        mock_translator_service._build_team_entity = mock.AsyncMock()
        with mock.patch(
            "business_rules.services.league.translator_service", mock_translator_service
        ):
            await league_service.translate_team_response_to_team(team_response)
            assert mock_translator_service._build_team_entity.called


class TestTranslateCompetitionResponseToCompetition:
    @pytest.mark.asyncio
    async def test_translate_competition_response_to_competition_called(self):
        """
        Test case to verify if the _build_competition_entity method of the translator service is called
        when translating a competition response to a competition entity.
        """
        competition_response = TeamResponseFactory()
        mock_translator_service = mock.MagicMock()
        mock_translator_service._build_competition_entity = mock.AsyncMock()
        with mock.patch(
            "business_rules.services.league.translator_service", mock_translator_service
        ):
            await league_service.translate_competition_response_to_competition(
                competition_response
            )
            assert mock_translator_service._build_competition_entity.called


class TestProcessSeasonDataToTeamCoachPlayer:
    @pytest.mark.asyncio
    async def test_process_season_data_to_team_coach_player_called(self):
        """
        Test case to verify if the process_season_data_to_team_coach_player method is called with the correct arguments.
        """
        season = SeasonResponseFactory()
        mock_get_team_by_season_data = mock.AsyncMock()
        mock_get_team_by_season_data.return_value = TeamResponseFactory()
        mock_translate_team_response_to_team = mock.AsyncMock()
        mock_translate_team_response_to_team.return_value = TeamResponseFactory()
        mock_translate_team_response_to_player = mock.AsyncMock()
        mock_translate_team_response_to_player.return_value = TeamResponseFactory()
        mock_translate_team_response_to_coach = mock.AsyncMock()
        mock_translate_team_response_to_coach.return_value = TeamResponseFactory()
        with mock.patch(
            "business_rules.services.league.get_team_by_season_data",
            mock_get_team_by_season_data,
        ):
            with mock.patch(
                "business_rules.services.league.translate_team_response_to_team",
                mock_translate_team_response_to_team,
            ):
                with mock.patch(
                    "business_rules.services.league.translate_team_response_to_player",
                    mock_translate_team_response_to_player,
                ):
                    with mock.patch(
                        "business_rules.services.league.translate_team_response_to_coach",
                        mock_translate_team_response_to_coach,
                    ):
                        await league_service._process_season_data_to_team_coach_player(
                            season
                        )
                        assert mock_get_team_by_season_data.called
                        assert mock_translate_team_response_to_team.called
                        assert mock_translate_team_response_to_player.called
                        assert mock_translate_team_response_to_coach.called


class TestBulkProcessSeasonDataToTeamCoachPlayer:
    @pytest.mark.asyncio
    async def test_bulk_process_season_data_to_team_coach_player_called(self):
        """
        Test case for the bulk_process_season_data_to_team_coach_player method in the league service.

        This test verifies that the bulk_process_season_data_to_team_coach_player method correctly calls
        the _process_season_data_to_team_coach_player method with the expected number of seasons.

        It sets up a mock for the _process_season_data_to_team_coach_player method and asserts that it is
        called the correct number of times.

        Returns:
            None
        """
        CALLS = 3
        seasons = [SeasonResponseFactory()] * CALLS
        mock__process_season_data_to_team_coach_player = mock.AsyncMock()
        mock__process_season_data_to_team_coach_player.return_value = [
            [TeamResponseFactory()],
            [PlayerResponseFactory()],
            [CoachResponseFactory()],
        ]
        with mock.patch(
            "business_rules.services.league._process_season_data_to_team_coach_player",
            mock__process_season_data_to_team_coach_player,
        ):
            await league_service.bulk_process_season_data_to_team_coach_player(seasons)
            assert mock__process_season_data_to_team_coach_player.call_count == CALLS
