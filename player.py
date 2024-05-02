import pygame as py
from weapon import Sword,Bow

#  class Player, will be the interactive entity for user to play
class Player():
    def __init__(self):
        self.image_path = "artwork/player/idle.png"
        self.image = py.image.load(self.image_path).convert_alpha() # _alpha for transparency
        self.player_rect = self.image.get_rect() # gets rectangle of player
        self.position = py.Vector2(400,600)

        # player attributes
        self.movement_speed = 5 
        self.hit_points = 35

        #image variables/paths for player
        self.status = 'idle'  # auto set to idle
        self.status_path = 'artwork/player/' + self.status + '.png'

        # guard clause to check if player has controller
        self.has_controller = False

        if py.joystick.get_count() > 0:
            py.joystick.init() # inits joystick controls
            self.joystick = py.joystick.Joystick(0)
            self.joystick.init()

            self.has_controller = True
        else:
            pass

    # movement controls + setting status for animation
    def input(self):

        # Only tested with Xbox controller
        # 0 is A, 1 is B, 2 is X, 3 is Y, 4 is LB, 5 is RB
        if self.has_controller == True:
            if self.joystick:
                joystick_x = self.joystick.get_axis(0)
                joystick_y = self.joystick.get_axis(1)
                sword_trigger = self.joystick.get_button(5)  # this RB button
                bow_trigger = self.joystick.get_button(4)  # this LB button

                if abs(joystick_x) > 0.1:
                    self.position.x += joystick_x * self.movement_speed
                    self.status = 'PlayerRight' if joystick_x > 0 else 'PlayerLeft'

                if abs(joystick_y) > 0.1:
                    self.position.y += joystick_y * self.movement_speed
                    self.status = 'PlayerDown' if joystick_y > 0 else 'PlayerUp'

                if sword_trigger:
                    self.status = 'PlayerSwordAttack'
                if bow_trigger:
                    self.status = 'PlayerBowAttack'


        # player movement controls
        # setting status for future image uses for direction of player
        keys = py.key.get_pressed()
        if keys[py.K_w] or keys[py.K_UP]:
            self.position.y -= self.movement_speed  # goes up
            self.status = 'PlayerUp'

        if keys[py.K_s] or keys[py.K_DOWN]:
            self.position.y += self.movement_speed # goes down
            self.status = 'PlayerDown'

        if keys[py.K_a] or keys[py.K_LEFT]:
            self.position.x -= self.movement_speed # goes left
            self.status = 'PlayerLeft'

        if keys[py.K_d] or keys[py.K_RIGHT]:
            self.position.x += self.movement_speed # goes right 
            self.status = 'PlayerRight'

        if keys[py.K_SPACE]:
            self.status = 'PlayerSwordAttack'

        if keys[py.K_q]:
            self.status = 'PlayerBowAttack'

        

    # status for animation
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


    # Updates the location of the player rectangle location
    def update(self, dt):
        self.player_rect.x = self.position.x # updating player rectangle location 
        self.player_rect.y = self.position.y # updating player rectangle location
        self.input() # input controls
        self.get_status() # gets status
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
