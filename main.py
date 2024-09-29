from board import Board
from card import Card
from minion import Minion
from spell import Spell

s = Spell()
m = Minion()
b = Board()
c = Card()
a = [s, m, 5, b, c]
for i in a:
    if issubclass(type(i), Card):
        print(str(type(i)))
