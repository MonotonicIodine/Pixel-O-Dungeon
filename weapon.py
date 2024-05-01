import pygame as py

# parent class 
class Weapon:

    # constructor for Weapon
    def __init__(self):
        self.position = py.Vector2(0,0)
        self.image_path = ''
        pass

    # draws weapon on display when called
    def draw(self, display):
        display.blit(self.image, self.position)
        pass
    
    # nothing atm
    def update(self, dt):
        pass


# baby class
class Sword(Weapon):

    # constructor for Sword
    def __init__(self):
        self.image_path = "artwork/sword.png"
        self.image = py.image.load(self.image_path).convert() # change to _alpha
        self.sword_image_rect = self.image.get_rect() # converts image for rectangle

        self.damage = 20
    pass


#baby class
class Bow(Weapon):
    # bow will not do anything rn
    # constructor for Bow
    def __init__(self):
        self.image_path = "artwork/bow.png"
        self.image = py.image.load(self.image_path).convert_alpha()
        self.damage = 0
    pass


class Claws(Weapon):
    
    # constructor for Claws
    def __init__(self):
        self.image_path = "artwork/player1.png"
        self.image = py.image.load(self.image_path).convert_alpha()
        self.damage = 10
    pass