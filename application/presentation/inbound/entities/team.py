from dataclasses import dataclass
from typing import List, Optional
from presentation.inbound.entities.competition import AreaResponse


@dataclass
class PlayerResponse:
    id: int
    name: str
    position: str
    dateOfBirth: str
    nationality: str


@dataclass
class CompetitionTeamResponse:
    id: int
    name: str
    code: str
    areaName: str


@dataclass
class ContractResponse:
    start: str
    until: str


@dataclass
class CoachResponse:
    id: int
    firstName: str
    lastName: str
    dateOfBirth: str
    nationality: str
    contract: ContractResponse


@dataclass
class TeamResponse:
    id: int
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
    runningCompetitions: List[CompetitionTeamResponse]


@dataclass
class TeamRequest:
    football_uri: str
    x_api_token: str
    team_endpoint: str

    def get_request_dict(self, team_id: str) -> dict:
        return {
            "url": f"{self.football_uri}/{self.team_endpoint}/{team_id}",
            "headers": {"X-Auth-Token": self.x_api_token},
        }
