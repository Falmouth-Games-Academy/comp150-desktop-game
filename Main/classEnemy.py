"""

"""

import random
import math

from random import randint

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

def setSpawnPoints():
    spawnPointTest = (400,300)
    return spawnPointTest

def spawnEnemies():
    enemyStats = createEnemyStats(0,0,0,0,0)
    enemyHP = enemyStats[0]
    enemyStrength = enemyStats[1]
    enemyDexterity = enemyStats[2]
    enemyPerception = enemyStats[3]
    enemyConstitution = enemyStats[4]
    spawnLocation = setSpawnPoints()
    return spawnLocation
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

