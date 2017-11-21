import random, pygame, sys

pygame.init()

pygame.display.set_caption('Pillars')

textures = {
    'Dirt': pygame.image.load('Dirt.png'),
    'Grass': pygame.image.load('Grass.png'),
    'Sand': pygame.image.load('Sand.png'),
    'Stone': pygame.image.load('Stone.png'),
    'Water': pygame.image.load('Water.png')
}

TextureList = ['Dirt', 'Grass', 'Sand', 'Stone', 'Water']


TileSize = 64
X = 16
Y = 11
MapWidth = TileSize*X
MapLength = TileSize*Y


screen = pygame.display.set_mode((MapWidth, MapLength))

done = False


def tiles():
    for x in range(0,MapWidth, TileSize):
        for y in range(0,MapLength, TileSize):
            key = TextureList[random.randint(0, len(TextureList) - 1)]
            screen.blit(textures[key],(x,y))

tiles()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    pygame.display.update()