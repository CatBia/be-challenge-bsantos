import factory
from business_rules.entities.football import Competition, Team, Player, Coach


class CompetitionFactory(factory.Factory):
    class Meta:
        model = Competition

    name = factory.Faker("name")
    code = factory.Faker("country_code")
    areaName = factory.Faker("name")


class TeamFactory(factory.Factory):
    class Meta:
        model = Team

    name = factory.Faker("name")
    areaName = factory.Faker("name")
    shortName = factory.Faker("name")
    address = factory.Faker("address")


class PlayerFactory(factory.Factory):
    class Meta:
        model = Player

    name = factory.Faker("name")
    position = factory.Faker("job")
    dateOfBirth = factory.Faker("date")
    nationality = factory.Faker("country")


class CoachFactory(factory.Factory):
    class Meta:
        model = Coach

    name = factory.Faker("name")
    dateOfBirth = factory.Faker("date")
    nationality = factory.Faker("country")
