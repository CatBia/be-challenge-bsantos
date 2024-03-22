from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Competition:
    """
    Represents a competition in football.

    Attributes:
        name (str): The name of the competition.
        code (str): The code of the competition.
        areaName (str): The name of the area where the competition takes place.
    """

    name: str
    code: str
    areaName: str


@dataclass
class Team:
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


@dataclass
class Player:
    """
    Represents a football player.

    Attributes:
        name (str): The name of the player.
        position (str): The position of the player.
        dateOfBirth (date): The date of birth of the player.
        nationality (str): The nationality of the player.
    """

    name: str
    position: str
    dateOfBirth: date
    nationality: str


@dataclass
class Coach:
    """
    Represents a coach in the football application.

    Attributes:
        name (str): The name of the coach.
        dateOfBirth (date): The date of birth of the coach.
        nationality (str): The nationality of the coach.
    """

    name: str
    dateOfBirth: date
    nationality: str


class CompetitionResponseTranslator:
    competition: Competition
    teams: List[Team]
    players: List[Player]
    coaches: List[Coach]
