import pygame
from screen_settings import *
from player_class import *
from map_genreator import *
from vision_mechanic import *

# initiate pygame
pygame.init()

# limiting the FPS with this fps clock
FPS = 60
fpsClock = pygame.time.Clock()

generate_a_map()
player = Player(generate_a_map.player_spawn_pos)
laser = Laser((128, 64))
toggle_state = False
global running
running = True
while running:
    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            generate_a_map()

        # toggle between vision
        if toggle_state == False and event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            toggle_state = True
            vision_mechanic(int(round(player.pos.x + 32)), int(round(player.pos.y + 32)))
        elif toggle_state == True and event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            toggle_state = False
            render_map()

    if not toggle_state:
        vision_mechanic(int(round(player.pos.x + 32)), int(round(player.pos.y + 32)))
    if toggle_state:
        render_map()

    # running core gameplay elements
    laser.update(screen)
    player.render(screen)
    player.player_movement(wall_list, grav_well_list)

    pygame.display.update()
    fpsClock.tick(FPS)
