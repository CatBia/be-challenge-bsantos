from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CompetitionRequest:
    football_uri: str
    x_api_token: str
    competition_endpoint: str

    def get_request_dict(self, competition_id: str) -> dict:
        return {
            "url": f"{self.football_uri}/{self.competition_endpoint}/{competition_id}",
            "headers": {"X-Auth-Token": self.x_api_token},
        }


@dataclass
class AreaResponse:
    id: int
    name: str
    code: str
    flag: Optional[str]


@dataclass
class WinnerResponse:
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


@dataclass
class SeasonResponse:
    id: int
    startDate: str
    endDate: str
    currentMatchday: Optional[int]
    winner: WinnerResponse
    venue: Optional[str]
    lastUpdated: str


@dataclass
class CompetitionResponse:
    id: int
    name: str
    code: str
    type: str
    emblem: str
    currentSeason: SeasonResponse
    seasons: List[SeasonResponse]
    area: AreaResponse
    lastUpdated: str
