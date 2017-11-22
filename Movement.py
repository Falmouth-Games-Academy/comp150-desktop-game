import pygame
import math
import time

pygame.init()
screen = pygame.display.set_mode((300, 300))

ship_info = (pygame.image.load("sTAN.png").convert(),[0,0])
SHIP_SPEED = 2




mouse_loc = (0,0)


def move_ship(delta):
    x = (mouse_loc[0]-ship_info[1][0])*SHIP_SPEED*delta
    y = (mouse_loc[1]-ship_info[1][1])*SHIP_SPEED*delta
    ship_info[1][0] += x
    ship_info[1][1] += y


time1=0
while True:

    time2 = time1
    time1 = time.clock()
    delta = time1-time2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

        if pygame.mouse.get_pressed()[0]:
            mouse_loc = pygame.mouse.get_pos()
            print mouse_loc

    move_ship(delta)
    screen.fill((0, 0, 255))
    screen.blit(ship_info[0],ship_info[1])
    pygame.display.flip()
