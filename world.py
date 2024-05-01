import pygame as py
from player import Player
from enemy import Enemy
from map import Map
from EvilSpawner import EvilSpawner
from collisionmanager import CollisionHandler
from weapon import Sword

# class for world, is the main place where drawing to display happens
class World():

    # constructor taking in width and height for a display size
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = Map(py.Vector2(0,0), "artwork/map.png")
        self.player = Player(py.Vector2(self.width / 2, self.height / 2), "artwork/player.png")
        self.enemy_1 = Enemy(py.Vector2(800,200), "artwork/evilbunny.png")
        self.enemy_2 = Enemy(py.Vector2(700,200), "artwork/evilbunny.png")
        self.enemy_3 = Enemy(py.Vector2(600,200), "artwork/evilbunny.png")

        self.all_sprites = py.sprite.Group()
        #self.all_sprites.add(self.player)
        self.all_sprites.add(self.enemy_1)
        self.all_sprites.add(self.enemy_2)
        self.all_sprites.add(self.enemy_3)

    def update(self, dt):
        self.player.update(dt)
        self.enemy_1.update(dt)
        self.SwingedSword()

    def draw(self, display):
        self.map.draw(display)
        for entity in self.all_sprites:
            display.blit(entity.image, entity.position)
        # self.player.draw(display)
        # self.enemy_1.draw(display)
        self.check_world_bounds()
        self.check_enemy_bounds()


    def move_player(self, movement_vector, dt):
        self.player.move(movement_vector, dt)

    def move_enemy(self, movement_vector, dt):
        self.enemy_1.move(movement_vector, dt)

    
    # if instanced player swords rectangle collides with instanced enemy_1
    def SwingedSword (self):
        if self.player.player_sword.sword_image_rect.colliderect(self.enemy_1.enemy_rect):
            print("it worke")

        # if self.player.player_sword.sword_image_rect.colliderect(self.enemy_1):
        #     print("I HAVE HITTEN YOU WITH THINE SWORD")
        if self.player.player_rect.colliderect(self.enemy_1.enemy_rect):
            print("omg i hit with my body")

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

    def check_enemy_bounds(self):
        if self.enemy_1.position.x >= self.width - self.enemy_1.image.get_width():
            self.enemy_1.position.x = self.width - self.enemy_1.image.get_width()
        if self.enemy_1.position.x <= 0:
            self.enemy_1.position.x = 0
        if self.enemy_1.position.y >= self.height - self.enemy_1.image.get_height():
            self.enemy_1.position.y = self.height - self.enemy_1.image.get_height()
        if self.enemy_1.position.y <= 0:
            self.enemy_1.position.y = 0