from dataclasses import dataclass
from typing import List
from pydantic import BaseModel


class PlayerData(BaseModel):
    """
    Represents a football player.

    Attributes:
        name (str): The name of the player.
        position (str): The position of the player.
        dateOfBirth (str): The date of birth of the player.
        nationality (str): Nationality of the player
    """

    name: str
    position: str
    dateOfBirth: str
    nationality: str


class CoachData(BaseModel):
    """
    Represents a football coach.

    Attributes:
        name (str): The name of the coach.
        dateOfBirth (str): The date of birth of the coach
        nationality (str): Nationality of the coach
    """

    name: str
    dateOfBirth: str
    nationality: str


class TeamData(BaseModel):
    """
    Represents a football team.

    Attributes:
        name (str): The name of the team.
        areaName (str): The area name of the team.
        shortName (str): The short name of the team.
        address (str): The address of the team.
    """

    name: str
    areaName: str
    shortName: str
    address: str
    players: List[PlayerData]
    coach: CoachData


class CompetitionData(BaseModel):
    """
    Represents a competition in football.

    Attributes:
        name (str): The name of the competition.
        code (str): The code of the competition.
        areaName (str): The name of the area where the competition takes place.
        teams(obj): The teamdata obj
    """

    name: str
    code: str
    areaName: str
    teams: List[TeamData]
