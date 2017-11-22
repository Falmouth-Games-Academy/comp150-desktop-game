import random, pygame, sys
pygame.init()
game_state = dict()

# Sets Window Name
pygame.display.set_caption('Pillars')

# Variables for the Window size
TileSize = 64
X_AXIS = 16
Y_AXIS = 11
MapWidth = TileSize*X_AXIS
MapLength = TileSize*Y_AXIS


# The variables for the Main Menu screen & displaying the main menu Img
window = pygame.display.set_mode((MapWidth, MapLength))
mainmenu_img = pygame.image.load('pillarsmenuscreen.jpg')
mainmenu_img = pygame.transform.scale(mainmenu_img, (MapWidth, MapLength))
controls_img = pygame.image.load('Controls.jpg')
controls_img = pygame.transform.scale(controls_img, (MapWidth, MapLength))
button1 = pygame.image.load('Button1.jpg')
button2 = pygame.image.load('Button2.jpg')
button3 = pygame.image.load('Button3.jpg')
window.blit(mainmenu_img, (0,0))
pygame.display.flip()
fpsClock = pygame.time.Clock()



# Variables for loading our tiles and arranging them into a list with a key
TileList = ['Dirt', 'Grass', 'Sand', 'Stone', 'Water']
key = TileList[random.randint(0, len(TileList) - 1)]
tiles = [
    pygame.image.load('Dirt.png'),
    pygame.image.load('Grass.png'),
    pygame.image.load('Sand.png'),
    pygame.image.load('Stone.png'),
    pygame.image.load('Water.png')
]

# Defining our tile generation method
def tile_gen():
    for x in range(0, MapWidth):
        for y in range(0, MapLength):
            window.blit(tiles[random.randint(0,4)],(x*64,y*64))

# Blitting the buttons
window.blit(button1, ((440, 250), (440, 380)))
window.blit(button2, ((440, 322), (440, 370)))
window.blit(button3, ((440, 400), (440, 440)))
pygame.display.flip()

control_shown = False
map_generated = False

done = False

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
                        window.blit(controls_img, (0, 0))
                        control_shown = True
                        pygame.display.flip()
            elif not map_generated:
                tile_gen()
                pygame.display.flip()
                map_generated = True


    idle = pygame.image.load("idle1.png"),
    runningframeone = pygame.image.load("running1.png")
    runningframetwo = pygame.image.load("running2.png")
    runningframethree = pygame.image.load("running3.png")
    runningframefour = pygame.image.load("running4.png")
    runningframefive = pygame.image.load("running5.png")
    runningframesix  = pygame.image.load("running6.png")







    pygame.display.update()
