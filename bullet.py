






import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage a single bullet fired from the ship."""

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load laser image
        self.image = pygame.image.load(self.settings.bullet_file).convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_width, self.settings.bullet_height)
        )
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop

        # Float position for smooth movement
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw(self):
        """Draw the bullet with a fire trail."""
        # Fire glow trail
        glow_surface = pygame.Surface((self.rect.width*2, self.rect.height*2), pygame.SRCALPHA)
        pygame.draw.ellipse(glow_surface, (255, 200, 50, 100), glow_surface.get_rect())
        self.screen.blit(glow_surface, (self.rect.x - self.rect.width//2, self.rect.y - self.rect.height//2))

        # Draw the actual laser
        self.screen.blit(self.image, self.rect)
