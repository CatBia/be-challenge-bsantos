import factory
from presentation.inbound.entities.competition import (
    CompetitionRequest,
    AreaResponse,
    WinnerResponse,
    SeasonResponse,
    CompetitionResponse,
)
from presentation.inbound.entities.team import (
    TeamResponse,
    PlayerResponse,
    CompetitionTeamResponse,
    CoachResponse,
    ContractResponse,
    TeamRequest,
)


class CompetitionRequestFactory(factory.Factory):
    class Meta:
        model = CompetitionRequest

    football_uri = factory.Faker("url")
    x_api_token = factory.Faker("uuid4")
    competition_endpoint = factory.Faker("pystr")


class AreaResponseFactory(factory.Factory):
    class Meta:
        model = AreaResponse

    id = factory.Faker("random_int")
    name = factory.Faker("name")
    code = factory.Faker("country_code")
    flag = factory.Faker("url")


class WinnerResponseFactory(factory.Factory):
    class Meta:
        model = WinnerResponse

    id = factory.Faker("random_int")
    name = factory.Faker("name")
    shortName = factory.Faker("name")
    tla = factory.Faker("name")
    crest = factory.Faker("url")
    address = factory.Faker("address")
    website = factory.Faker("url")
    founded = factory.Faker("random_int")
    clubColors = factory.Faker("color_name")
    venue = factory.Faker("name")
    lastUpdated = factory.Faker("date_time")


class SeasonResponseFactory(factory.Factory):
    class Meta:
        model = SeasonResponse

    id = factory.Faker("random_int")
    startDate = factory.Faker("date")
    endDate = factory.Faker("date")
    currentMatchday = factory.Faker("random_int")
    winner = factory.SubFactory(WinnerResponseFactory)
    venue = factory.Faker("name")
    lastUpdated = factory.Faker("date_time")


class CompetitionResponseFactory(factory.Factory):
    class Meta:
        model = CompetitionResponse

    id = factory.Faker("random_int")
    name = factory.Faker("name")
    code = factory.Faker("country_code")
    type = factory.Faker("name")
    emblem = factory.Faker("url")
    currentSeason = factory.SubFactory(SeasonResponseFactory)
    seasons = factory.List(
        [factory.SubFactory(SeasonResponseFactory) for _ in range(3)]
    )
    area = factory.SubFactory(AreaResponseFactory)
    lastUpdated = factory.Faker("date_time")


class PlayerResponseFactory(factory.Factory):
    class Meta:
        model = PlayerResponse

    id = factory.Faker("random_int")
    name = factory.Faker("name")
    position = factory.Faker("job")
    dateOfBirth = factory.Faker("date")
    nationality = factory.Faker("country")


class ContractResponseFactory(factory.Factory):
    class Meta:
        model = ContractResponse

    start = factory.Faker("date")
    until = factory.Faker("date")


class CompetitionTeamResponseFactory(factory.Factory):
    class Meta:
        model = CompetitionTeamResponse

    id = factory.Faker("random_int")
    name = factory.Faker("name")
    code = factory.Faker("country_code")
    areaName = factory.Faker("name")


class CoachResponseFactory(factory.Factory):
    class Meta:
        model = CoachResponse

    id = factory.Faker("random_int")
    firstName = factory.Faker("first_name")
    lastName = factory.Faker("last_name")
    dateOfBirth = factory.Faker("date")
    nationality = factory.Faker("country")
    contract = factory.SubFactory(ContractResponseFactory)


class TeamResponseFactory(factory.Factory):
    class Meta:
        model = TeamResponse

    id = factory.Faker("random_int")
    name = factory.Faker("name")
    shortName = factory.Faker("name")
    tla = factory.Faker("name")
    crest = factory.Faker("url")
    address = factory.Faker("address")
    website = factory.Faker("url")
    founded = factory.Faker("random_int")
    clubColors = factory.Faker("color_name")
    venue = factory.Faker("name")
    lastUpdated = factory.Faker("date_time")
    coach = factory.SubFactory(CoachResponseFactory)
    area = factory.SubFactory(AreaResponseFactory)
    staff = factory.LazyAttribute(lambda _: ["any"] * 3)
    squad = factory.List([factory.SubFactory(PlayerResponseFactory) for _ in range(5)])
    runningCompetitions = factory.List(
        [factory.SubFactory(CompetitionTeamResponseFactory) for _ in range(5)]
    )


class TeamRequestFactory(factory.Factory):
    class Meta:
        model = TeamRequest

    football_uri = factory.Faker("url")
    x_api_token = factory.Faker("uuid4")
    team_endpoint = factory.Faker("pystr")
