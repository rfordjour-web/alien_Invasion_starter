


import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class ShipArsenal:
    """Manage the ship's bullets."""

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Update bullets and remove off-screen ones."""
        self.arsenal.update()
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw all bullets on the screen."""
        for bullet in self.arsenal:
            bullet.draw_bullet()  # Fixed method name

    def fire_bullet(self):
        """Fire a bullet if under the allowed limit."""
        if len(self.arsenal) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            # Play laser sound safely
            try:
                pygame.mixer.Sound(self.settings.laser_sound).play()
            except Exception as e:
                print(f"Laser sound failed: {e}")
            return True
        return False
