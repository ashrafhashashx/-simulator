from abc import ABC, abstractmethod

from combat import Combat
from player import Player


class Hero(ABC):
    def __init__(self, has_attack_priority: bool = False):
        self.has_attack_priority = has_attack_priority

    @abstractmethod
    def start_of_combat(self, me: Player, them: Player):
        pass


