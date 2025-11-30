




import pygame
from bullet import Bullet
from arsenal import ShipArsenal

class Ship:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_width, self.settings.ship_height))
        self.boundaries = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

        self.arsenal = ShipArsenal(game)

    def update(self):
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()
