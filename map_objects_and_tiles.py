import pygame
from player_class import *
Vector2 = pygame.math.Vector2


class Wall(pygame.sprite.Sprite):
    def __init__(self, (current_pos_x, current_pos_y)):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(current_pos_x, current_pos_y)
        self.image = pygame.Surface([64, 64])
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x + 32, self.pos.y + 32)

    def render(self, screen):
        wall_image = pygame.image.load('map_tiles/wall_tile.png').convert_alpha()
        screen.blit(wall_image, (self.pos.x, self.pos.y))


class Door(pygame.sprite.Sprite):
    list_of_sides = ["top", "bottom", "left", "right"]
    def __init__(self, (current_pos_x, current_pos_y), side_positions):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(current_pos_x, current_pos_y)
        self.image = pygame.Surface([64, 64])
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x + 32, self.pos.y + 32)
        self.sides_positions = list_of_sides

    def render(self, screen):
        wall_image = pygame.image.load('map_tiles/floor_tile.png').convert_alpha()
        screen.blit(wall_image, (self.pos.x, self.pos.y))


class Floor(pygame.sprite.Sprite):
    def __init__(self, current_pos_x, current_pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(current_pos_x, current_pos_y)

    def render(self, screen):
        floor_image = pygame.image.load('map_tiles/floor_tile.png').convert_alpha()
        screen.blit(floor_image, (self.pos.x, self.pos.y))


class PlayerSpawnTile(pygame.sprite.Sprite):
    def __init__(self, current_pos_x, current_pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(current_pos_x, current_pos_y)

    def render(self, screen):
        player_image = pygame.image.load('map_tiles/floor_tile.png').convert_alpha()
        screen.blit(player_image, (self.pos.x, self.pos.y))


class GravWell(pygame.sprite.Sprite):
    def __init__(self, (current_pos_x, current_pos_y)):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(current_pos_x, current_pos_y)
        self.image = pygame.Surface([64, 64])
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x + 32, self.pos.y + 32)

    def render(self, screen):
        grav_well_image = pygame.image.load('map_tiles/grav_well_tile.png').convert_alpha()
        screen.blit(grav_well_image, (self.pos.x, self.pos.y))


class Laser(pygame.sprite.Sprite):
    def __init__(self, (current_pos_x, current_pos_y)):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(current_pos_x, current_pos_y)
        self.image = pygame.Surface([8, 128])
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x + 4, self.pos.y + 64)

        self.image_0 = pygame.image.load('map_tiles/laser_tile_on.png')
        self.image_1 = pygame.image.load('map_tiles/laser_tile_off.png')
        self.time_target = 100
        self.time_num = 0
        self.current_image = 0

    def update(self, screen):
        self.time_num += 1
        if (self.time_num == self.time_target):
            if (self.current_image == 0):
                self.current_image += 1

            else:
                self.current_image = 0
            self.time_num = 0
        self.render(screen)


    def render(self, screen):

        if (self.current_image == 0):
            screen.blit(self.image_0, (self.pos.x, self.pos.y))
        else:
            screen.blit(self.image_1, (self.pos.x, self.pos.y))
