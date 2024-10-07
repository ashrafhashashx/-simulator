from hero import Hero
from minion import Minion
from player import Player


class AlAkir(Hero):
    def start_of_combat(self, me: Player, them: Player):
        if me.board:
            first_minion: Minion = me.board[0]
            first_minion.divine_shield = True
            first_minion.taunt = True
            first_minion.windfury = True


