import pygame
from pygame.locals import *
from screen_settings import *
from map_genreator import *
from map_objects_and_tiles import *

'''This defines the player class'''


class Player(pygame.sprite.Sprite):
    milliseconds = 100
    milliseconds_boost = 2000
    counter = 0
    max_vision_radius = 180
    vision_speed = 30

    def __init__(self, (current_pos_x, current_pos_y)):
        pygame.sprite.Sprite.__init__(self)

        self.dead = False
        self.win = False
        self.lose = False

        self.speed_h = 0
        self.speed_v = 0
        self.speed_limit = 5
        self.speed_increase = 0.2
        self.boost = False
        self.pos = Vector2(current_pos_x, current_pos_y)

        self.time_since_last_event_up = 0
        self.time_since_last_event_down = 0
        self.time_since_last_event_left = 0
        self.time_since_last_event_right = 0
        self.time_since_last_event_boost = 0

        self.clock_up = pygame.time.Clock()
        self.clock_down = pygame.time.Clock()
        self.clock_left = pygame.time.Clock()
        self.clock_right = pygame.time.Clock()
        self.clock_boost = pygame.time.Clock()

        # code for rendering the player
        self.player_image = pygame.image.load('image_files/spr_player.png')
        self.player_image_dead = pygame.image.load('image_files/spr_player_dead.png')
        self.boost_ui_image = pygame.image.load('image_files/boost.png')
        self.player_image_rect = pygame.Surface([32, 32])

        # this loads the win and lose images
        self.win_image = pygame.image.load('image_files/win.png')
        self.lose_image = pygame.image.load('image_files/lose.png')

        # this loads the thruster images, named based on movement direction
        self.thruster_up = pygame.image.load('image_files/thruster_up.png')
        self.thruster_down = pygame.image.load('image_files/thruster_down.png')
        self.thruster_left = pygame.image.load('image_files/thruster_left.png')
        self.thruster_right = pygame.image.load('image_files/thruster_right.png')

    def render(self, screen):
        self.rect = self.player_image_rect.get_rect()

        self.rect.center = (self.pos.x + 26, self.pos.y + 26)
        # boost UI element
        if self.boost:
            screen.blit(self.boost_ui_image, (screen_width / 2, screen_height - 64))

        if self.lose:
            screen.blit(self.lose_image, (screen_width / 3, screen_height / 3))

        if self.win:
            screen.blit(self.win_image, (screen_width / 3, screen_height / 3))

        if self.dead:
            screen.blit(self.player_image_dead, (self.pos.x, self.pos.y))
        else:
            screen.blit(self.player_image, (self.pos.x, self.pos.y))

        # this blits the thrusters onto the screen
        pressed_keys = pygame.key.get_pressed()
        if (pressed_keys[K_w] or pressed_keys[K_UP]) and not self.dead:
            screen.blit(self.thruster_up, (self.pos.x + 16, self.pos.y + 48))
        if (pressed_keys[K_s] or pressed_keys[K_DOWN]) and not self.dead:
            screen.blit(self.thruster_down, (self.pos.x + 16, self.pos.y - 32))
        if (pressed_keys[K_a] or pressed_keys[K_LEFT]) and not self.dead:
            screen.blit(self.thruster_left, (self.pos.x + 50, self.pos.y + 16))
        if (pressed_keys[K_d] or pressed_keys[K_RIGHT]) and not self.dead:
            screen.blit(self.thruster_right, (self.pos.x - 36, self.pos.y + 16))

    def vision_mechanic(self, Dtime):
        display_size = (screen_width, screen_height)
        darkness = pygame.Surface(display_size)
        screen.blit(darkness, (0, 0))
        vision_radius = 0

        if self.counter <= self.max_vision_radius:
            vision_radius = self.counter
        elif self.counter <= self.max_vision_radius * 2:
            vision_radius = 0
            self.counter = 0

        self.counter += self.vision_speed * Dtime

        pygame.draw.circle(darkness, (0, 0, 1), (int(self.pos.x + 25),
                                                 int(self.pos.y) + 25),
                           int(vision_radius))
        darkness.set_colorkey((0, 0, 1))
        screen.blit(map_image, (self.pos.x - 200 + 32, self.pos.y - 200 + 32),
                    (self.pos.x - 200 + 32, self.pos.y - 200 + 32, 400, 400))
        render_lasers()
        screen.blit(darkness, (0, 0))

    def player_movement(self, wall, grav_well, laser, win_tile):

        pressed_keys = pygame.key.get_pressed()

        self.dt_up = self.clock_up.tick()
        self.dt_down = self.clock_down.tick()
        self.dt_left = self.clock_left.tick()
        self.dt_right = self.clock_right.tick()
        self.dt_boost = self.clock_boost.tick()

        self.time_since_last_event_up += self.dt_up
        self.time_since_last_event_down += self.dt_down
        self.time_since_last_event_left += self.dt_left
        self.time_since_last_event_right += self.dt_right
        self.time_since_last_event_boost += self.dt_boost

        # when the player dies this If statement disables control over the player.
        if not self.dead:
            # movement up
            # clocks limit the number of events that take place when keys are pressed
            if self.time_since_last_event_up > self.milliseconds:
                if pressed_keys[K_w] or pressed_keys[K_UP]:
                    self.speed_v -= self.speed_increase
                    # reset clock
                    self.time_since_last_event_up = 0
                    # set an upward speed limit
            if (pressed_keys[K_LSHIFT] or pressed_keys[K_SPACE]) and \
                    (pressed_keys[K_w] or pressed_keys[K_UP]):
                self.speed_v -= self.boost
            if self.speed_v <= - self.speed_limit:
                self.speed_v = - self.speed_limit

            # movement down
            if self.time_since_last_event_down > self.milliseconds:
                if pressed_keys[K_s] or pressed_keys[K_DOWN]:
                    self.speed_v += self.speed_increase
                    self.time_since_last_event_down = 0
            if (pressed_keys[K_LSHIFT] or pressed_keys[K_SPACE]) and \
                    (pressed_keys[K_s] or pressed_keys[K_DOWN]):
                self.speed_v += self.boost
            if self.speed_v >= self.speed_limit:
                self.speed_v = self.speed_limit

            # movement left
            if self.time_since_last_event_left > self.milliseconds:
                if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                    self.speed_h -= self.speed_increase
                    self.time_since_last_event_left = 0
            if (pressed_keys[K_LSHIFT] or pressed_keys[K_SPACE]) and \
                    (pressed_keys[K_a] or pressed_keys[K_LEFT]):
                self.speed_h -= self.boost
            if self.speed_h <= - self.speed_limit:
                self.speed_h = - self.speed_limit

            # movement right
            if self.time_since_last_event_right > self.milliseconds:
                if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                    self.speed_h += self.speed_increase
                    self.time_since_last_event_right = 0
            if (pressed_keys[K_LSHIFT] or pressed_keys[K_SPACE]) and \
                    (pressed_keys[K_d] or pressed_keys[K_RIGHT]):
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
        if self.time_since_last_event_boost > self.milliseconds_boost:
            self.boost = 2
            self.boost = True

            if (pressed_keys[K_LSHIFT] or pressed_keys[K_SPACE]) and \
                    (pressed_keys[K_w] or pressed_keys[K_s] or
                     pressed_keys[K_a] or pressed_keys[K_d]):
                self.time_since_last_event_boost = 0
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
                # player explodes if he hits a wall at speed
                if self.speed_h > 3.5:
                    self.player_death()
                if self.speed_h < -3.5:
                    self.player_death()
                if self.speed_v > 3.5:
                    self.player_death()
                if self.speed_v < -3.5:
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
        slow_down_rate = 0.92
        collision_rect = self.rect
        collision_rect.left += self.speed_h
        collision_rect.right += self.speed_h
        collision_rect.top += self.speed_v
        collision_rect.bottom += self.speed_v
        for grav_well in grav_well_list:
            if collision_rect.colliderect(grav_well.rect):
                self.speed_h *= slow_down_rate
                self.speed_v *= slow_down_rate

    '''Winning tile collision function'''

    def collide_win_tile(self, win_tiles):
        # creates a temporary rect that moves where the player moves
        collision_rect = self.rect
        collision_rect.left += self.speed_h
        collision_rect.right += self.speed_h
        collision_rect.top += self.speed_v
        collision_rect.bottom += self.speed_v
        for win_tile in win_tiles:
            if collision_rect.colliderect(win_tile.rect) and not self.dead:
                self.win = True

    '''Laser collision function'''

    def collide_laser(self, lasers):
        # creates a temporary rect that moves where the player moves
        collision_rect = self.rect
        collision_rect.left += self.speed_h
        collision_rect.right += self.speed_h
        collision_rect.top += self.speed_v
        collision_rect.bottom += self.speed_v
        for laser in lasers:
            if collision_rect.colliderect(laser.rect):
                if laser.current_image == 0:
                    self.player_death()

    def player_death(self):
        self.dead = True
        self.lose = True
