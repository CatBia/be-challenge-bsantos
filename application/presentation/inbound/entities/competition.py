from typing import List, Optional
from pydantic import BaseModel


class CompetitionRequest(BaseModel):
    football_uri: str
    x_api_token: str
    competition_endpoint: str

    def get_request_dict(self, league_code: str) -> dict:
        return {
            "url": f"{self.football_uri}/{self.competition_endpoint}/{league_code}",
            "headers": {"X-Auth-Token": self.x_api_token},
        }


class AreaResponse(BaseModel):
    id: int
    name: str
    code: str
    flag: Optional[str]


class WinnerResponse(BaseModel):
    id: int
    name: str
    shortName: str
    tla: str
    crest: str
    address: str
    website: str
    founded: int
    clubColors: str
    venue: Optional[str] = None
    lastUpdated: str


class SeasonResponse(BaseModel):
    id: int
    startDate: str
    endDate: str
    currentMatchday: Optional[int]
    winner: WinnerResponse
    venue: Optional[str] = None


class CompetitionResponse(BaseModel):
    id: int
    name: str
    code: str
    type: str
    emblem: str
    currentSeason: SeasonResponse
    seasons: List[SeasonResponse]
    area: AreaResponse
    lastUpdated: str
