import pygame

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

class door(pygame.sprite.Sprite):
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


class Player_spawn_tile(pygame.sprite.Sprite):
    def __init__(self, current_pos_x, current_pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(current_pos_x, current_pos_y)

    def render(self, screen):
        player_image = pygame.image.load('map_tiles/floor_tile.png').convert_alpha()
        screen.blit(player_image, (self.pos.x, self.pos.y))


class Grav_Well(pygame.sprite.Sprite):
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

        self.i0 = pygame.image.load('map_tiles/laser_tile_on.png')
        self.i1 = pygame.image.load('map_tiles/laser_tile_off.png')
        self.timeTarget = 100
        self.timeNum = 0
        self.currentImage = 0

    def update(self, screen):
        self.timeNum += 1
        if (self.timeNum == self.timeTarget):
            if (self.currentImage == 0):
                self.currentImage += 1

            else:
                self.currentImage = 0
            self.timeNum = 0
        self.render(screen)


    def render(self, screen):
        if (self.currentImage == 0):
            screen.blit(self.i0, (self.pos.x, self.pos.y))
        else:
            screen.blit(self.i1, (self.pos.x, self.pos.y))
