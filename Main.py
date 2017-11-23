import random, pygame, sys, time
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
main_Char = (pygame.image.load("idle.png").convert(),[0,0]) ##Character image being converted and set at position 0,0
main_char_speed = 2
enemy_char = (pygame.image.load("enemy.png").convert(),[0,2]) ##Enemy image being converted and set at position 0,2
enemy_char_speed = 3
fpsClock = pygame.time.Clock()

#Mouse location
mouse_loc = (0,0)

def move_char(delta): #Moves sprite towards mouse location
    x = (mouse_loc[0]-main_Char[1][0])*main_char_speed*delta
    y = (mouse_loc[1]-main_Char[1][1])*main_char_speed*delta
    main_Char[1][0] += x
    main_Char[1][1] += y

time1=0
while True:
    time2 = time1
    time1 = time.clock()
    delta = time1-time2 #sets delta time (time between frames)

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
character_shown = False
enemy_shown = False

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
            elif map_generated:
                character_shown = True
                enemy_shown = True
                window.blit(main_Char[0], main_Char[1])
                window.blit(enemy_char[0], enemy_char[1])
                pygame.display.flip()
            if pygame.mouse.get_pressed()[0]:  # Sets mouse location on mouse left click
                mouse_loc = pygame.mouse.get_pos()
                print mouse_loc

    pygame.display.update()
