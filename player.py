import pygame as py
from weapon import Sword,Bow
from entity import Entity
from support import import_folder

#  class Player, will be the interactive entity for user to play
class Player(Entity):
    def __init__(self, position, image_path):
        super().__init__(position, image_path)

        self.image = py.image.load(self.image_path).convert_alpha() # change to _alpha
        self.player_rect = self.image.get_rect() # rectangle of player

        # player attributes
        self.movement_speed = 5 
        self.hit_points = 20

        #graphics for player
        self.status = 'idle'  # idle

        self.player_assets()

        pass

    def get_status(self):
        #idle 
        if self.position.x == 0 and self.position.y == 0:
            self.status = self.status + 'idle'
        #up
        if self.position.x == 0 and self.position.y < 0:
            self.status = self.status + 'PlayerUp'
        #down
        if self.position.x == 0 and self.position.y > 0:
            self.status = self.status + 'PlayerDown'
        #left
        if self.position.x < 0 and self.position.y == 0:
            self.status = self.status + 'PlayerLeft'
        #right
        if self.position.x > 0 and self.position.y == 0:
            self.status = self.status + 'PlayerRight'


    def player_assets(self):
        player_path = '../artwork/player'
                            #idle       #up         #down       #left       #right
        self.animations = {'idle': [], 'PlayerUp': [], 'PlayerDown': [], 'PlayerLeft': [], 'PlayerRight': []}
        for animation in self.animations.keys():
            full_path = player_path + '/' + animation        # ../artwork/player/PlayerUp   
            self.animations[animation] = import_folder(full_path)
        print(self.animations)

        pass

    # Updates the location of the player rectangle location
    def update(self, dt):
        self.player_rect.x = self.position.x
        self.player_rect.y = self.position.y
        self.get_status()
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
