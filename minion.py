from card import Card
from minions.types import Type


class Minion(Card):
    def __init__(self, original_health: int, original_attack: int, tyype: Type):
        self.original_health: int = original_health
        self.original_attack: int = original_attack
        self.current_health: int = self.original_health
        self.current_attack: int = self.original_attack
        self.tyype: Type = tyype
        self.played: bool = False
