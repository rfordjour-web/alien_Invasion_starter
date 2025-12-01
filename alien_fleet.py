




import pygame
from alien import Alien

class AlienFleet:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings

        self.fleet = pygame.sprite.Group()
        self.fleet_direction = 1

        self.create_fleet()

    def create_fleet(self):
        alien_width = self.settings.alien_width
        alien_height = self.settings.alien_height
        screen_width = self.settings.screen_width

        fleet_width = screen_width // (alien_width + 20) - 2
        fleet_height = 3

        x_offset = 100
        y_offset = 50

        for row in range(fleet_height):
            for col in range(fleet_width):
                x = (alien_width + 20) * col + x_offset
                y = (alien_height + 20) * row + y_offset
                self._create_alien(x, y)

    def _create_alien(self, x, y):
        alien = Alien(self, x, y)
        self.fleet.add(alien)

    def _check_edges(self):
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_fleet()
                self.fleet_direction *= -1
                break

    def _drop_fleet(self):
        for alien in self.fleet:
            alien.rect.y += self.settings.fleet_drop_speed

    def update_fleet(self):
        self._check_edges()

        for alien in self.fleet:
            alien.rect.x += self.settings.fleet_speed * self.fleet_direction

    def draw(self):
        for alien in self.fleet:
            alien.draw_alien()

    def check_fleet_bottom(self):
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_height:
                return True
        return False

    def check_destroyed_status(self):
        return not self.fleet
