import pygame

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

PINK = ((255,105,180))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

        screen.fill(PINK)
        pygame.display.flip()