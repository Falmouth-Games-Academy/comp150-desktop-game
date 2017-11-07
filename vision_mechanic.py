from screen_settings import *
from player_class import *
from map_genreator import *


def vision_mechanic(player_x, player_y):
    vision_radius = 200
    display = (screen_width, screen_height)
    screen.blit(map_image, (0, 0))
    fog_of_war = pygame.Surface(display)
    pygame.draw.circle(fog_of_war, (0, 200, 0), (player_x, player_y), vision_radius, 0)
    fog_of_war.set_colorkey((0, 200, 0))
    screen.blit(fog_of_war, (0, 0))
