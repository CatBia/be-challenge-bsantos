import pytest


class TestGetTeams:
    @pytest.mark.asyncio
    async def test_get_teams_200_no_player_no_coach(
        self, client, db_session, build_one_competition_data
    ):
        competition_data = build_one_competition_data
        league_code = competition_data.code
        team_name = competition_data.teams[0].name
        response = await client.get("/teams", params={"team_name": team_name})
        status_code = response.status_code
        assert status_code == 200
        content = response.json()
        assert len(content) == 5
        for team in content:
            assert team.get("players") is None
            assert team.get("coach") is None

    @pytest.mark.asyncio
    async def test_get_teams_200_player_and_coach(
        self, client, db_session, build_one_competition_data
    ):
        competition_data = build_one_competition_data
        league_code = competition_data.code
        team_name = competition_data.teams[0].name
        response = await client.get(
            "/teams", params={"team_name": team_name, "has_players": 1, "has_coach": 1}
        )
        status_code = response.status_code
        assert status_code == 200
        content = response.json()
        assert len(content) == 5
        for team in content:
            assert team.get("players") is not None
            assert team.get("coach") is not None

    @pytest.mark.asyncio
    async def test_get_teams_200_player_and_no_coach(
        self, client, db_session, build_one_competition_data
    ):
        competition_data = build_one_competition_data
        league_code = competition_data.code
        team_name = competition_data.teams[0].name
        response = await client.get(
            "/teams", params={"team_name": team_name, "has_players": 1}
        )
        status_code = response.status_code
        assert status_code == 200
        content = response.json()
        assert len(content) == 5
        for team in content:
            assert team.get("players") is not None
            assert team.get("coach") is None

    @pytest.mark.asyncio
    async def test_get_teams_200_coach_and_no_player(
        self, client, db_session, build_one_competition_data
    ):
        competition_data = build_one_competition_data
        league_code = competition_data.code
        team_name = competition_data.teams[0].name
        response = await client.get(
            "/teams", params={"team_name": team_name, "has_coach": 1}
        )
        status_code = response.status_code
        assert status_code == 200
        content = response.json()
        assert len(content) == 5
        for team in content:
            assert team.get("players") is None
            assert team.get("coach") is not None
