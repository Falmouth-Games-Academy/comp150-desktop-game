## Importing pygame and initializing
import pygame
pygame.init()


##Setting values, variables for the images with proper scaling as well as blitting the main menu
x = y = 0
window = pygame.display.set_mode((800, 600))
mainmenuimg = pygame.image.load('pillarsmenuscreen.jpg')
mainmenuimg = pygame.transform.scale(mainmenuimg, (800, 600))
controlsimg = pygame.image.load('Controls.jpg')
controlsimg = pygame.transform.scale(controlsimg, (800, 600))
window.blit(mainmenuimg, (0,0))
pygame.display.flip()


##Exit loop to run quit game when the ESC key is pressed as well as showing the controls on-screen
running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.MOUSEMOTION: ## Tracks mouse motion with co-ordinates
                print "mouse at (%d, %d)" % event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                window.blit(controlsimg, (0,0))
                pygame.display.flip()
