import pygame
pygame.init()

# create display
screen_width = 64 * 15
screen_height = 64 * 10
screen = pygame.display.set_mode((screen_width, screen_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False




    screen.fill((255, 255, 255))
    pygame.display.flip()

