import pygame
from bullet import Bullet

class Ship:
    def __init__(self, game):
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.arsenal = game.arsenal




    def update(self):

        self. _update_ship_movement()
        self.arsenal.update_bullets()


    def _update_ship_movement(self):
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x


    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()