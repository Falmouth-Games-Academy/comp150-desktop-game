from player_class import *
from map_genreator import *
import time

'''
This is the Main file, this calls all the other game objects and functions
from the other python files to run the game.
The game needs to be run through this file.
'''

# initiate pygame
pygame.init()

# limiting the FPS with this fps clock
FPS = 60
fpsClock = pygame.time.Clock()

# generate a new map on launch of the game
generate_a_map()

# initialising the player
player = Player(generate_a_map.player_spawn_pos)

toggle_state = False

running = True
time1 = 0.00

# The main run loop
while running:
    time2 = time1
    time1 = time.clock()
    deltatime = time1 - time2
    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            generate_a_map()
            player = Player(generate_a_map.player_spawn_pos)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            generate_a_map()

        # toggle between vision
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            toggle_state = not toggle_state

    if not toggle_state:
        player.vision_mechanic(deltatime)
    else:
        render_map()
        render_lasers()

    player.render(screen)
    player.player_movement(wall_list, grav_well_list, laser_list, win_tile_list)

    pygame.display.update()
    fpsClock.tick(FPS)
