from pydantic import BaseModel
from typing import Literal


class LeagueResponse(BaseModel):
    status: Literal["success", "error"]
    message: Literal["League imported successfully", "Error importing league"]
