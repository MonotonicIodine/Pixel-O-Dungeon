import pygame as py
from world import World
import random

py.init()

# display variables
width = 1000
height = 800
display = py.display.set_mode((width,height))
world = World(width, height)

clock = py.time.Clock()
running = True

dt = 0
fps = 60
# game loop
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                running = False


    # world updating display methods
    world.update(dt)
    world.draw(display)

    # updates display
    dt = clock.tick(fps) / 10
    py.display.update()
    