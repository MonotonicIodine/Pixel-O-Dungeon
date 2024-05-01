from enemy import Enemy
import pygame as py

class EvilSpawner:
    def __init__(self, spawn_uses, position, image_path):
        self.spawn_uses = spawn_uses
        self.spawn_counter = 0
        self.position = position
        self.image_path = image_path
        self.image = py.image.load(self.image_path).convert_alpha()
        self.last_spawn_time = py.time.get_ticks()
        self.enemies = []  # store the enemies here

    def spawn(self, display):
        while self.spawn_uses != self.spawn_counter:
            entity_type = Enemy(py.Vector2(self.position), "artwork/evilbunny.png")
            display.blit(entity_type.image, entity_type.position)
            self.enemies.append(entity_type)  # store the enemy instance
            self.spawn_counter += 1
        pass

    def update(self, display):
        pass

    def draw(self, display):
        display.blit(self.image, self.position)

