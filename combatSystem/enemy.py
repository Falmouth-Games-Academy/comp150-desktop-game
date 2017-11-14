import pygame

screenX, screenY = 800, 600

from spear import *

class Enemy():
    def __init__(self):
        self.image = pygame.image.load('ball.png')
        self.sizeX = self.image.get_width()
        self.sizeY = self.image.get_height()
        self.x = 250
        self.y = 250
        self.angle = 0
        self.speed = 2
        self.rect = self.image.get_rect()

    def draw(self, surface):
        rotImage = pygame.transform.rotate(self.image, self.angle)
        rotRect = rotImage.get_rect(center = self.rect.center)
        surface.blit(rotImage, (self.x + rotRect.x, self.y + rotRect.y))

    def move_up(self, half):
        self.y = max(self.y - (self.speed / half), 0)

    def move_left(self, half):
        self.x = max(self.x - (self.speed / half), 0)

    def move_down(self, half):
        self.y = min(self.y + (self.speed / half), screenY - self.sizeY)

    def move_right(self, half):
        self.x = min(self.x + (self.speed / half), screenX - self.sizeX)