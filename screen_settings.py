import pygame

"""
This File contains the Screen settings, from here you can adjust the screen dimensions,
this also modifies the map dimensions.
"""

# This code sets and creates the display window.
screen_height = 64 * 12
screen_width = 64 * 19
screen = pygame.display.set_mode((screen_width, screen_height))

# Gives a title/caption to the window of the game.
pygame.display.set_caption("Vision In The Dark DEMO BUILD")
