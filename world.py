import pygame as py
from player import Player
from enemy import Enemy
from map import Map
from gameover import GameOver

# class for world, is the main place where drawing to display happens
class World():

    # constructor taking in width and height for a display size
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.map = Map(py.Vector2(0,0), "artwork/map.png") # creates map
        self.game_over = GameOver(py.Vector2(0,0), "artwork/gameover.png")

        # instantiates player
        self.player = Player()
        
        # instantiates enemies
        self.enemy_1 = Enemy(py.Vector2(800,200), "artwork/evilbunny.png")
        self.enemy_2 = Enemy(py.Vector2(700,200), "artwork/evilbunny.png")
        self.enemy_3 = Enemy(py.Vector2(600,200), "artwork/evilbunny.png")
        self.enemy_4 = Enemy(py.Vector2(200,200), "artwork/evilbunny.png")
        self.enemy_5 = Enemy(py.Vector2(300,200), "artwork/evilbunny.png")
        self.enemy_6 = Enemy(py.Vector2(400,200), "artwork/evilbunny.png")
        self.enemies = [self.enemy_1, self.enemy_2, self.enemy_3, self.enemy_4, self.enemy_5, self.enemy_6]

    # updates the needed world methods
    def update(self, dt):
        self.player.update(dt) # updates player

        for enemy in self.enemies: # updates all enemies 
            enemy.update(dt)

        self.HitTesting() # testing for collisions between player and
        self.check_world_bounds()
        self.check_enemy_bounds()

    # method for drawing to display
    def draw(self, display):
        self.map.draw(display) # draws map
        self.player.draw(display) # draws player

        if self.player.status == 'PlayerSwordAttack':
            self.player.swing(display)
            self.player.status = 'PlayerIdle'

        if self.player.status == 'PlayerBowAttack':
            self.player.shoot(display)
            self.player.status = 'PlayerIdle'

        # draws all the enemies
        for enemy in self.enemies:
            enemy.draw(display)
        
        # checks if player has died AND then draws game over screen
        if self.player.hit_points <= 0:
            self.game_over.draw(display)

    # if instanced player rectangle collides with any enemy rect
    def HitTesting (self):
        for enemy in self.enemies:
            if self.player.player_rect.colliderect(enemy.enemy_rect):
                print("omg i hit with an enemy")
                self.player.hit_points -= 1

    # game over screen
    def GameOver(self,display):
            display.blit(py.image.load("artwork/gameover.png"), (0,0))

    def check_world_bounds(self):
        #bounds of player
        if self.player.position.x >= self.width - self.player.image.get_width():
            self.player.position.x = self.width - self.player.image.get_width()
        if self.player.position.x <= 0:
            self.player.position.x = 0
        if self.player.position.y >= self.height - self.player.image.get_height():
            self.player.position.y = self.height - self.player.image.get_height()
        if self.player.position.y <= 0:
            self.player.position.y = 0

    # bounds for enemies
    def check_enemy_bounds(self):
        for enemy in self.enemies:
            if enemy.position.x >= self.width - enemy.image.get_width():
                enemy.position.x = self.width - enemy.image.get_width()
            if enemy.position.x <= 0:
                enemy.position.x = 0
            if enemy.position.y >= self.height - enemy.image.get_height():
                enemy.position.y = self.height - enemy.image.get_height()
            if enemy.position.y <= 0:
                enemy.position.y = 0