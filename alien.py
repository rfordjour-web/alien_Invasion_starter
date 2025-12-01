



import pygame
import sys
from settings import Settings
from alien_fleet import AlienFleet
from ship import Ship  # assuming you have a Ship class
from bullet import Bullet  # assuming you have a Bullet class

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.name)

        # Game elements
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alien_fleet = AlienFleet(self)

        # Clock for FPS control
        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            self._check_events()
            self._update_game()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    # ------------------------
    # Event handling
    # ------------------------
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)

    def _check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # ------------------------
    # Bullet firing
    # ------------------------
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    # ------------------------
    # Update all game elements
    # ------------------------
    def _update_game(self):
        self.ship.update()
        self._update_bullets()
        self.alien_fleet.update_fleet()

    def _update_bullets(self):
        self.bullets.update()

        # Remove bullets that have gone off screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for collisions with aliens
        collisions = self.alien_fleet.check_collisions(self.bullets)
        if collisions:
            for aliens_hit in collisions.values():
                for alien in aliens_hit:
                    self.alien_fleet.fleet.remove(alien)

    # ------------------------
    # Draw everything
    # ------------------------
    def _update_screen(self):
        self.screen.fill((30, 30, 30))  # background color

        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.alien_fleet.draw()

        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
