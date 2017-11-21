import random, pygame, sys
pygame.init()
game_state = dict()

pygame.display.set_caption('Pillars')

##Variables for the Window size
TileSize = 64
XAXIS = 16
YAXIS = 11
MapWidth = TileSize*XAXIS
MapLength = TileSize*YAXIS


##Rest of the variables
window = pygame.display.set_mode((MapWidth, MapLength))
mainmenuimg = pygame.image.load('pillarsmenuscreen.jpg')
mainmenuimg = pygame.transform.scale(mainmenuimg, (MapWidth, MapLength))
controlsimg = pygame.image.load('Controls.jpg')
controlsimg = pygame.transform.scale(controlsimg, (MapWidth, MapLength))
button1 = pygame.image.load('Button1.jpg')
button2 = pygame.image.load('Button2.jpg')
button3 = pygame.image.load('Button3.jpg')
window.blit(mainmenuimg, (0,0))
pygame.display.flip()
TextureList = ['Dirt', 'Grass', 'Sand', 'Stone', 'Water']
done = False
key = TextureList[random.randint(0, len(TextureList) - 1)]
textures = [
    pygame.image.load('Dirt.png'),
    pygame.image.load('Grass.png'),
    pygame.image.load('Sand.png'),
    pygame.image.load('Stone.png'),
    pygame.image.load('Water.png')
]
def tiles():
    for x in range(0, MapWidth):
        for y in range(0, MapLength):
            window.blit(textures[random.randint(0,4)],(x*64,y*64))

#Blitting the buttons
window.blit(button1, ((440, 250), (440, 380)))
window.blit(button2, ((440, 322), (440, 370)))
window.blit(button3, ((440, 400), (440, 440)))
pygame.display.flip()

control_shown = False
map_generated = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not control_shown:
                if pygame.mouse.get_pos() >= (440, 250):
                    if pygame.mouse.get_pos() <= (536, 380):
                        window.blit(controlsimg, (0, 0))
                        control_shown = True
                        pygame.display.flip()
            elif not map_generated:
                tiles()
                pygame.display.flip()
                map_generated = True

    pygame.display.update()
