"""
========================================================================================================================
Author: Connor Sean Rodgers
Program: Main & Movement
Purpose: The main class for the game including the movement code
========================================================================================================================
"""
#Imports
from __future__ import division
import pygame
import sys
import math
import time
import random
from random import randint
from pygame.locals import *
import classEnemy
import classSpawnPoint

"""
========================================================================================================================
Player Class
Define self
    sprite = player
    x = 300
    y = 400
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
# ----------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.image = pygame.image.load('player.png')
        self.sizeX = self.image.get_width()
        self.sizeY = self.image.get_height()
        self.x = 300
        self.y = 400
        self.angle = 0
        self.speed = 2
        self.rect = self.image.get_rect()
# ----------------------------------------------------------------------------------------------------------------------
    def draw(self, surface):
        rotImage = pygame.transform.rotate(self.image, (50 * self.angle))
        rotRect = rotImage.get_rect(center = self.rect.center)
        surface.blit(rotImage, (self.x + rotRect.x, self.y + rotRect.y))
        pygame.display.update()
# ----------------------------------------------------------------------------------------------------------------------
    def move_up(self, half):
        self.y = max(self.y - (self.speed / half), 0)
# ----------------------------------------------------------------------------------------------------------------------
    def move_left(self, half):
        self.x = max(self.x - (self.speed / half), 0)
# ----------------------------------------------------------------------------------------------------------------------
    def move_down(self, half):
        self.y = min(self.y + (self.speed / half), screenY - self.sizeY)
# ----------------------------------------------------------------------------------------------------------------------
    def move_right(self, half):
        self.x = min(self.x + (self.speed / half), screenX - self.sizeX)
# ----------------------------------------------------------------------------------------------------------------------
classEnemy.spawnEnemies()
"""
========================================================================================================================
Enemy Class
Define self
    sprite = ball
    x = 0
    y = 0
    angle = 0 degrees
    create rectangle around the sprite

Define draw
    detect change in mouse position and x 50 as a sensitivity modifier
    rotate a rectangle around the player to face the mouse
    rotate the player to be back in line with the rectangle
    transfer to screen

Define spawn
    Randomly select a spawn point that is predefined, these points are allong 3 sides of the screen and an enemy can
    spawn on any one of these 12 spawn points with an even chance

