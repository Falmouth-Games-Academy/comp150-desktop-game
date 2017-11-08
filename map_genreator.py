import pygame
import random
import numpy
from map_objects_and_tiles import *
from screen_settings import *

Vector2 = pygame.math.Vector2
map_image = pygame.Surface((screen_width, screen_height))

wall_list = []
grav_well_list = []

# Creates a random map matrix with rules
def generate_a_map():
    pos_x = 0
    pos_y = 0

    map_matrix = numpy.random.randint(4, size=(screen_height / 64, screen_width / 64))
    player_spawn = False

    generate_a_map.list_of_wall_pos = []
    generate_a_map.list_of_grav_well_pos = []

    generate_a_map.player_spawn_pos = (0, 0)

    for row_num, row_list in enumerate(map_matrix):
        for tile_num in enumerate(row_list):

            tile_above = (row_num - 1, tile_num[0])
            tile_left = (row_num, tile_num[0] - 1)
            current_pos = (row_num, tile_num[0])

            # IF statement rules to apply to the map matrix
            if row_num == 0 or row_num == screen_height / 64 - 1 or tile_num[0] == 0 or tile_num[0] == screen_width / 64 -1:
                map_matrix.itemset(current_pos, 1)

            elif random.random() < 0.2 and map_matrix.item(tile_left) == 1:
                map_matrix.itemset(current_pos, 1)

            elif random.random() < 0.85 and tile_num[1] == 3:
                map_matrix.itemset(current_pos, 0)
                print "it worked"

            elif random.random() < 0.6 or (player_spawn == True and tile_num[1] == 2):
                map_matrix.itemset(current_pos, 0)

            elif random.random() < 0.3 and player_spawn == False:
                map_matrix.itemset(current_pos, 2)
                player_spawn = True

    print map_matrix

    del wall_list[:]
    del grav_well_list[:]

# Creates the map image from the map matrix
    for row_num, row_list in enumerate(map_matrix):
        for tile_num in enumerate(row_list):
            floor = Floor(pos_x, pos_y)
            player_tile = PlayerSpawnTile(pos_x, pos_y)

            if tile_num[1] == 1:
                generate_a_map.wall_pos = (pos_x, pos_y)
                wall = Wall(generate_a_map.wall_pos)
                wall.render(map_image)
                generate_a_map.list_of_wall_pos.append(generate_a_map.wall_pos)
                wall_list.append(wall)

            elif tile_num[1] == 2:
                player_tile.render(map_image)
                generate_a_map.player_spawn_pos = (pos_x, pos_y)

            elif tile_num[1] == 3:
                generate_a_map.grav_well_pos = (pos_x, pos_y)
                grav_well = GravWell(generate_a_map.grav_well_pos)
                grav_well.render(map_image)
                generate_a_map.list_of_grav_well_pos.append(generate_a_map.grav_well_pos)
                grav_well_list.append(grav_well)

            elif tile_num[1] == 0:
                floor.render(map_image)

            pos_x += 64
        pos_y += 64
        pos_x = 0


def render_map():
    screen.blit(map_image, (0, 0))
