import pygame as py

# parent class enetity for subclasses to inherit
class Entity:

    # constructor
    def __init__(self, position, image_path):
        self.position = position
        self.image_path = image_path
        self.image = py.image.load(self.image_path).convert_alpha()

        self.hit_points = 1
        self.movement_speed = 0
        pass

    # nothing atm
    def update(self, dt):
        pass
    
    # draws entity on display when called
    def draw(self, display):
        display.blit(self.image, self.position)