========================================================================================================================
"""
class Enemy(object):
    def __init__(self):
        self.image = pygame.image.load('ball.png')
        self.sizeX = self.image.get_width()
        self.sizeY = self.image.get_height()
        self.x = 0
        self.y = 0
        self.angle = 0
        self.speed = 2
        self.rect = self.image.get_rect()
# ----------------------------------------------------------------------------------------------------------------------
    def draw(self, surface):
        rotImage = pygame.transform.rotate(self.image, (1 * self.angle))
        rotRect = rotImage.get_rect(center = self.rect.center)
        self.angle = math.atan2((self.x - objPlayer.x), (self.y -  objPlayer.y))
        surface.blit(rotImage, (self.x + rotRect.x, self.y + rotRect.y))
        surface.blit(self.image, (self.x,self.y))
        pygame.display.update

# ----------------------------------------------------------------------------------------------------------------------
    def spawn(self):
        """
        Spawn function
         This function makes use of a random number seed to spawn an enemy in a random unoccupied location.
        """
        mustSpawn = True
        while mustSpawn == True:
            #print str(spawnPointsTop(0).x)
            side = randint(1,3) # calculate if the enemy will spawn along the top, bottom or flank
            print int(side)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if side == 1:
                print "a"
                #position = randint(1,4)#calculate which of the 4 points along the top will be used as the enemies
                                       #  spawn location
                position = randint(0,3)
                print str(spawnPointsTop[position].boolPointOccupied)
                if spawnPointsTop[position].boolPointOccupied == False:
                   # self.spawnPoint = spawnPointsTop[position]
                    self.x = spawnPointsTop[position].x
                    self.y = spawnPointsTop[position].y
                    print str(self.x)
                    print "(" + str(self.x) + "," + str(self.y) + ")"
                    spawnPointsTop[position].boolPointOccupied = True  # set spawn to occupied
                    mustSpawn = False
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            elif side == 2:
                print "b"
                position = randint(0, 3)
                print str(spawnPointsFlank[position].boolPointOccupied)
                if spawnPointsFlank[position].boolPointOccupied == False:
                    #self.spawnPoint = spawnPointsFlank[position]
                    self.x = spawnPointsFlank[position].x
                    self.y = spawnPointsFlank[position].y
                    print "(" + str(self.x) + "," + str(self.y) + ")"
                    spawnPointsTop[position].boolPointOccupied = True  # set spawn to occupied
                    mustSpawn = False

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            else:
                print "c"
                position = randint(0, 3)
                print str(spawnPointsBottom[position].boolPointOccupied)
                if spawnPointsBottom[position].boolPointOccupied == False:
                    #self.spawnPoint = spawnPointsBottom[position]
                    self.x = spawnPointsBottom[position].x
                    self.y = spawnPointsBottom[position].y
                    print str(self.x)
                    print "(" + str(self.x) + "," + str(self.y) + ")"
                    spawnPointsTop[position].boolPointOccupied = True  # set spawn to occupied
                    mustSpawn = False

# ----------------------------------------------------------------------------------------------------------------------
    def moveTowardsPlayer(self):
        if self.x > objPlayer.x:
            self.x -= 1
        elif self.x < objPlayer.x:
            self.x +=1
        else:
            self.x = self.x

        if self.y > objPlayer.y:
            self.y -= 1
        elif self.y < objPlayer.y:
            self.y +=1
        else:
            self.y = self.y
#=======================================================================================================================
pygame.init()
# ----------------------------------------------------------------------------------------------------------------------
screenX, screenY = 1000, 1000
screen = pygame.display.set_mode((screenX, screenY))#
# ----------------------------------------------------------------------------------------------------------------------
objPlayer = Player()
objEnemy = Enemy()
objEnemyii = Enemy()
# ----------------------------------------------------------------------------------------------------------------------
clock = pygame.time.Clock()
# ----------------------------------------------------------------------------------------------------------------------
pygame.mouse.set_visible(False) # Hide the cursor,
# ----------------------------------------------------------------------------------------------------------------------
blnRunning = True
spawnPointsTop = []
spawnPointsFlank = []
spawnPointsBottom = []
# ----------------------------------------------------------------------------------------------------------------------
spawnT1 = classSpawnPoint.spawnPoint()
spawnT2 = classSpawnPoint.spawnPoint()
spawnT3 = classSpawnPoint.spawnPoint()
spawnT4 = classSpawnPoint.spawnPoint()
spawnF1 = classSpawnPoint.spawnPoint()
spawnF2 = classSpawnPoint.spawnPoint()
spawnF3 = classSpawnPoint.spawnPoint()
spawnF4 = classSpawnPoint.spawnPoint()
spawnB1 = classSpawnPoint.spawnPoint()
spawnB2 = classSpawnPoint.spawnPoint()
spawnB3 = classSpawnPoint.spawnPoint()
spawnB4 = classSpawnPoint.spawnPoint()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
spawnT1.x = 0
spawnT2.x = 160
spawnT3.x = 360
spawnT4.x = 760
spawnF1.x = 800
spawnF2.x = 800
spawnF3.x = 800
spawnF4.x = 800
spawnB1.x = 0
spawnB2.x = 160
spawnB3.x = 360
spawnB4.x = 760
spawnT1.y = 0
spawnT2.y = 0
spawnT3.y = 0
spawnT4.y = 0
spawnF1.y = 0
spawnF2.y = 200
spawnF3.y = 400
spawnF4.y = 540
spawnB1.y = 600
spawnB2.y = 600
spawnB3.y = 600
spawnB4.y = 600
# ----------------------------------------------------------------------------------------------------------------------
spawnPointsTop = {
    0: spawnT1,
    1: spawnT2,
    2: spawnT3,
    3: spawnT4
}
# ----------------------------------------------------------------------------------------------------------------------
spawnPointsFlank = {
    0: spawnF1,
    1: spawnF2,
    2: spawnF3,
    3: spawnF4
}
# ----------------------------------------------------------------------------------------------------------------------
spawnPointsBottom = {
    0: spawnB1,
    1: spawnB2,
    2: spawnB3,
    3: spawnB4
}
# ----------------------------------------------------------------------------------------------------------------------
objEnemy.spawn()
objEnemyii.spawn()
# ======================================================================================================================
while blnRunning:

    for event in pygame.event.get():
        """
        ----------------------------------------------------------------------------------------------------------------
            When the mouse moves fetch the position and rotate the player to face it
        ----------------------------------------------------------------------------------------------------------------
        """
        if event.type == MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            objPlayer.angle = math.atan2((objPlayer.x - mouseX), (objPlayer.y - mouseY))

        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
    """
    --------------------------------------------------------------------------------------------------------------------
        When the keyboard is pressed (WASD), move the player
    --------------------------------------------------------------------------------------------------------------------
    """
    if pygame.key.get_focused():
        keys = pygame.key.get_pressed()

        # Check for diagonals
        half = 0
        if keys[K_w]:
            half = min(half + 1, 2)
        if keys[K_a]:
            half = min(half + 1, 2)
        if keys[K_s]:
            half = min(half + 1, 2)
        if keys[K_d]:
            half = min(half + 1, 2)

        # Move the player
        if keys[K_w]:
            objPlayer.move_up(half)

        if keys[K_a]:
            objPlayer.move_left(half)
        if keys[K_s]:
            objPlayer.move_down(half)
        if keys[K_d]:
            objPlayer.move_right(half)
    objEnemy.moveTowardsPlayer()
    objEnemyii.moveTowardsPlayer()
    screen.fill((255, 255, 255))
    objEnemy.draw(screen)
    objEnemyii.draw(screen)
    objPlayer.draw(screen)
    pygame.display.update()
    clock.tick(40)