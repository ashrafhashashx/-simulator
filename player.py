from board import Board
from hand import Hand
from hero import Hero


class Player:
    def __init__(self):
        self.hero: Hero
        self.board: Board
        self.hand: Hand
    
