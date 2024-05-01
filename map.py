import pygame as py

# class for map
class Map():
    # constructor for Map object
    def __init__(self,position, image_path):
        self.image_path = image_path
        self.position = position
        self.image = py.image.load(self.image_path).convert_alpha()
        self.map_rect = self.image.get_rect()
        pass

    # draws map on display
    def draw(self, display):
        display.blit(self.image, self.position)
        pass

    # nothing atm 
    def update(self, dt):
        pass