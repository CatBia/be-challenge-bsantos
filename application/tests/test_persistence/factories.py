import factory
from persistence.entities.football import (
    PlayerData,
    CoachData,
    CompetitionData,
    TeamData,
)


class PlayerDataFactory(factory.Factory):
    class Meta:
        model = PlayerData

    name = factory.Faker("name")
    dateOfBirth = factory.Faker("date")
    nationality = factory.Faker("country")
    position = factory.Faker("pystr")


class CoachDataFactory(factory.Factory):
    class Meta:
        model = CoachData

    name = factory.Faker("name")
    dateOfBirth = factory.Faker("date")
    nationality = factory.Faker("country")


class TeamDataFactory(factory.Factory):
    class Meta:
        model = TeamData

    name = factory.Faker("name")
    areaName = factory.Faker("pystr")
    shortName = factory.Faker("name")
    address = factory.Faker("address")
    players = factory.List([factory.SubFactory(PlayerDataFactory) for _ in range(5)])
    coach = factory.SubFactory(CoachDataFactory)


class CompetitionDataFactory(factory.Factory):
    class Meta:
        model = CompetitionData

    name = factory.Faker("name")
    code = factory.Faker("pystr")
    areaName = factory.Faker("pystr")
    teams = factory.List([factory.SubFactory(TeamDataFactory) for _ in range(5)])
