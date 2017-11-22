"""
========================================================================================================================
Author: Connor Sean Rodgers
Program: Enemy Class
Purpose: Blueprint for the enemies and the creation of these enemies
========================================================================================================================
"""

import random
import math
import pygame

from random import randint

# ----------------------------------------------------------------------------------------------------------------------
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
    """
    Draw function
    This function draws the enemy sprites including any rotations that have happened.
    """
    rotImage = pygame.transform.rotate(self.image, (1 * self.angle))
    rotRect = rotImage.get_rect(center=self.rect.center)
    surface.blit(rotImage, (self.x + rotRect.x, self.y + rotRect.y))
    surface.blit(self.image, (self.x, self.y))
    pygame.display.update
# ----------------------------------------------------------------------------------------------------------------------
def spawn(self):

    """
    Spawn function
     This function makes use of a random number seed to spawn an enemy in a random unoccupied location.
    """
    side = randint(1, 3) # Randomly decide if the enemy will be coming from the top, bottom or flank
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if side == 1: # Top
        position = randint(1, 4)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if position == 1:
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            if spawnT1.boolPointOccupied == False:
                self.spawnPoint = spawnT1
                self.x = spawnT1.x
                self.y = spawnT1.y
                print "Spawn Top 1"
                print "(" + str(self.x) + "," + str(self.y) + ")"
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            else:
                print""
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif position == 2:
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            if spawnT2.boolPointOccupied == False:
                self.spawnPoint = spawnT2
                self.x = spawnT2.x
                self.y = spawnT2.y
                print "Spawn Top 2"
                print "(" + str(self.x) + "," + str(self.y) + ")"
            else:
                print""
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif position == 3:
            if spawnT3.boolPointOccupied == False:
                self.spawnPoint = spawnT3
                self.x = spawnT3.x
                self.y = spawnT3.y
                print "Spawn Top 3"
                print "(" + str(self.x) + "," + str(self.y) + ")"
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            else:
                print""
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        else:
            if spawnT4.boolPointOccupied == False:
                self.spawnPoint = spawnT4
                self.x = spawnT4.x
                self.y = spawnT4.y
                print "Spawn Top 4"
                print "(" + str(self.x) + "," + str(self.y) + ")"
            else:
                print""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif side == 2: # Flank
        position = randint(1, 4)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if position == 1:
            if spawnF1.boolPointOccupied == False:
                self.spawnPoint = spawnF1
                self.x = spawnF1.x
                self.y = spawnF1.y
                print "Spawn Flank 1"
                print "(" + str(self.x) + "," + str(self.y) + ")"
            else:
                print""
 # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif position == 2:
            if spawnF2.boolPointOccupied == False:
                self.spawnPoint = spawnF2
                self.x = spawnF2.x
                self.y = spawnF2.y
                print "Spawn Flank 2"
                print "(" + str(self.x) + "," + str(self.y) + ")"
            else:
                print""
 # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif position == 3:
            if spawnF3.boolPointOccupied == False:
                self.spawnPoint = spawnF3
                self.x = spawnF3.x
                self.y = spawnF3.y
                print "Spawn Flank 3"
                print "(" + str(self.x) + "," + str(self.y) + ")"
            else:
                print""
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        else:
            if spawnF4.boolPointOccupied == False:
                self.spawnPoint = spawnF4
                self.x = spawnF4.x
                self.y = spawnF4.y
                print "Spawn Flank 4"
                print "(" + str(self.x) + "," + str(self.y) + ")"
            else:
                print""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else: # Bottom
        position = randint(1, 4)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if position == 1:
            if spawnB1.boolPointOccupied == False:
                self.spawnPoint = spawnB1
                self.x = spawnB1.x
                self.y = spawnB1.y
                print "Spawn Bottom 1"
                print "(" + str(self.x) + "," + str(self.y) + ")"
            else:
                print""
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif position == 2:
            if spawnB2.boolPointOccupied == False:
                self.spawnPoint = spawnB2
                self.x = spawnB2.x
                self.y = spawnB2.y
                print "Spawn Bottom 2"
                print "(" + str(self.x) + "," + str(self.y) + ")"
            else:
                print""
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif position == 3:
            if spawnB3.boolPointOccupied == False:
                self.spawnPoint = spawnB3
                self.x = spawnB3.x
                self.y = spawnB3.y
                print "Spawn Bottom 3"
                print "(" + str(self.x) + "," + str(self.y) + ")"
            else:
                print""
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        else:
            if spawnB4.boolPointOccupied == False:
                self.spawnPoint = spawnB4
                self.x = spawnB4.x
                self.y = spawnB4.y
                print "(" + str(self.x) + "," + str(self.y) + ")"
                print "Spawn Bottom 4"
            else:
                print""

# ----------------------------------------------------------------------------------------------------------------------
enemyHP = 0
enemyStrength = 0
enemyDexterity = 0
enemyPerception = 0
enemyConstitution = 0
diceFour = 0
diceSix = 0
diceTen = 0
diceHundred = 0
diceTwelve = 0
diceTwenty = 0
enemyStats = [enemyHP,enemyStrength,enemyDexterity,enemyPerception,enemyConstitution]
# ----------------------------------------------------------------------------------------------------------------------
def createEnemyStats(enemyHP,enemyStrength,enemyDexterity,enemyPerception,enemyConstitution):
    enemyCreationPoints = 36
    while (enemyCreationPoints > 0):
        diceFour = randint(1,4)
        if diceFour == 1:
            enemyStrength += 1
        elif diceFour == 2:
            enemyDexterity += 1
        elif diceFour == 3:
            enemyPerception += 1
        else:
            enemyConstitution += 1
        enemyCreationPoints -= 1
    print "Strength:" + str(enemyStrength)
    print "Dexterity:" + str(enemyDexterity)
    print "Perception:" + str(enemyPerception)
    print "Constitution:" + str(enemyConstitution)
    enemyHP = enemyConstitution * 10
    print "HP:" + str(enemyHP)
    enemyStats = [enemyHP, enemyStrength, enemyDexterity, enemyPerception, enemyConstitution]
    return enemyStats
# ----------------------------------------------------------------------------------------------------------------------
def setSpawnPoints():
    spawnPointTest = (400,300)
    return spawnPointTest
# ----------------------------------------------------------------------------------------------------------------------
def spawnEnemies():
    enemyStats = createEnemyStats(0,0,0,0,0)
    enemyHP = enemyStats[0]
    enemyStrength = enemyStats[1]
    enemyDexterity = enemyStats[2]
    enemyPerception = enemyStats[3]
    enemyConstitution = enemyStats[4]
    spawnLocation = setSpawnPoints()
    return spawnLocation
# ----------------------------------------------------------------------------------------------------------------------
spawnLocation = spawnEnemies()


# spawn
#   - no overlap
#   - off screen
#   - x spawn points of screen
#       - if spawn point 1 contins enemy{
#           - Generate list without spawn point 1
#           - Spawn enemy in random spawn point}
# moving
#   - move towards player
#   - cone of influence for steering behaviour
#       - look at direction that the collision is moving and make use of the vectors to rotate to avoid colision while
#           remaining on the same path
#           - line interception?
#               - polygon testing?
# attacking/defending
#   -D&D
# death
"""
for x in range (1...4){
    "spawnPointT" + x
}

"""
