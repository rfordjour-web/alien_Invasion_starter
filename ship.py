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
        self.image = pygame.transform.scale(self.image, 
                 (self.settings.ship_width, self.settings.ship_height)
                  )
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen.get_rect().midbottom
        

    def draw(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)