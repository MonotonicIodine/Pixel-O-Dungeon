from entity import Entity
from weapon import Claws
import pygame as py

# class for enemy
class Enemy(Entity):

    # constructor for Enemy
    def __init__(self, position, image_path):
        super().__init__(position, image_path)
        self.image = py.image.load(self.image_path).convert_alpha() # change to _alpha
        self.enemy_rect = self.image.get_rect() # converts image for rectangle

        # enemy attributes
        self.movement_speed = 5
        self.hit_points = 50
        pass
    

    # Updates the location of the enemy rectangle location
    def update(self, dt):
        self.enemy_rect.x = self.position.x
        self.enemy_rect.y = self.position.y
        pass

    # draws enemy on display when called
    def draw(self, display):
        display.blit(self.image, self.position)

    # method to move enemy (currently unused until fixed)
    def move(self, movement_vector, dt):
        self.position.x += (movement_vector.x * self.movement_speed) * dt
        self.position.y += (movement_vector.y * self.movement_speed) * dt
        self.enemy_rect.x = self.position.x
        self.enemy_rect.y = self.position.y        

    # instance method to attack
    def attack(self, display):
        claws = Claws()# this is weird placement for claws constructor, there until tested w/ collisions
        display.blit(claws.image, (self.position.x + 40, self.position.y + 15))