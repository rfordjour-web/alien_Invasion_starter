import pygame 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Ship:

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the ship and set its starting position."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_width, self.settings.ship_height)
        )

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's movement."""
        temp_speed = 5

        # Move right only if ship isn't at right edge
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += temp_speed

        # Move left only if ship isn't at left edge
        if self.moving_left and self.rect.left > 0:
            self.x -= temp_speed

        # Apply updated x-position to the rect
        self.rect.x = self.x

    def draw(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)