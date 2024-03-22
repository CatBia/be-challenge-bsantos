from business_rules.services.translator import (
    _build_competition_entity,
    _build_team_entity,
    _build_player_entity,
    _build_coach_entity,
)
from business_rules.entities.football import Competition, Team, Player, Coach
from tests.test_business_rules.test_entities.factories import CompetitionFactory
from presentation.inbound.entities.competition import CompetitionResponse
from tests.test_presentation.test_inbound.factories import (
    CompetitionResponseFactory,
    TeamResponseFactory,
)
import pytest


class TestBuildCompetitionEntity:
    @pytest.mark.asyncio
    async def test_build_competition_entity(self):
        """
        Test case to verify that a Competition entity is built correctly.

        It builds a Competition entity using the _build_competition_entity method and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        any_competition_response = CompetitionResponseFactory()
        any_competition = await _build_competition_entity(any_competition_response)
        assert any_competition.__class__ == Competition
        assert any_competition.name == any_competition_response.name
        assert any_competition.code == any_competition_response.code
        assert any_competition.areaName == any_competition_response.area.name


class TestBuildTeamEntity:
    @pytest.mark.asyncio
    async def test_build_team_entity(self):
        """
        Test case to verify that a Team entity is built correctly.

        It builds a Team entity using the _build_team_entity method and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        any_team_response = TeamResponseFactory()
        any_team = await _build_team_entity(any_team_response)
        assert any_team.__class__ == Team
        assert any_team.name == any_team_response.name
        assert any_team.areaName == any_team_response.area.name
        assert any_team.shortName == any_team_response.shortName
        assert any_team.address == any_team_response.address


class TestBuildPlayerEntity:
    @pytest.mark.asyncio
    async def test_build_player_entity(self):
        """
        Test case to verify that a Player entity is built correctly.

        It builds a Player entity using the _build_player_entity method and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        any_team_response = TeamResponseFactory()
        any_player = await _build_player_entity(any_team_response)
        assert isinstance(any_player, list)
        for player in any_player:
            assert player.__class__ == Player


class TestBuildCoachEntity:
    @pytest.mark.asyncio
    async def test_build_coach_entity(self):
        """
        Test case to verify that a Coach entity is built correctly.

        It builds a Coach entity using the _build_coach_entity method and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        any_team_response = TeamResponseFactory()
        any_coach = await _build_coach_entity(any_team_response)
        assert any_coach.__class__ == Coach
        assert (
            any_coach.name
            == any_team_response.coach.firstName
            + " "
            + any_team_response.coach.lastName
        )
        assert any_coach.dateOfBirth == any_team_response.coach.dateOfBirth
        assert any_coach.nationality == any_team_response.coach.nationality
