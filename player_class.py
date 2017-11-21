import pygame
from pygame.locals import *
from screen_settings import *
from map_genreator import *

Vector2 = pygame.math.Vector2
#clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    speed_limit = 5
    milliseconds = 100
    milliseconds_boost = 2000
    dead = False

    def __init__(self, (current_pos_x, current_pos_y)):
        pygame.sprite.Sprite.__init__(self)

        self.dead = False
        self.win = False

        self.speed_h = 0
        self.speed_v = 0
        self.increase = 0.1
        self.boost = False
        self.pos = Vector2(current_pos_x, current_pos_y)

        self.time_elapsed_since_last_action_up = 0
        self.time_elapsed_since_last_action_down = 0
        self.time_elapsed_since_last_action_left = 0
        self.time_elapsed_since_last_action_right = 0
        self.time_elapsed_since_last_action_boost = 0

        self.clock_up = pygame.time.Clock()
        self.clock_down = pygame.time.Clock()
        self.clock_left = pygame.time.Clock()
        self.clock_right = pygame.time.Clock()
        self.clock_boost = pygame.time.Clock()

        self.dt_up = self.clock_up.tick()
        self.dt_down = self.clock_down.tick()
        self.dt_left = self.clock_left.tick()
        self.dt_right = self.clock_right.tick()
        self.dt_boost = self.clock_boost.tick()

        self.time_elapsed_since_last_action_up += self.dt_up
        self.time_elapsed_since_last_action_down += self.dt_down
        self.time_elapsed_since_last_action_left += self.dt_left
        self.time_elapsed_since_last_action_right += self.dt_right
        self.time_elapsed_since_last_action_boost += self.dt_boost

        self.player_image = pygame.image.load('spr_player.png').convert_alpha()
        self.player_image_dead = pygame.image.load('spr_player_dead.png').convert_alpha()
        self.boost_image = pygame.image.load('boost.png').convert_alpha()
        self.player_image_rect = pygame.Surface([32, 32])
        self.win_image = pygame.image.load('map_tiles/win.png').convert_alpha()
        


    def render(self, screen):

        self.rect = self.player_image_rect.get_rect()
        self.rect.center = (self.pos.x + 26, self.pos.y + 26)
        # boost UI element
        if self.boost == True:
            screen.blit(self.boost_image, (screen_width / 2 , screen_height - 64))

        if self.win == True:
            screen.blit(self.win_image, (screen_width / 3 , screen_height / 3))

        if self.dead == True:

            screen.blit(self.player_image_dead, (self.pos.x, self.pos.y))
        else:

            screen.blit(self.player_image, (self.pos.x, self.pos.y))

    def vision_mechanic(self):
        vision_radius = 200
        display_size = (screen_width, screen_height)
        screen.blit(map_image, (0, 0))
        fog_of_war = pygame.Surface(display_size)
        pygame.draw.circle(fog_of_war, (0, 200, 0), (int(round(self.pos.x + 32)), int(round(self.pos.y+32))), vision_radius, 0)
        fog_of_war.set_colorkey((0, 200, 0))
        screen.blit(fog_of_war, (0, 0))

    def player_movement(self, wall, grav_well, laser, win_tile):

        pressed_keys = pygame.key.get_pressed()

        self.dt_up = self.clock_up.tick()
        self.dt_down = self.clock_down.tick()
        self.dt_left = self.clock_left.tick()
        self.dt_right = self.clock_right.tick()
        self.dt_boost = self.clock_boost.tick()

        self.time_elapsed_since_last_action_up += self.dt_up
        self.time_elapsed_since_last_action_down += self.dt_down
        self.time_elapsed_since_last_action_left += self.dt_left
        self.time_elapsed_since_last_action_right += self.dt_right
        self.time_elapsed_since_last_action_boost += self.dt_boost

        # when the player dies this If statement disables control over the player.
        if self.dead == False:

            # movement up
            # clocks limit the number of events that take place when keys are pressed
            if self.time_elapsed_since_last_action_up > self.milliseconds:
                if pressed_keys[K_w] or pressed_keys[K_UP]:
                    self.speed_v -= self.increase
                    # reset clock
                    self.time_elapsed_since_last_action_up = 0
                    # set an upward speed limit
            if (pressed_keys[K_LSHIFT] or pressed_keys[K_SPACE]) and (pressed_keys[K_w] or pressed_keys[K_UP]):
                self.speed_v -= self.boost
            if self.speed_v <= - self.speed_limit:
                self.speed_v = - self.speed_limit

            # movement down
            if self.time_elapsed_since_last_action_down > self.milliseconds:
                if pressed_keys[K_s] or pressed_keys[K_DOWN]:
                    self.speed_v += self.increase
                    self.time_elapsed_since_last_action_down = 0
            if (pressed_keys[K_LSHIFT] or pressed_keys[K_SPACE]) and (pressed_keys[K_s] or pressed_keys[K_DOWN]):
                self.speed_v += self.boost
            if self.speed_v >= self.speed_limit:
                self.speed_v = self.speed_limit

            # movement left
            if self.time_elapsed_since_last_action_left > self.milliseconds:
                if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                    self.speed_h -= self.increase
                    self.time_elapsed_since_last_action_left = 0
            if (pressed_keys[K_LSHIFT] or pressed_keys[K_SPACE]) and (pressed_keys[K_a] or pressed_keys[K_LEFT]):
                self.speed_h -= self.boost
            if self.speed_h <= - self.speed_limit:
                self.speed_h = - self.speed_limit

            # movement right
            if self.time_elapsed_since_last_action_right > self.milliseconds:
                if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                    self.speed_h += self.increase
                    self.time_elapsed_since_last_action_right = 0
            if (pressed_keys[K_LSHIFT] or pressed_keys[K_SPACE]) and (pressed_keys[K_d] or pressed_keys[K_RIGHT]):
                self.speed_h += self.boost
            if self.speed_h >= self.speed_limit:
                self.speed_h = self.speed_limit

        # put collision func before player movement initialisation
        Player.collide_grav_well(self, grav_well)
        Player.collide_wall(self, wall)
        Player.collide_laser(self, laser)
        Player.collide_win_tile(self, win_tile)
        # initialize player movement
        self.pos.x += self.speed_h
        self.pos.y += self.speed_v

        # boost mechanic
        if self.time_elapsed_since_last_action_boost > self.milliseconds_boost:
            self.boost = 2
            self.boost = True

            if (pressed_keys[K_LSHIFT] or pressed_keys[K_SPACE]) and (pressed_keys[K_w] or pressed_keys[K_s] or pressed_keys[K_a] or pressed_keys[K_d]):
                self.time_elapsed_since_last_action_boost = 0
                self.boost = 0

    '''Wall collision function'''

    def collide_wall(self, wall_list):
        # creates a temporary rect that moves where the player moves
        collision_rect = self.rect
        collision_rect.left += self.speed_h
        collision_rect.right += self.speed_h
        collision_rect.top += self.speed_v
        collision_rect.bottom += self.speed_v
        for wall in wall_list:
            if collision_rect.colliderect(wall.rect):
                if self.speed_h > 4.0:
                    # can replace with explosion animation sound etc and level restart
                    self.player_death()
                    print "DEAD"
                if self.speed_h < -4.0:
                    print "DEAD"
                    self.player_death()
                if self.speed_v > 4.0:
                    print "DEAD"
                    self.player_death()
                if self.speed_v < -4.0:
                    print "DEAD"
                    self.player_death()

                # bounces player off of wall when colliding
                if self.rect.x < wall.rect.x:
                    self.speed_h = -(self.speed_h / 2)

                elif self.rect.x > wall.rect.x:
                    self.speed_h = -(self.speed_h / 2)

                if self.rect.y < wall.rect.y:
                    self.speed_v = -(self.speed_v / 2)

                elif self.rect.y > wall.rect.y:
                    self.speed_v = -(self.speed_v / 2)

    '''Gravity Well collision function'''

    def collide_grav_well(self, grav_well_list):
        # creates a temporary rect that moves where the player moves
        collision_rect = self.rect
        collision_rect.left += self.speed_h
        collision_rect.right += self.speed_h
        collision_rect.top += self.speed_v
        collision_rect.bottom += self.speed_v
        for grav_well in grav_well_list:
            if collision_rect.colliderect(grav_well.rect):
                self.speed_limit = 0.5
            else:
                self.speed_limit = 5.0


    def collide_win_tile(self, win_tile_list):
        # creates a temporary rect that moves where the player moves
        collision_rect = self.rect
        collision_rect.left += self.speed_h
        collision_rect.right += self.speed_h
        collision_rect.top += self.speed_v
        collision_rect.bottom += self.speed_v
        for win_tile in win_tile_list:
            if collision_rect.colliderect(win_tile.rect):
                print "PLAYER WINS!!!!"
                self.win = True

    '''Laser collision function'''

    def collide_laser(self, laser_list):
        # creates a temporary rect that moves where the player moves
        collision_rect = self.rect
        collision_rect.left += self.speed_h
        collision_rect.right += self.speed_h
        collision_rect.top += self.speed_v
        collision_rect.bottom += self.speed_v
        for laser in laser_list:
            if collision_rect.colliderect(laser.rect):
                if laser.current_image == 0:
                    self.player_death()


    def player_death(self):
        self.dead = True


