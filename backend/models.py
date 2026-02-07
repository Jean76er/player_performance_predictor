from dataclasses import dataclass

@dataclass
class Player:
    nba_id: int
    name: str
    team: str
    positions: list #One player can play multiple positions