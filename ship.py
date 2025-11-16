import pygame
from bullet import Bullet

class Ship:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Load original ship image
        self.image = pygame.image.load(self.settings.ship_file)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # For smooth movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Bullet cooldown
        self.last_shot = 0
        self.cooldown = 250  # ms

    def update(self):
        speed = self.settings.ship_speed

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += speed
        if self.moving_left and self.rect.left > 0:
            self.x -= speed
        if self.moving_up and self.rect.top > 0:
            self.y -= speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += speed

        self.rect.x = self.x
        self.rect.y = self.y

    def fire_bullet(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot >= self.cooldown:
            if len(self.game.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self.game)
                self.game.bullets.add(new_bullet)
                self.last_shot = now

    def draw(self):
        self.screen.blit(self.image, self.rect)
