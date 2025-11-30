





import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """Manages the fleet of aliens."""

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    # ------------------------
    # Create the fleet of aliens
    # ------------------------
    def create_fleet(self):
        alien_width = self.settings.alien_width
        alien_height = self.settings.alien_height
        screen_width = self.settings.screen_width
        screen_height = self.settings.screen_height

        fleet_width, fleet_height = self.calculate_fleet_size(
            alien_width, screen_width, alien_height, screen_height
        )
        x_offset, y_offset = self.calculate_offset(
            alien_width, alien_height, screen_width, fleet_width, fleet_height
        )

        self._create_rectangle_fleet(alien_width, alien_height, fleet_width, fleet_height, x_offset, y_offset)

    # ------------------------
    # Create aliens in grid
    # ------------------------
    def _create_rectangle_fleet(self, alien_width, alien_height, fleet_width, fleet_height, x_offset, y_offset):
        for row in range(fleet_height):
            for column in range(fleet_width):
                # Skip every other column for spacing
                if column % 2 == 0:
                    continue
                current_x = alien_width * column + x_offset
                current_y = alien_height * row + y_offset
                self._create_alien(current_x, current_y)

    # ------------------------
    # Calculate fleet size based on difficulty
    # ------------------------
    def calculate_fleet_size(self, alien_width, screen_width, alien_height, screen_height):
        # Base counts
        base_width = screen_width // alien_width
        base_height = (screen_height // 2) // alien_height

        difficulty = getattr(self.settings, "difficulty", "medium").lower()

        if difficulty == "easy":
            fleet_width = max(3, base_width // 3)
            fleet_height = max(2, base_height // 3)
        elif difficulty == "medium":
            fleet_width = max(4, base_width // 2)
            fleet_height = max(3, base_height // 2)
        else:  # hard
            fleet_width = base_width - 2
            fleet_height = base_height - 2

        # Ensure odd numbers for spacing
        if fleet_width % 2 == 0:
            fleet_width -= 1
        if fleet_height % 2 == 0:
            fleet_height -= 1

        return int(fleet_width), int(fleet_height)

    # ------------------------
    # Calculate offsets to center fleet
    # ------------------------
    def calculate_offset(self, alien_width, alien_height, screen_width, fleet_width, fleet_height):
        half_screen = self.settings.screen_height // 2
        fleet_horizontal_space = fleet_width * alien_width
        fleet_vertical_space = fleet_height * alien_height
        x_offset = int((screen_width - fleet_horizontal_space) // 2)
        y_offset = int((half_screen - fleet_vertical_space) // 2)
        return x_offset, y_offset

    # ------------------------
    # Create single alien
    # ------------------------
    def _create_alien(self, x, y):
        new_alien = Alien(self, x, y)
        self.fleet.add(new_alien)

    # ------------------------
    # Update fleet
    # ------------------------
    def update_fleet(self):
        self._check_fleet_edges()
        self.fleet.update()

    # ------------------------
    # Check edges and drop
    # ------------------------
    def _check_fleet_edges(self):
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed
            alien.rect.y = alien.y

    # ------------------------
    # Draw aliens
    # ------------------------
    def draw(self):
        for alien in self.fleet:
            alien.draw_alien()

    # ------------------------
    # Collision checks
    # ------------------------
    def check_collisions(self, other_group):
        return pygame.sprite.groupcollide(other_group, self.fleet, True, True)

    # ------------------------
    # Check if fleet reached bottom
    # ------------------------
    def check_fleet_bottom(self):
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_height:
                return True
        return False

    # ------------------------
    # Check if fleet is destroyed
    # ------------------------
    def check_destroyed_status(self):
        return not self.fleet
