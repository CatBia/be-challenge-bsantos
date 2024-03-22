import pytest
from business_rules.services import league as league_service
import mock


class TestImportLeague:
    @pytest.mark.asyncio
    async def test_import_league_200_ok(self, client):
        """
        Test case to verify that the import_league function is called correctly.

        It calls the import_league function and asserts that it is called correctly.

        Args:
            self: The test case object.

        Returns:
            None
        """
        league_id = "any_id"
        mock_process_get_import_league = mock.AsyncMock()
        mock_process_get_import_league.return_value = "success"
        response = await client.get("/import-league", params={"league_id": league_id})
        status_code = response.status_code
        assert status_code == 200
        assert response.json() == {
            "status": "success",
            "message": "League imported successfully",
        }

    @pytest.mark.asyncio
    async def test_import_league_500_server_error(self, client):
        league_id = "any_id"
        mock_process_get_import_league = mock.AsyncMock(
            side_effect=Exception("Error importing league")
        )
        with mock.patch(
            "business_rules.services.league.process_get_import_league",
            mock_process_get_import_league,
        ):
            response = await client.get(
                "/import-league", params={"league_id": league_id}
            )
            status_code = response.status_code
            assert status_code == 500
            assert response.json() == {"detail": "Error importing league"}
