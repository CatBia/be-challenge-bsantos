import factory
from presentation.outbound.entities.league import LeagueResponse


class LeagueResponseFactory(factory.Factory):
    class Meta:
        model = LeagueResponse

    status = "success"
    message = "League imported successfully"
