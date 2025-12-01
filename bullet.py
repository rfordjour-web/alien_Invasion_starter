






import pygame
from pygame.sprite import Sprite
from settings import Settings

class Bullet(Sprite):
    """A class to manage bullets fired by the ship."""

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Create a bullet rect at (0,0) then set correct position
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = game.ship.rect.midtop

        # Store bullet position as float for smooth movement
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to the screen."""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
