
import pygame
pygame.init()

x = y = 0
window = pygame.display.set_mode((800, 600))
mainmenuimg = pygame.image.load('pillarsmenuscreen.jpg')
mainmenuimg = pygame.transform.scale(mainmenuimg, (800, 600))
controlsimg = pygame.image.load('Controls.jpg')
controlsimg = pygame.transform.scale(controlsimg, (800, 600))
window.blit(mainmenuimg, (0,0))
pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEMOTION:
                print "mouse at (%d, %d)" % event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                window.blit(controlsimg, (0,0))
                pygame.display.flip()







