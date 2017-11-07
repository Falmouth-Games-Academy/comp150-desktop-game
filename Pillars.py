import pygame
import random
pygame.init()

MAINSCREEN = pygame.display.set_mode((800,600))


WaterTile = pygame.image.load("Water_Tile.png")
GrassTile = pygame.image.load("Grass_Tile.png")
DesertTile = pygame.image.load("Desert_Tile.png")
HillTile = pygame.image.load("Hill_Tile.png")
RandomTile = [HillTile, DesertTile, GrassTile, WaterTile]
RandomMap = random.choice(RandomTile)


GameCycle = True
while GameCycle:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameCycle = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            GameCycle = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            MAINSCREEN.blit(RandomMap, (400,200))

            pygame.display.flip()