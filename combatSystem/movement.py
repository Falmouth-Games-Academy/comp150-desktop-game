#Imports
from __future__ import division
import pygame
import sys
import math
from pygame.locals import *
from spear import *
from enemy import *

"""
========================================================================================================================
Player Class
Define self
    sprite = ball
    x = 1
    y = 1
    angle = 0 degrees
    create rectangle around the sprite

Define draw
    detect change in mouse position and x 50 as a sensitivity modifier
    rotate a rectangle around the player to face the mouse
    rotate the player to be back in line with the rectangle
    transfer to screen

Define move_up / move_left / move_down / move_right
    moves the player across the screen whilst stopping them from going
    out of bounds and can reduce the speed by half which is used when
    the player is going diagonally to stop the speed boost.

========================================================================================================================
"""


class Player(object):
    def __init__(self):
        self.image = pygame.image.load('ball.png')
        self.sizeX = self.image.get_width()
        self.sizeY = self.image.get_height()
        self.x = 1
        self.y = 1
        self.angle = 0
        self.speed = 2
        self.rect = self.image.get_rect()
        self.enemies = []

    def draw(self, surface):
        rotImage = pygame.transform.rotate(self.image, self.angle)
        rotRect = rotImage.get_rect(center = self.rect.center)
        surface.blit(rotImage, (self.x + rotRect.x, self.y + rotRect.y))

    def moveUp(self, half):
        self.y = max(self.y - (self.speed / half), 0)

    def moveLeft(self, half):
        self.x = max(self.x - (self.speed / half), 0)

    def moveDown(self, half):
        self.y = min(self.y + (self.speed / half), screenY - self.sizeY)

    def moveRight(self, half):
        self.x = min(self.x + (self.speed / half), screenX - self.sizeX)

    def killEnemy(self, enemy):
        if self.enemies[enemy] is not None:
            for i in xrange(len(self.enemies)):
                self.enemies.remove(i)
                spear.enemies.remove(i)


pygame.init()
screenX, screenY = 800, 600
screen = pygame.display.set_mode((screenX, screenY))
objPlayer = Player()
objWeapon = spear(objPlayer)
objEnemy = Enemy()
objPlayer.enemies.append(objEnemy)
objWeapon.enemies.append(objEnemy)
clock = pygame.time.Clock()

hideCursor = True
cursorBindHeld = False
pygame.mouse.set_visible(not hideCursor) # Hide the cursor
pygame.event.set_grab(hideCursor) # Lock the cursor to the window

#while running
blnRunning = True
while blnRunning:

    for event in pygame.event.get():
        """
        ----------------------------------------------------------------------------------------------------------------
            When the mouse moves fetch the position and rotate the player to face it
        ----------------------------------------------------------------------------------------------------------------
        """
        if event.type == MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()

            # Base the mouse position off the centre of the screen
            mouseX -= (screenX / 2)
            mouseY -= (screenY / 2)

            # Workout the angle for the player to face
            angle = math.atan2(mouseY, mouseX) * 180 / math.pi
            objPlayer.angle = 270 - angle

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            objWeapon.attack()

        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # Toggle the cursor
            if event.key == pygame.K_ESCAPE:
                if hideCursor:
                    hideCursor = False
                else:
                    hideCursor = True
                pygame.event.set_grab(hideCursor)
                pygame.mouse.set_visible(not hideCursor)

    """
    --------------------------------------------------------------------------------------------------------------------
        When the keyboard is pressed (WASD), move the player
    --------------------------------------------------------------------------------------------------------------------
    """
    if pygame.key.get_focused():
        keys = pygame.key.get_pressed()

        # Check for diagonals
        half = 1
        if keys[K_w] and (keys[K_a] or keys[K_d]):
            half = 2
        if keys[K_s] and (keys[K_a] or keys[K_d]):
            half = 2

        # Move the player
        if keys[K_w]:
            objPlayer.moveUp(half)
        if keys[K_a]:
            objPlayer.moveLeft(half)
        if keys[K_s]:
            objPlayer.moveDown(half)
        if keys[K_d]:
            objPlayer.moveRight(half)

    screen.fill((255, 255, 255))

    for i in xrange(len(objPlayer.enemies)):
        objPlayer.enemies[i].draw(screen)

    objPlayer.draw(screen)
    objWeapon.draw(screen)
    pygame.display.update()
    clock.tick(40)