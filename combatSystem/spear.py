import pygame
import math

class spear():
    def __init__(self, parent):
        self.image = pygame.image.load('spear.png')
        self.sizeX = self.image.get_width()
        self.sizeY = self.image.get_height()
        self.parent = parent
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(0, 0)
        self.enemies = []

        self.inAttack = False
        self.weaponReachProgress = 0
        self.weaponReachForwards = True
        self.weaponReach = 60
        self.weaponSpeed = 4

    def draw(self, surface):
        posX = self.parent.x + self.pos.x
        posY = self.parent.y + self.pos.y

        # Adjust in a direction +90 degrees to the direction pointed at
        posX += math.sin(math.radians(self.parent.angle + 90)) * 80
        posY += math.cos(math.radians(self.parent.angle + 90)) * 80

        # Check if collided
        if self.inAttack:
            if self.weaponReachForwards: # if weapon going forwards
                if self.weaponReachProgress >= self.weaponReach:
                    self.weaponReachForwards = False
                else:
                    # Collision check
                    tempX = posX - math.sin(math.radians(self.parent.angle)) * self.weaponReachProgress
                    tempY = posY - math.cos(math.radians(self.parent.angle)) * self.weaponReachProgress

                    # Debug
                    pygame.draw.rect(surface, (90, 150, 80), (tempX, tempY, 30, 30))

                    for i in xrange(self.weaponSpeed):
                        for enemy in xrange(len(self.enemies)):
                            pygame.draw.rect(surface, (255,0,0), (tempX + 40, tempY, self.sizeX, self.sizeY))
                            if pygame.Rect(tempX + 40, tempY, self.sizeX, self.sizeY).colliderect(
                                    pygame.Rect(self.enemies[enemy].x, self.enemies[enemy].y,
                                                self.enemies[enemy].sizeX, self.enemies[enemy].sizeY)):
                                self.weaponReachForwards = False
                                break
                            else:
                                tempX = posX - math.sin(math.radians(self.parent.angle)) * self.weaponReachProgress
                                tempY = posY - math.cos(math.radians(self.parent.angle)) * self.weaponReachProgress
                                self.weaponReachProgress = min(self.weaponReachProgress + 1, self.weaponReach)
            else:
                if self.weaponReachProgress <= 1:
                    self.inAttack = False
                    self.weaponReachForwards = True
                else:
                    self.weaponReachProgress = max(self.weaponReachProgress - self.weaponSpeed, 0)

            # Animation
            posX -= math.sin(math.radians(self.parent.angle)) * self.weaponReachProgress
            posY -= math.cos(math.radians(self.parent.angle)) * self.weaponReachProgress

        rotImage = pygame.transform.rotate(self.image, self.parent.angle)
        rotRect = rotImage.get_rect(center=self.parent.rect.center)
        surface.blit(rotImage, (posX + rotRect.x, posY + rotRect.y))

    def attack(self):
        if self.inAttack:
            return
        self.inAttack = True