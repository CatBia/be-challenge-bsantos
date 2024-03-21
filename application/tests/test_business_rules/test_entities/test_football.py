import pytest
from business_rules.entities.football import Competition, Team, Player, Coach
from tests.test_business_rules.test_entities.factories import (
    CompetitionFactory,
    TeamFactory,
    PlayerFactory,
    CoachFactory,
)


class TestCompetition:
    def test_competition_entity_is_created(self):
        """
        Test case to verify that a Competition entity is created correctly.

        It creates a Competition entity using the CompetitionFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        name = "Any name"
        code = "ABC"
        areaName = "Any area"
        any_competition = CompetitionFactory(name=name, code=code, areaName=areaName)
        assert any_competition.__class__ == Competition
        assert any_competition.name == name
        assert any_competition.code == code
        assert any_competition.areaName == areaName


class TestTeam:
    def test_team_entity_is_created(self):
        """
        Test case to verify that a Team entity is created correctly.

        It creates a Team entity using the TeamFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        name = "Any name"
        areaName = "Any area"
        shortName = "Any short name"
        address = "Any address"
        any_team = TeamFactory(
            name=name, areaName=areaName, shortName=shortName, address=address
        )
        assert any_team.__class__ == Team
        assert any_team.name == name
        assert any_team.areaName == areaName
        assert any_team.shortName == shortName
        assert any_team.address == address


class TestPlayer:
    def test_player_entity_is_created(self):
        """
        Test case to verify that a Player entity is created correctly.

        It creates a Player entity using the PlayerFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        name = "Any name"
        position = "Any position"
        dateOfBirth = "Any date of birth"
        any_player = PlayerFactory(
            name=name, position=position, dateOfBirth=dateOfBirth
        )
        assert any_player.__class__ == Player
        assert any_player.name == name
        assert any_player.position == position
        assert any_player.dateOfBirth == dateOfBirth


class TestCoach:
    def test_coach_entity_is_created(self):
        """
        Test case to verify that a Coach entity is created correctly.

        It creates a Coach entity using the CoachFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        name = "Any name"
        dateOfBirth = "Any date"
        nationality = "Any Nationality"

        any_coach = CoachFactory(
            name=name,
            dateOfBirth=dateOfBirth,
            nationality=nationality,
        )

        assert any_coach.__class__ == Coach
        assert any_coach.name == name
        assert any_coach.dateOfBirth == dateOfBirth
        assert any_coach.nationality == nationality
