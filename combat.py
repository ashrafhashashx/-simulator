import copy

from player import Player


class Combat:
    def __init__(self, me: Player, them: Player):
        self.me = copy.deepcopy(me)
        self.them = copy.deepcopy(them)

    def start(self, me, them) -> (float, float, float):
        pass
