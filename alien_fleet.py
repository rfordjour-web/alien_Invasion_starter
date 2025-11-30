





import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """Manage the fleet of aliens."""

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = 1
        self.fleet_drop_speed = self.settings.fleet_drop_speed

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

        self._create_rectangle_fleet(alien_width, alien_height, fleet_width, fleet_height, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_width, alien_height, fleet_width, fleet_height, x_offset, y_offset):
        for row in range(fleet_height):
            for column in range(fleet_width):
                current_x = (alien_width + 20) * column + x_offset
                current_y = (alien_height + 20) * row + y_offset
                self._create_alien(current_x, current_y)

    # ------------------------
    # Fleet size
    # ------------------------
    def calculate_fleet_size(self, alien_width, screen_width, alien_height, screen_height):
        fleet_width = (screen_width // (alien_width * 2)) - 2
        fleet_height = (screen_height // 2) // (alien_height * 2)

        fleet_width = max(3, fleet_width)   # minimum 3 aliens per row
        fleet_height = max(2, fleet_height) # minimum 2 rows

        return int(fleet_width), int(fleet_height)

    # ------------------------
    # Offsets
    # ------------------------
    def calculate_offset(self, alien_width, alien_height, screen_width, fleet_width, fleet_height):
        fleet_horizontal_space = fleet_width * (alien_width + 20)
        fleet_vertical_space = fleet_height * (alien_height + 20)
        x_offset = int((screen_width - fleet_horizontal_space) // 2)
        y_offset = 50
        return x_offset, y_offset

    # ------------------------
    # Create single alien
    # ------------------------
    def _create_alien(self, x, y):
        new_alien = Alien(self, x, y)
        self.fleet.add(new_alien)

    # ------------------------
    # Edge check & drop
    # ------------------------
    def _check_fleet_edges(self):
        for alien in self.fleet:
            if alien.check_edges():
                self.fleet_direction *= -1
                self._drop_alien_fleet()
                break

    def update_fleet(self):
        """Move fleet horizontally and gradually downward."""
        self._check_fleet_edges()
        for alien in self.fleet:
            alien.rect.x += self.settings.fleet_speed * self.fleet_direction
            alien.rect.y += self.fleet_drop_speed * 0.05  # smooth downward movement

    def _drop_alien_fleet(self):
        """Drop fleet slightly when hitting an edge."""
        for alien in self.fleet:
            alien.rect.y += self.fleet_drop_speed

    # ------------------------
    # Draw aliens
    # ------------------------
    def draw(self):
        for alien in self.fleet:
            alien.draw_alien()

    # ------------------------
    # Collisions & bottom check
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
