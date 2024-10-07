from combat import Combat
from card import Card
from hero import Hero
from heroes.finley import Finley
from heroes.illidan import Illidan
from minion import Minion


class Player:
    def __init__(
            self,
            opponent: 'Player',
            hero: Hero,
            board: [Minion],
            hand: [Card],
            health: int,
            armor: int,
            gold_spent: int,
            has_attack_priority: bool = False,
            beetles_active: bool = False,
            spore_active: bool = False,
            vigor_active: bool = False,
            elementals_played: int = 0,
            eternal_knights_died: int = 0,
            ancestral_automata_summoned: int = 0,
            undead_army: int = 0,
            pirates_played: int = 0,
            blood_gem_attack: int = 1,
            blood_gem_health: int = 1
    ):
        self.opponent = opponent
        self.hero = hero
        self.board = board
        self.hand = hand
        self.health = health
        self.armor = armor
        self.has_attack_priority = has_attack_priority
        self.gold_spent = gold_spent
        self.beetles_active = beetles_active
        self.spore_active = spore_active
        self.vigor_active = vigor_active
        self.elementals_played = elementals_played
        self.eternal_knights_died = eternal_knights_died
        self.ancestral_automata_summoned = ancestral_automata_summoned
        self.undead_army = undead_army
        self.pirates_played = pirates_played
        self.blood_gem_attack = blood_gem_attack
        self.blood_gem_health = blood_gem_health

        self.minions_died: int = 0
        self.minions_attacked: int = 0
        self.attack_queue: [Minion] = []

        self.is_illidan: bool = type(self.hero) is Illidan


