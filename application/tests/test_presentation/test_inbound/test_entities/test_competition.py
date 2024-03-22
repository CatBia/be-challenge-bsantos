import pytest
import mock
from presentation.inbound.entities.competition import (
    CompetitionRequest,
    AreaResponse,
    WinnerResponse,
    SeasonResponse,
    CompetitionResponse,
)
from tests.test_presentation.test_inbound.factories import (
    CompetitionRequestFactory,
    AreaResponseFactory,
    WinnerResponseFactory,
    SeasonResponseFactory,
    CompetitionResponseFactory,
)


class TestCompetitionRequest:
    def test_competition_request_entity_is_created(self):
        """
        Test case to verify that a CompetitionRequest entity is created correctly.

        It creates a CompetitionRequest entity using the CompetitionRequestFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        football_uri = "Any football uri"
        x_api_token = "Any x api token"
        any_competition_request = CompetitionRequestFactory(
            football_uri=football_uri, x_api_token=x_api_token
        )
        assert any_competition_request.__class__ == CompetitionRequest
        assert any_competition_request.football_uri == football_uri
        assert any_competition_request.x_api_token == x_api_token

    def test_competition_request_get_request_dict(self):
        """
        Test case to verify that the get_request_dict method returns the correct dictionary.

        It creates a CompetitionRequest entity using the CompetitionRequestFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        football_uri = "Any football uri"
        x_api_token = "Any x api token"
        competition_endpoint = "Any competition endpoint"
        any_competition_request = CompetitionRequestFactory(
            football_uri=football_uri,
            x_api_token=x_api_token,
            competition_endpoint=competition_endpoint,
        )
        league_code = "Any competition id"
        expected_dict = {
            "url": f"{football_uri}/{competition_endpoint}/{league_code}",
            "headers": {"X-Auth-Token": x_api_token},
        }
        assert isinstance(any_competition_request.get_request_dict(league_code), dict)
        assert any_competition_request.get_request_dict(league_code) == expected_dict


class TestAreaResponse:
    def test_area_response_entity_is_created(self):
        """
        Test case to verify that an AreaResponse entity is created correctly.

        It creates an AreaResponse entity using the AreaResponseFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        id = 123
        name = "Any name"
        code = "ABC"
        flag = "Any flag"

        any_area_response = AreaResponseFactory(id=id, name=name, code=code, flag=flag)
        assert any_area_response.__class__ == AreaResponse
        assert any_area_response.id == id
        assert any_area_response.name == name
        assert any_area_response.code == code
        assert any_area_response.flag == flag


class TestWinnerResponse:
    def test_winner_response_entity_is_created(self):
        """
        Test case to verify that a WinnerResponse entity is created correctly.

        It creates a WinnerResponse entity using the WinnerResponseFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        id = 123
        name = "Any name"
        shortName = "Any short name"
        tla = "Any tla"
        crest = "Any crest"
        address = "Any address"
        website = "Any website"
        founded = 2021
        clubColors = "Any club colors"
        venue = "Any venue"
        lastUpdated = "2021-01-01T00:00:00Z"

        any_winner_response = WinnerResponseFactory(
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
        )
        assert any_winner_response.__class__ == WinnerResponse
        assert any_winner_response.id == id
        assert any_winner_response.name == name
        assert any_winner_response.shortName == shortName
        assert any_winner_response.tla == tla
        assert any_winner_response.crest == crest
        assert any_winner_response.address == address
        assert any_winner_response.website == website
        assert any_winner_response.founded == founded
        assert any_winner_response.clubColors == clubColors
        assert any_winner_response.venue == venue
        assert any_winner_response.lastUpdated == lastUpdated


class TestSeasonResponse:
    def test_season_response_entity_is_created(self):
        """
        Test case to verify that a SeasonResponse entity is created correctly.

        It creates a SeasonResponse entity using the SeasonResponseFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        id = 123
        startDate = "2021-01-01"
        endDate = "2021-12-31"
        currentMatchday = 1
        winner = WinnerResponseFactory()
        venue = "Any venue"
        lastUpdated = "2021-01-01T00:00:00Z"

        any_season_response = SeasonResponseFactory(
            id=id,
            startDate=startDate,
            endDate=endDate,
            currentMatchday=currentMatchday,
            winner=winner,
            venue=venue,
            lastUpdated=lastUpdated,
        )
        assert any_season_response.__class__ == SeasonResponse
        assert any_season_response.id == id
        assert any_season_response.startDate == startDate
        assert any_season_response.endDate == endDate
        assert any_season_response.currentMatchday == currentMatchday
        assert any_season_response.winner == winner
        assert any_season_response.venue == venue
        assert any_season_response.lastUpdated == lastUpdated


class TestCompetitionFactory:
    def test_competition_response_entity_is_created(self):
        """
        Test case to verify that a CompetitionResponse entity is created correctly.

        It creates a CompetitionResponse entity using the CompetitionResponseFactory and asserts that the created entity
        has the correct attributes.

        Args:
            self: The test case object.

        Returns:
            None
        """
        id = 123
        name = "Any name"
        code = "ABC"
        type = "Any type"
        emblem = "Any emblem"
        currentSeason = SeasonResponseFactory()
        seasons = [SeasonResponseFactory()] * 30
        area = AreaResponseFactory()
        lastUpdated = "2021-01-01T00:00:00Z"

        any_competition_response = CompetitionResponseFactory(
            id=id,
            name=name,
            code=code,
            type=type,
            emblem=emblem,
            currentSeason=currentSeason,
            seasons=seasons,
            area=area,
            lastUpdated=lastUpdated,
        )
        assert any_competition_response.__class__ == CompetitionResponse
        assert any_competition_response.id == id
        assert any_competition_response.name == name
        assert any_competition_response.code == code
        assert any_competition_response.type == type
        assert any_competition_response.emblem == emblem
        assert any_competition_response.currentSeason == currentSeason
        assert any_competition_response.seasons == seasons
        assert any_competition_response.area == area
        assert any_competition_response.lastUpdated == lastUpdated
