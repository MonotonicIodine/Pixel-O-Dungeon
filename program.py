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

    keys = py.key.get_pressed()
    player_vector = py.Vector2(0,0)
    
    # movement controls
    if keys[py.K_w] or keys[py.K_UP]:
        player_vector.y -= 1 # goes up
    if keys[py.K_s] or keys[py.K_DOWN]:
        player_vector.y += 1 # goes down
    if keys[py.K_a] or keys[py.K_LEFT]:
        player_vector.x -= 1 # goes left
    if keys[py.K_d] or keys[py.K_RIGHT]:
        player_vector.x += 1 # goes right   
    

    # enemy movement, currently set to random
    # # plan to make it follow player
    # random_num = random.randint(-2, 1)
    # enemy_vector = py.Vector2(0,0)
    # if random_num == 1:
    #     enemy_vector.x += 1
    # if random_num == -1:
    #     enemy_vector.x -= 1
    # if random_num == -2:
    #     enemy_vector.y -= 1
    # if random_num == 0:
    #     enemy_vector.y += 1

    # world updating display methods
    #world.move_enemy(enemy_vector, dt)
    world.move_player(player_vector, dt)
    world.update(dt)
    world.draw(display)

    # weapon controls
    # spacebar controls sword
    # q controls bow
    if keys[py.K_SPACE]:
        world.player.swing(display)
        pass
    elif keys[py.K_q]:
        world.player.shoot(display)
        pass

    # enemy attack
    #world.enemy.attack(display) # just showing that enemy will attack


    # updates display
    dt = clock.tick(fps) / 10
    py.display.update()
    