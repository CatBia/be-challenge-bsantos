from persistence.repositories.competition import CompetitionRepository
from persistence.entities.football import CompetitionData
from persistence.adapters.mongodb import DatabaseManager


async def create_competition_data(
    database_manager: DatabaseManager, competition_data: CompetitionData
) -> CompetitionData:
    created_objetcs = await database_manager.competition_repo.create_competition_by_competition_object(
        competition_object=competition_data
    )
    return database_manager
