
""""
Lab Name: Ship.py
Author:Rosemond Fordjour
Purpose:manages the player's ship, including its position, 
movement, drawing on the screen, 
and firing bullets.
Date: November 30, 2025



"""



import pygame
from arsenal import ShipArsenal

class Ship:
    def __init__(self, game):

        self.game = game
        self.settings = game.settings
        self.screen = game.screen

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_width, self.settings.ship_height)
        )

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

        self.arsenal = ShipArsenal(game)

    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed

        if self.moving_left:
            self.x -= self.settings.ship_speed

        self.x = max(0, min(
            self.settings.screen_width - self.rect.width,
            self.x
        ))

        self.rect.x = self.x

        self.arsenal.update_arsenal()

    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        self.arsenal.fire_bullet()
