import pygame as py
from weapon import Sword,Bow
from entity import Entity

#  class Player, will be the interactive entity for user to play
class Player(Entity):
    def __init__(self, position, image_path):
        super().__init__(position, image_path)

        self.image = py.image.load(self.image_path).convert() # change to _alpha
        self.player_rect = self.image.get_rect() # rectangle of player

        self.movement_speed = 5 
        self.hit_points = 50

        self.player_sword = Sword()


        pass

    # Updates the location of the player rectangle location
    def update(self, dt):
        self.player_rect.x = self.position.x
        self.player_rect.y = self.position.y
        pass

    # method to draw player on display when called
    def draw(self, display):
        display.blit(self.image, self.position)
    
    # method to move player given movement vector
    def move(self, movement_vector, dt):
        self.position.x += (movement_vector.x * self.movement_speed) * dt
        self.position.y += (movement_vector.y * self.movement_speed) * dt
    
    # method to draw sword
    def swing(self, display):
        self.player_sword = Sword() # this is weird placement for sword constructor, there until tested w/ collisions
        display.blit(self.player_sword.image, (self.position.x + 40, self.position.y + 15)) #hardcoded to be fitting
        pass

    # method to draw bow
    def shoot(self, display):
        bow = Bow() # this is weird placement for bow constructor, there until tested w/ collisions
        display.blit(bow.image, (self.position.x + 40, self.position.y + 10)) #hardcoded to be fitting
        pass
