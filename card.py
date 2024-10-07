from abc import ABC


class Card(ABC):
    def __init__(self, name: str, description: str = ''):
        self.name: str = name
        self.description: str = description
