import pygame
from typing import TYPE_CHECKING
from bullet import Bullet


if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class ShipArsenal:
    """A class to manage the ship's arsenal."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the ship's arsenal."""
        self.game = game  
        self.settings = game.settings
        self.screen = game.screen
        self.arsenal = pygame.sprite.Group()


        def update_arsenal(self):        """Update the ship's arsenal."""
        self.arsenal.update()
        self.remove_bullets_offscreen()

        def _remove_bullets_offscreen(self):
            """Remove bullets that have moved off the screen."""
            for bullet in self.arsenal.copy():
                if bullet.rect.bottom <= 0:
                    self.arsenal.remove(bullet)




        def draw(self):        """Draw the ship's arsenal on the screen."""
        for bullet in  self.arsenal:
            bullet.draw(self.screen)

        def fire_bullet(self):
            if len(self.arsenal) < self.settings.bullets_amount:
                new_bullet = Bullet(self.game)
                self.arsenal.add(new_bullet)
                return True
            return False
        

    