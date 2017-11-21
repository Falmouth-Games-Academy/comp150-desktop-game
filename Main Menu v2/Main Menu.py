## Importing pygame and initializing
import pygame
pygame.init()
game_state = dict()

##Setting values, variables for the images with proper scaling as well as blitting the main menu
x = y = 0

##Variables for the Window and the various images that are used
window = pygame.display.set_mode((840, 700))
mainmenuimg = pygame.image.load('pillarsmenuscreen.jpg')
mainmenuimg = pygame.transform.scale(mainmenuimg, (840, 700))
controlsimg = pygame.image.load('Controls.jpg')
controlsimg = pygame.transform.scale(controlsimg, (840, 700))
button1 = pygame.image.load('Button1.jpg')
button2 = pygame.image.load('Button2.jpg')
button3 = pygame.image.load('Button3.jpg')
window.blit(mainmenuimg, (0,0))
pygame.display.flip()

#Blitting the buttons
window.blit(button1, ((370, 260), (424, 298)))
window.blit(button2, ((370, 330), (424, 367)))
window.blit(button3, ((370, 405), (424, 437)))
pygame.display.flip()

#Exit loop to run quit game when the ESC key is pressed as well as showing the controls on-screen
running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos() >= (370, 260):
                    if pygame.mouse.get_pos() <= (424, 298):
                        window.blit(controlsimg, (0, 0))
                        pygame.display.flip()
            elif event.type == pygame.MOUSEMOTION: ## Tracks mouse motion with co-ordinates
                print "mouse at (%d, %d)" % event.pos


