import pytest


class TestGetPlayers:
    @pytest.mark.asyncio
    async def test_get_players_200_ok_one_competition_with_team_and_players(
        self, client, db_session, build_one_competition_data
    ):
        competition_data = build_one_competition_data
        league_code = competition_data.code
        response = await client.get("/players", params={"league_code": league_code})
        status_code = response.status_code
        assert status_code == 200
        content = response.json()
        players = []
        for team in competition_data.teams:
            players.extend(team.players)
        for player in content:
            assert player["name"] in [player.name for player in players]

    @pytest.mark.asyncio
    async def test_get_players_200_ok_repeated_competition_with_team_and_players(
        self, client, db_session, build_repeated_competition_data
    ):
        competition_data = build_repeated_competition_data
        league_code = competition_data.code
        response = await client.get("/players", params={"league_code": league_code})
        status_code = response.status_code
        assert status_code == 200
        content = response.json()
        players = []
        for team in competition_data.teams:
            players.extend(team.players)
        for player in content:
            assert player["name"] in [player.name for player in players]

    @pytest.mark.asyncio
    async def test_get_players_404_repeated_competition_with_team_and_no_players(
        self, client, db_session, build_competition_data_noplayers
    ):
        competition_data = build_competition_data_noplayers
        league_code = competition_data.code
        response = await client.get("/players", params={"league_code": league_code})
        status_code = response.status_code
        assert status_code == 404
        content = response.json()
        assert content == {"detail": "Players Does Not Exists"}

    @pytest.mark.asyncio
    async def test_get_players_200_ok_one_competition_with_team_and_players_team_name(
        self, client, db_session, build_one_competition_data
    ):
        competition_data = build_one_competition_data
        league_code = competition_data.code
        team_name = competition_data.teams[0].name
        response = await client.get(
            "/players", params={"league_code": league_code, "team_name": team_name}
        )
        status_code = response.status_code
        assert status_code == 200
        content = response.json()
        players = []
        for team in competition_data.teams:
            players.extend(team.players)
        for player in content:
            assert player["name"] in [player.name for player in players]

    @pytest.mark.asyncio
    async def test_get_players_200_repeated_competition_with_team_and_players_team_name(
        self, client, db_session, build_repeated_competition_data
    ):
        competition_data = build_repeated_competition_data
        league_code = competition_data.code
        players = []
        team_name = competition_data.teams[0].name
        response = await client.get(
            "/players", params={"league_code": league_code, "team_name": team_name}
        )
        status_code = response.status_code
        assert status_code == 200
        content = response.json()
        for team in competition_data.teams:
            players.extend(team.players)
        for player in content:
            assert player["name"] in [player.name for player in players]

    @pytest.mark.asyncio
    async def test_get_players_404_ok_repeated_competition_with_team_and_no_players_team_name(
        self, client, db_session, build_competition_data_noplayers
    ):
        competition_data = build_competition_data_noplayers
        league_code = competition_data.code
        team_name = competition_data.teams[0].name
        response = await client.get(
            "/players", params={"league_code": league_code, "team_name": team_name}
        )
        status_code = response.status_code
        assert status_code == 404

    @pytest.mark.asyncio
    async def test_get_players_404_ok_repeated_competition_with_team_and_no_players_team_name(
        self, client, db_session, build_competition_data_noplayers
    ):
        competition_data = build_competition_data_noplayers
        league_code = competition_data.code
        team_name = competition_data.teams[0].name
        response = await client.get(
            "/players", params={"league_code": league_code, "team_name": team_name}
        )
        status_code = response.status_code
        assert status_code == 404
        content = response.json()
        assert content == {"detail": "Players Does Not Exists"}


class TestGetPlayersOfTeam:
    @pytest.mark.asyncio
    async def test_get_players_team_one_competition(
        self, client, db_session, build_one_competition_data
    ):
        competition_data = build_one_competition_data
        team_name = competition_data.teams[0].name
        response = await client.get("/players/team", params={"team_name": team_name})
        status_code = response.status_code
        assert status_code == 200
        content = response.json()
        assert len(content) == 5
        players_name = [player.name for player in competition_data.teams[0].players]
        for player in content:
            assert player["name"] in players_name

    @pytest.mark.asyncio
    async def test_get_players_team_ten_competition(
        self, client, db_session, build_ten_competition_data
    ):
        competition_data = build_ten_competition_data[0]
        team_name = competition_data.teams[0].name
        response = await client.get("/players/team", params={"team_name": team_name})
        status_code = response.status_code
        assert status_code == 200
        content = response.json()
        assert len(content) == 5
        players_name = [player.name for player in competition_data.teams[0].players]
        for player in content:
            assert player["name"] in players_name
