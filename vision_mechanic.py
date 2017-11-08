from screen_settings import *
from player_class import *
from map_genreator import *


def vision_mechanic(player_x, player_y):
    '''
    #screen.blit(map_image, (0, 0))
    display_size = (screen_width, screen_height)
    vision_radius = 150
    darkness = pygame.Surface(display_size, pygame.SRCALPHA)
    darkness.fill((0,0,0))
    #screen.blit(darkness, (0, 0))
    m = 255/float(150)

    for i in range(150, 1, -1):
        pygame.draw.circle(darkness, (0, 0, 0, i*m), (player_x, player_y), vision_radius, i)
    return darkness
    '''

    vision_radius = 200
    display_size = (screen_width, screen_height)
    screen.blit(map_image, (0, 0))
    fog_of_war = pygame.Surface(display_size)
    pygame.draw.circle(fog_of_war, (0, 200, 0), (player_x, player_y), vision_radius, 0)
    fog_of_war.set_colorkey((0, 200, 0))
    screen.blit(fog_of_war, (0, 0))
