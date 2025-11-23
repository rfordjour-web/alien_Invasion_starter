




import pygame
from bullet import Bullet

class Ship:
    """Class to manage the player ship."""

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        # Load ship image
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_width, self.settings.ship_height)
        )

        # Get boundaries of screen
        self.boundaries = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Float position for smooth movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Create ship arsenal
        self.arsenal = game.ship_arsenal if hasattr(game, 'ship_arsenal') else None
        if self.arsenal is None:
            from arsenal import ShipArsenal
            self.arsenal = ShipArsenal(game)
            game.ship_arsenal = self.arsenal  # link to game

    def update(self):
        """Update ship position and bullets."""
        self._update_movement()
        self.arsenal.update_arsenal()

    def _update_movement(self):
        """Update ship position based on movement flags."""
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        """Draw ship and bullets on screen."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire_bullet(self):
        """Fire a bullet if under allowed limit."""
        return self.arsenal.fire_bullet()

