from tests.test_persistence.factories import (
    PlayerDataFactory,
    CoachDataFactory,
    TeamDataFactory,
    CompetitionDataFactory,
)
from persistence.entities.football import (
    PlayerData,
    CoachData,
    TeamData,
    CompetitionData,
)


class TestPlayerData:
    def test_player_data_entity_is_created(self):
        player_data = PlayerDataFactory()
        assert player_data.__class__ == PlayerData


class TestCoachData:
    def test_coach_data_entity_is_created(self):
        coach_data = CoachDataFactory()
        assert coach_data.__class__ == CoachData


class TestTeamData:
    def test_team_data_entity_is_created(self):
        team_data = TeamDataFactory()
        assert team_data.__class__ == TeamData


class TestCompetitionData:
    def test_competition_data_entity_is_created(self):
        competition_data = CompetitionDataFactory()
        assert competition_data.__class__ == CompetitionData
