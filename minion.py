from combat import Combat
from card import Card
from minions.types import Tribe
from player import Player


class Minion(Card):

    def __init__(
            self,
            owner: Player,
            name: str,
            original_health: int,
            original_attack: int,
            tribe: Tribe = None,
            health_buff_when_attacking: int = 0,
            attack_buff_when_attacking: int = 0,
            played: bool = True,
            divined_shield: bool = False,
            taunt: bool = False,
            reborn: bool = False,
            windfury: bool = False,
            invulnerable: bool = False,
            description: str = ''
    ):
        super().__init__(name, description)
        self.owner = owner
        self.original_health = original_health
        self.original_attack = original_attack
        self.tyype: Tribe = tribe
        self.current_health = self.original_health
        self.current_attack = self.original_attack
        self.health_buff_when_attacking = health_buff_when_attacking
        self.attack_buff_when_attacking = attack_buff_when_attacking
        self.played = played
        self.divine_shield = divined_shield
        self.taunt = taunt
        self.reborn = reborn
        self.windfury = windfury
        self.invulnerable = invulnerable

    def start_of_combat(self):
        pass

    def attack(self, target: 'Minion'):
        if self.current_attack == 0:
            return
        if target.invulnerable:
            pass

        if target.divine_shield:
            target.divine_shield = False
        target.current_health -= self.current_attack
        if self.divine_shield:
            self.divine_shield = False
        self.current_health -= target.current_attack

        if target.current_health < 1:
            target.die()
        if self.current_health < 1:
            self.die()
        self.owner.minions_attacked += 1

    def get_attacked(self):
        pass

    def die(self):
        self.owner.minions_died += 1
        self.trigger_deathrattle()

    def trigger_deathrattle(self):
        pass
