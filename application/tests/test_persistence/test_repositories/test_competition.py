from tests.test_persistence.factories import CompetitionDataFactory
from persistence.repositories.competition import CompetitionRepository
from persistence.repositories.exceptions import CompetitionDoesNotExists
import pytest
from persistence.entities.football import CompetitionData, TeamData


class TestCompetitionRepository:
    @pytest.mark.asyncio
    async def test_get_several_competition_by_query_raised(self, db_session):
        repo = CompetitionRepository(db_client=db_session.client[db_session.database])
        with pytest.raises(CompetitionDoesNotExists):
            response = await repo.get_several_competition_by_query({})
            print(111)

    @pytest.mark.asyncio
    async def test_get_several_competition_by_query_one_item(
        self, db_session, build_one_competition_data
    ):
        repo = CompetitionRepository(db_client=db_session.client[db_session.database])
        response = await repo.get_several_competition_by_query({})
        assert isinstance(response, list)
        assert len(response) == 1
        assert response[0].name == build_one_competition_data.name
        assert response[0].areaName == build_one_competition_data.areaName

    @pytest.mark.asyncio
    async def test_get_several_competition_by_query_ten_item(
        self, db_session, build_ten_competition_data
    ):
        repo = CompetitionRepository(db_client=db_session.client[db_session.database])
        response = await repo.get_several_competition_by_query({})
        assert isinstance(response, list)
        assert len(response) == 10

    @pytest.mark.asyncio
    async def test_create_competition_by_competition_object_one_obj(self, db_session):
        competition_data = CompetitionDataFactory()
        repo = CompetitionRepository(db_client=db_session.client[db_session.database])
        received_data = await repo.create_competition_by_competition_object(
            competition_object=competition_data
        )
        assert received_data.__class__ == CompetitionData
        assert received_data.name == competition_data.name
        assert received_data.areaName == competition_data.areaName
        assert received_data.code == competition_data.code
        assert isinstance(received_data.teams, list)
        assert len(received_data.teams) == len(competition_data.teams)
        assert received_data.teams == competition_data.teams

    @pytest.mark.asyncio
    async def test_create_many_competition_by_competition_object_one_obj(
        self, db_session
    ):
        competition_data_list = CompetitionDataFactory.create_batch(10)
        repo = CompetitionRepository(db_client=db_session.client[db_session.database])
        received_data = await repo.create_many_competition_by_competition_object(
            competition_object_list=competition_data_list
        )
        assert isinstance(received_data, list)
        assert len(competition_data_list) == len(received_data)
        for competition_data in competition_data_list:
            assert competition_data.__class__ == CompetitionData
        assert set([cd.name for cd in competition_data_list]) == set(
            [data.name for data in received_data]
        )
