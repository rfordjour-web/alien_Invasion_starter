""""
Lab Name: Bullet.py
Author: Rosemond Fordjour
Purpose: manages the ship's bullets: creating them, 
updating their positions, drawing them, 
and enforcing the limit on how many can exist at once.
Date: November 30, 2025

"""






import pygame

class Bullet(pygame.sprite.Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) then move it to ship's position
        self.rect = pygame.Rect(
            0,
            0,
            self.settings.bullet_width,
            self.settings.bullet_height
        )

        # Start bullet at top of ship
        self.rect.midtop = game.ship.rect.midtop

        # Store bullet's vertical position as float
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
