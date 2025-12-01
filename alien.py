



import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """A class representing a single alien in the fleet."""

    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.settings = fleet.game.settings

        # Load and scale image
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_width, self.settings.alien_height)
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # ------------------------
    # Draw the alien
    # ------------------------
    def draw_alien(self):
        self.screen.blit(self.image, self.rect)

    # ------------------------
    # Check if alien is at screen edge
    # ------------------------
    def check_edges(self):
        return self.rect.right >= self.screen.get_rect().right or self.rect.left <= 0
