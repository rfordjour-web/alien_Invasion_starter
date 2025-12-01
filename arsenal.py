


import pygame
from bullet import Bullet

class ShipArsenal:

    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen

        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        self.arsenal.update()

        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        for bullet in self.arsenal:
            bullet.draw()

    def fire_bullet(self):
        if len(self.arsenal) < self.settings.bullets_allowed:
            bullet = Bullet(self.game)
            self.arsenal.add(bullet)

            try:
                pygame.mixer.Sound(self.settings.laser_sound).play()
            except:
                pass

            return True
        return False
