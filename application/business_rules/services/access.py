from persistence.repositories.access import AccessRepository
from persistence.adapters.mongodb import DatabaseManager


async def create_access(database_manager: DatabaseManager) -> None:
    await database_manager.acess_repo.create()


async def get_last_1_min_access(database_manager: DatabaseManager):
    return await database_manager.acess_repo.get_last_1_min_acces()


async def calls_remaining(database_manager: DatabaseManager):
    access = await get_last_1_min_access(database_manager)
    return 10 - len(access)
