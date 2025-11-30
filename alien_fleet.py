





import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """Create the fleet of aliens with fewer aliens per row and fewer rows."""
        for row in range(self.settings.alien_rows):
            for col in range(self.settings.aliens_per_row):
                x = 100 + col * (self.settings.alien_width + 20)
                y = 50 + row * (self.settings.alien_height + 20)
                self._create_alien(x, y)

    def _create_alien(self, x, y):
        alien = Alien(self, x, y)
        self.fleet.add(alien)

    def _check_fleet_edges(self):
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def update_fleet(self):
        self._check_fleet_edges()
        for alien in self.fleet:
            alien.rect.x += self.fleet_direction * self.settings.fleet_speed

    def _drop_alien_fleet(self):
        for alien in self.fleet:
            alien.rect.y += self.fleet_drop_speed

    def draw(self):
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        return pygame.sprite.groupcollide(other_group, self.fleet, True, True)

    def check_fleet_bottom(self):
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_height:
                return True
        return False

    def check_destroyed_status(self):
        return not self.fleet
