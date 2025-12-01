




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

        self.fleet_direction = 1   # 1 = right, -1 = left
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        # NEW: counter for smooth downward movement
        self.drop_counter = 0  

        self.create_fleet()

    # ------------------------
    # Create fleet
    # ------------------------
    def create_fleet(self):
        alien_width = self.settings.alien_width
        alien_height = self.settings.alien_height
        screen_width = self.settings.screen_width
        screen_height = self.settings.screen_height

        fleet_width, fleet_height = self.calculate_fleet_size(
            alien_width, screen_width,
            alien_height, screen_height
        )

        x_offset, y_offset = self.calculate_offset(
            alien_width, alien_height,
            screen_width, fleet_width, fleet_height
        )

        for row in range(fleet_height):
            for col in range(fleet_width):
                x = (alien_width + 20) * col + x_offset
                y = (alien_height + 20) * row + y_offset
                self._create_alien(x, y)

    # ------------------------
    # Fleet size math
    # ------------------------
    def calculate_fleet_size(self, alien_width, screen_width,
                              alien_height, screen_height):

        fleet_width = max(3, (screen_width //
                              (alien_width + 20)) - 2)

        fleet_height = max(2, (screen_height // 2) //
                               (alien_height + 20))

        return fleet_width, fleet_height

    # ------------------------
    # Fleet offset
    # ------------------------
    def calculate_offset(self, alien_width, alien_height,
                          screen_width, fleet_width, fleet_height):

        fleet_horizontal_space = fleet_width * (alien_width + 20)
        x_offset = (screen_width - fleet_horizontal_space) // 2
        y_offset = 50

        return x_offset, y_offset

    # ------------------------
    # Create alien
    # ------------------------
    def _create_alien(self, x, y):
        alien = Alien(self, x, y)
        self.fleet.add(alien)

    # ------------------------
    # Handle edges
    # ------------------------
    def _check_fleet_edges(self):
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """Big step when hitting an edge"""
        for alien in self.fleet:
            alien.rect.y += self.fleet_drop_speed

    # ------------------------
    # ✅ UPDATED movement
    # ------------------------
    def update_fleet(self):
        """Smooth horizontal + SLOW vertical alien movement"""

        # Edge detection / turn-around
        self._check_fleet_edges()

        # Move horizontally EACH FRAME
        for alien in self.fleet:
            alien.rect.x += self.settings.fleet_speed * self.fleet_direction

        # Slowly move DOWN using frame counter
        self.drop_counter += 1

        drop_interval = 20      # Larger = slower downward movement
        drop_amount   = 0.4    # Smaller = smaller step

        if self.drop_counter % drop_interval == 0:
            for alien in self.fleet:
                alien.rect.y += drop_amount

    # ------------------------
    # Draw aliens
    # ------------------------
    def draw(self):
        for alien in self.fleet:
            alien.draw_alien()

    # ------------------------
    # Collision & bottom check
    # ------------------------
    def check_collisions(self, other_group):
        return pygame.sprite.groupcollide(
            other_group,
            self.fleet,
            True,
            True
        )

    def check_fleet_bottom(self):
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_height:
                return True
        return False

    def check_destroyed_status(self):
        return not self.fleet
