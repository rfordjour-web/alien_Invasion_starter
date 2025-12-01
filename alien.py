"""
Lab Name: Alien Fleet
Author: Rosemond Fordjour
Purpose: manages the creation, movement, edge-checking, 
and drawing of all the aliens in the game.
Date: November 30, 2025
"""



import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, fleet, x, y):
        super().__init__()

        self.fleet = fleet
        self.settings = fleet.game.settings
        self.screen = fleet.game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_width, self.settings.alien_height)
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def check_edges(self):
        return self.rect.right >= self.boundaries.right or self.rect.left <= 0

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)
