




import pygame
from typing import TYPE_CHECKING
from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """Manages the fleet of aliens, their movement, and collisions."""

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = 1  # 1 = right, -1 = left
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        # Create initial fleet
        self.create_fleet()

    # ------------------------
    # Create fleet
    # ------------------------
    def create_fleet(self):
        alien_width = self.settings.alien_width
        alien_height = self.settings.alien_height
        screen_width = self.settings.screen_width
        screen_height = self.settings.screen_height

        fleet_width, fleet_height = self.calculate_fleet_size(alien_width, screen_width, alien_height, screen_height)
        x_offset, y_offset = self.calculate_offset(alien_width, alien_height, screen_width, fleet_width, fleet_height)

        for row in range(fleet_height):
            for col in range(fleet_width):
                x = (alien_width + 20) * col + x_offset
                y = (alien_height + 20) * row + y_offset
                self._create_alien(x, y)

    def _create_alien(self, x, y):
        alien = Alien(self, x, y)
        self.fleet.add(alien)

    def calculate_fleet_size(self, alien_width, screen_width, alien_height, screen_height):
        fleet_width = max(3, (screen_width // (alien_width + 20)) - 2)
        fleet_height = max(2, (screen_height // 2) // (alien_height + 20))
        return fleet_width, fleet_height

    def calculate_offset(self, alien_width, alien_height, screen_width, fleet_width, fleet_height):
        fleet_horizontal_space = fleet_width * (alien_width + 20)
        x_offset = (screen_width - fleet_horizontal_space) // 2
        y_offset = 50
        return x_offset, y_offset

    # ------------------------
    # Update fleet position
    # ------------------------
    def update_fleet(self):
        self._check_fleet_edges()
        for alien in self.fleet:
            alien.rect.x += self.settings.fleet_speed * self.fleet_direction
            alien.rect.y += self.fleet_drop_speed * 0.3  # smooth downward movement

    def _check_fleet_edges(self):
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        for alien in self.fleet:
            alien.rect.y += self.fleet_drop_speed

    # ------------------------
    # Draw aliens
    # ------------------------
    def draw(self):
        for alien in self.fleet:
            alien.draw_alien()

    # ------------------------
    # Collision & bottom checks
    # ------------------------
    def check_collisions(self, other_group):
        return pygame.sprite.groupcollide(other_group, self.fleet, True, True)

    def check_fleet_bottom(self):
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_height:
                return True
        return False

    def check_destroyed_status(self):
        return not self.fleet
