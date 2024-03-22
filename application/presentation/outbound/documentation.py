IMPORT_LEAGUE_DOCUMENTATION = {
    "title": "Import League",
    "description": "Import a league from football-data API",
    "responses": {
        200: {
            "description": "League imported successfully",
            "content": {
                "application/json": {
                    "example": {
                        "status": "success",
                        "message": "League imported successfully",
                    }
                }
            },
        },
        500: {
            "description": "Error importing league",
            "content": {
                "application/json": {
                    "example": {
                        "status": "error",
                        "message": "Error importing league",
                    }
                }
            },
        },
    },
}
