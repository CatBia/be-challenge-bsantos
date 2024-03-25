from presentation.inbound.entities.team import (
    TeamResponse,
    PlayerResponse,
    CompetitionTeamResponse,
    CoachResponse,
    ContractResponse,
    TeamRequest,
)
import factory
from tests.test_presentation.test_inbound.factories import (
    TeamResponseFactory,
    PlayerResponseFactory,
    CompetitionTeamResponseFactory,
    CoachResponseFactory,
    ContractResponseFactory,
    AreaResponseFactory,
    TeamRequestFactory,
    RunningCompetitionTeamResponseFactory,
)


class TestPlayerResponse:
    def test_player_response_entity_is_created(self):
        """
        Test case to verify that a PlayerResponse entity is created correctly.

        It creates a PlayerResponse entity using the PlayerResponseFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        id = 1
        name = "Any name"
        position = "Any position"
        dateOfBirth = "Any date"
        any_player_response = PlayerResponseFactory(
            id=id, name=name, position=position, dateOfBirth=dateOfBirth
        )
        assert any_player_response.__class__ == PlayerResponse


class TestContractResponse:
    def test_contract_response_entity_is_created(self):
        """
        Test case to verify that a ContractResponse entity is created correctly.

        It creates a ContractResponse entity using the ContractResponseFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        start = "Any start"
        until = "Any until"
        any_contract_response = ContractResponseFactory(start=start, until=until)
        assert any_contract_response.__class__ == ContractResponse


class TestCompetitionTeamResponse:
    def test_competition_team_response_entity_is_created(self):
        """
        Test case to verify that a CompetitionTeamResponse entity is created correctly.

        It creates a CompetitionTeamResponse entity using the CompetitionTeamResponseFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        id = 1
        name = "Any name"
        code = "Any code"
        areaName = "Any area name"
        any_competition_team_response = CompetitionTeamResponseFactory(
            id=id, name=name, code=code, areaName=areaName
        )
        assert any_competition_team_response.__class__ == CompetitionTeamResponse


class TestCoachResponse:
    def test_coach_response_entity_is_created(self):
        """
        Test case to verify that a CoachResponse entity is created correctly.

        It creates a CoachResponse entity using the CoachResponseFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        id = 1
        firstName = "Any first name"
        lastName = "Any last name"
        dateOfBirth = "Any date"
        nationality = "Any nationality"
        contract = ContractResponseFactory()
        coach = CoachResponseFactory(
            firstName=firstName,
            lastName=lastName,
            dateOfBirth=dateOfBirth,
            nationality=nationality,
            contract=contract,
        )
        assert coach.__class__ == CoachResponse


class TestTeamResponse:
    id = 1
    name = "Any name"
    shortName = "Any short name"
    tla = "Any tla"
    crest = "Any crest"
    address = "Any address"
    website = "Any website"
    founded = 1
    clubColors = "Any club colors"
    venue = "Any venue"
    lastUpdated = "Any last updated"
    coach = CoachResponseFactory()
    area = AreaResponseFactory()
    squad = [PlayerResponseFactory() for _ in range(3)]
    runningCompetitions = [RunningCompetitionTeamResponseFactory() for _ in range(3)]
    any_team_response = TeamResponseFactory(
        id=id,
        name=name,
        shortName=shortName,
        tla=tla,
        crest=crest,
        address=address,
        website=website,
        founded=founded,
        clubColors=clubColors,
        venue=venue,
        lastUpdated=lastUpdated,
        coach=coach,
        area=area,
        squad=squad,
        runningCompetitions=runningCompetitions,
    )
    assert any_team_response.__class__ == TeamResponse


class TestTeamRequest:
    def test_team_request_entity_is_created(self):
        """
        Test case to verify that a TeamRequest entity is created correctly.

        It creates a TeamRequest entity using the TeamRequestFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        football_uri = "Any football uri"
        x_api_token = "Any x api token"
        team_endpoint = "Any team endpoint"
        any_team_request = TeamRequestFactory(
            football_uri=football_uri,
            x_api_token=x_api_token,
            team_endpoint=team_endpoint,
        )
        assert any_team_request.__class__ == TeamRequest

    def test_get_request_dict(self):
        """
        Test case to verify that the get_request_dict method of the TeamRequest entity returns the correct dictionary.

        It creates a TeamRequest entity using the TeamRequestFactory and asserts that the get_request_dict method
        returns the correct dictionary.

        Args:
            self: The test case object.

        Returns:
            None
        """
        football_uri = "Any football uri"
        x_api_token = "Any x api token"
        team_endpoint = "Any team endpoint"
        team_id = "Any team id"
        any_team_request = TeamRequestFactory(
            football_uri=football_uri,
            x_api_token=x_api_token,
            team_endpoint=team_endpoint,
        )
        expected_dict = {
            "url": f"{football_uri}/{team_endpoint}/{team_id}",
            "headers": {"X-Auth-Token": x_api_token},
        }
        assert isinstance(any_team_request.get_request_dict(team_id), dict)
        assert any_team_request.get_request_dict(team_id) == expected_dict
