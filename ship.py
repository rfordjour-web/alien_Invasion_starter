




import pygame
from arsenal import ShipArsenal

class Ship:
    """A class to manage the player ship."""

    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen

        # Load and scale ship image
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_width, self.settings.ship_height)
        )

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Store horizontal position as float for smooth movement
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        # Ship arsenal
        self.arsenal = ShipArsenal(game)

    def update(self):
        """Update ship position and bullets."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """Move ship left or right, clamp within screen bounds."""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Clamp to screen
        self.x = max(0, min(self.settings.screen_width - self.rect.width, self.x))
        self.rect.x = self.x

    def draw(self):
        """Draw the ship and bullets to the screen."""
        # Draw bullets first so they appear under the ship
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """Fire a bullet from the ship."""
        fired = self.arsenal.fire_bullet()
        if fired:
            print("Bullet fired!")  # debug
