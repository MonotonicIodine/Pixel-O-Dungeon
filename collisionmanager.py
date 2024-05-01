from entity import Entity
from player import Player
from enemy import Enemy

class CollisionHandler:
    def __init__(self, entity1, entity2):
        self.entity1 = entity1
        self.entity2 = entity2

