from typing import List, Optional, Union
from presentation.inbound.entities.competition import AreaResponse
from pydantic import BaseModel


class PlayerResponse(BaseModel):
    id: int
    name: str
    position: str
    dateOfBirth: str
    nationality: str


class CompetitionTeamResponse(BaseModel):
    id: int
    name: str
    code: str
    areaName: str


class ContractResponse(BaseModel):
    start: str | None
    until: str | None


class CoachResponse(BaseModel):
    id: str | int | None
    firstName: str | None
    lastName: str | None
    dateOfBirth: str | None
    nationality: str | None
    contract: ContractResponse


class RunningCompetitionTeamResponse(BaseModel):
    id: int
    name: str
    code: str
    type: str
    emblem: Optional[str] = None


class TeamResponse(BaseModel):
    id: Union[int, str]
    name: str
    shortName: str
    tla: str
    crest: str
    address: str
    website: str
    founded: int
    clubColors: str
    venue: str
    lastUpdated: str
    coach: CoachResponse
    area: AreaResponse
    squad: List[PlayerResponse]
    staff: list
    runningCompetitions: List[RunningCompetitionTeamResponse]


class TeamRequest(BaseModel):
    football_uri: str
    x_api_token: str
    team_endpoint: str

    def get_request_dict(self, team_id: str) -> dict:
        return {
            "url": f"{self.football_uri}{self.team_endpoint}/{team_id}",
            "headers": {"X-Auth-Token": self.x_api_token},
        }
