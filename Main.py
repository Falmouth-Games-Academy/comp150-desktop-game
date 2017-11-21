import random, pygame, sys

pygame.init()

pygame.display.set_caption('Pillars')

textures = {
    'Dirt' : pygame.image.load('Dirt.png'),
    'Grass' : pygame.image.load('Grass.png'),
    'Sand' : pygame.image.load('Sand.png'),
    'Stone' : pygame.image.load('Stone.png'),
    'Water' : pygame.image.load('Water.png')
}

TextureList = ['Dirt', 'Grass', 'Sand', 'Stone', 'Water']



jam = 64
crumpet = 16
butter = 11
delicious = jam*crumpet
questionable = jam*butter


screen = pygame.display.set_mode((delicious,questionable))

done = False

def tiles():
    for x in range(0,delicious, jam):
        for y in range(0,questionable, jam):
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