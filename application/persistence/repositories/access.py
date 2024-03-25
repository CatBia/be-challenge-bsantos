from abc import ABC, abstractmethod
from persistence.entities.access import Access
from persistence.repositories.exceptions import AccessNotFound
from datetime import datetime, timedelta
from typing import List


class AccessManager(ABC):
    @abstractmethod
    async def get_access_by_query(
        self,
    ) -> Access:
        pass

    async def create(
        self,
    ) -> Access:
        pass


class AccessRepository(AccessManager):
    collecion_name = "Access"

    def __init__(self, db_client) -> None:
        self.collecion = db_client[self.collecion_name]

    async def get_access_by_query(self, query: dict) -> Access:
        cursor = self.collecion.find(query)
        documents = await cursor.to_list(length=None)
        if not documents:
            raise AccessNotFound()
        return [Access(**document) for document in documents]

    async def get_last_1_min_acces(self) -> List[Access]:
        ten_minutes_ago = datetime.now() - timedelta(minutes=1)
        return self.get_access_by_query(
            {"datetime": {"$gte": ten_minutes_ago.isoformat()}}
        )

    async def create(self) -> None:
        access = Access(datetime=datetime.now().isoformat())
        await self.collecion.insert_one(access.model_dump())
