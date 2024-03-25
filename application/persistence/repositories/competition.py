from abc import ABC, abstractmethod
from typing import List, Optional
from persistence.repositories.exceptions import CompetitionDoesNotExists
from motor.motor_asyncio import AsyncIOMotorDatabase
from persistence.entities.football import CompetitionData


class CompetitionManager(ABC):
    @abstractmethod
    async def get_several_competition_by_query(
        self, query: dict
    ) -> List[CompetitionData]:
        pass


class CompetitionRepository(CompetitionManager):
    collection_name = "Competition"

    def __init__(self, db_client: AsyncIOMotorDatabase) -> None:
        self.collection = db_client[self.collection_name]

    async def get_several_competition_by_query(
        self, query: dict
    ) -> List[CompetitionData]:
        cursor = self.collection.find(query, {"_id": False})
        documents = await cursor.to_list(length=None)
        if not documents:
            raise CompetitionDoesNotExists()
        return [CompetitionData(**document) for document in documents]

    async def create_competition_by_competition_object(
        self, competition_object: CompetitionData
    ) -> CompetitionData:
        id_generated = await self.collection.insert_one(competition_object.model_dump())
        competition_created = await self.get_several_competition_by_query(
            {"_id": id_generated.inserted_id}
        )
        return competition_created[0]

    async def create_many_competition_by_competition_object(
        self, competition_object_list: List[CompetitionData]
    ) -> CompetitionData:
        id_generated = await self.collection.insert_many(
            [
                competition_object.model_dump()
                for competition_object in competition_object_list
            ]
        )
        return await self.get_several_competition_by_query(
            {"_id": {"$in": [id for id in id_generated.inserted_ids]}}
        )

    async def get_several_players_by_query(self, query):
        pipeline = [
            {"$match": query},
            {
                "$project": {
                    "_id": 0,
                    "players": "$teams.players",
                }
            },
            {"$unwind": "$players"},
        ]
        cursor = self.collection.aggregate(pipeline)
        documents = await cursor.to_list(length=None)
        players = []
        for document in documents:
            if document["players"]:
                players.extend(document["players"])
        return players

    async def get_several_players_team_by_query(self, team_name):
        pipeline = [
            {"$match": {"teams.name": team_name}},
            {"$project": {"teams": "$teams"}},
            {"$unwind": "$teams"},
            {"$match": {"teams.name": team_name}},
            {"$project": {"_id": 0, "players": "$teams.players"}},
            {"$unwind": "$players"},
        ]
        cursor = self.collection.aggregate(pipeline)
        documents = await cursor.to_list(length=None)
        players = []
        for document in documents:
            players.append(document["players"])
        return players

    async def get_several_teams_by_query(self, query, players: bool, coach: bool):
        project = {}
        if not players:
            project["teams.players"] = 0
        if not coach:
            project["teams.coach"] = 0

        pipeline = [
            {"$match": query},
            {
                "$project": {
                    "_id": 0,
                    "teams": "$teams",
                }
            },
            {"$unwind": "$teams"},
        ]
        if project:
            pipeline.append({"$project": project})
        cursor = self.collection.aggregate(pipeline)
        documents = await cursor.to_list(length=None)
        return [document["teams"] for document in documents]

    async def get_players_by_league_code(
        self, league_code: str, team_name: Optional[str] = None
    ):
        if team_name:
            return await self.get_several_players_by_query(
                {"code": league_code, "teams.name": team_name}
            )
        return await self.get_several_players_by_query({"code": league_code})

    async def get_players_by_team_name(self, team_name: str):
        return await self.get_several_players_team_by_query(team_name=team_name)

    async def get_teams_by_team_name(
        self, team_name: str, players: bool = False, coach: bool = False
    ):
        query = {"teams.name": team_name}
        return await self.get_several_teams_by_query(
            query=query, players=players, coach=coach
        )
