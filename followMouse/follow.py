#Imports
from __future__ import division
import pygame
import sys
import math
from pygame.locals import *

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

========================================================================================================================
"""

class Player(object):
    def __init__(self):
        self.image = pygame.image.load('ball.png')
        self.x = 1
        self.y = 1
        self.angle = 0
        self.rect = self.image.get_rect()

    def draw(self, surface):
        rotImage = pygame.transform.rotate(self.image, (50 * self.angle))
        rotRect = rotImage.get_rect(center = self.rect.center)
        self.x = (rotRect.x)
        self.y = (rotRect.y)
        surface.blit(rotImage, (self.x, self.y))
        pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((800,600))
objPlayer = Player()
clock = pygame.time.Clock()

#while running
blnRunning = True
while blnRunning:
    screen.fill((255,255,255))
    objPlayer.draw(screen)

    for event in pygame.event.get():
        """
        ----------------------------------------------------------------------------------------------------------------
            When the mouse moves fetch the position and rotate the player to face it
        ----------------------------------------------------------------------------------------------------------------
        """
        if event.type == MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            objPlayer.angle = math.atan2((objPlayer.x - mouseX), (objPlayer.y - mouseY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(40)