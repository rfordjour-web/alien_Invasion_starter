





import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from arsenal import ShipArsenal
from alien_fleet import AlienFleet
from time import sleep


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.starting_ship_count)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.name)

        self.running = True
        self.clock = pygame.time.Clock()

        # Initialize mixer and sounds
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(str(self.settings.impact_sound))
        self.impact_sound.set_volume(0.7)

        # ✅ Load alien drum sound
        self.alien_drums = 'Assets/alien_drums.wav'

        self.bullets = pygame.sprite.Group()
        self.ship = Ship(self, ShipArsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()
        self.game_active = True

    # ---------------------------------------------------------
    # 🇬🇭 GHANA FLAG BACKGROUND DRAWING FUNCTION
    # ---------------------------------------------------------
    def draw_ghana_background(self):
        screen_w = self.settings.screen_width
        screen_h = self.settings.screen_height
        stripe_h = screen_h // 3

        RED = (206, 17, 38)
        GOLD = (252, 209, 22)
        GREEN = (0, 122, 61)
        BLACK = (0, 0, 0)

        # Draw stripes
        pygame.draw.rect(self.screen, RED, (0, 0, screen_w, stripe_h))
        pygame.draw.rect(self.screen, GOLD, (0, stripe_h, screen_w, stripe_h))
        pygame.draw.rect(self.screen, GREEN, (0, stripe_h * 2, screen_w, stripe_h))

        # Draw black star centered
        star_size = stripe_h // 2
        center_x = screen_w // 2
        center_y = stripe_h + (stripe_h // 2)

        # 5-point star polygon
        star_points = [
            (center_x, center_y - star_size // 2),
            (center_x + star_size // 3, center_y - star_size // 8),
            (center_x + star_size // 2, center_y - star_size // 8),
            (center_x + star_size // 4, center_y + star_size // 6),
            (center_x + star_size // 3, center_y + star_size // 2),
            (center_x, center_y + star_size // 3),
            (center_x - star_size // 3, center_y + star_size // 2),
            (center_x - star_size // 4, center_y + star_size // 6),
            (center_x - star_size // 2, center_y - star_size // 8),
            (center_x - star_size // 3, center_y - star_size // 8),
        ]

        pygame.draw.polygon(self.screen, BLACK, star_points)

    # ---------------------------------------------------------
    # ✅ NEW: Play alien drum intro
    # ---------------------------------------------------------
    def play_alien_drums(self):
        pygame.mixer.music.load(self.alien_drums)
        pygame.mixer.music.play(-1)  # loop while aliens are on screen

    # ---------------------------------------------------------

    def run_game(self):
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
                self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()

        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()

        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()

    def _check_game_status(self):
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

    # ---------------------------------------------------------
    # ✅ Updated: Reset level and start alien drum
    # ---------------------------------------------------------
    def _reset_level(self):
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
        self.play_alien_drums()  # ← play drum intro for new aliens

    # ---------------------------------------------------------
    # UPDATED SCREEN DRAW — GHANA FLAG FIRST
    # ---------------------------------------------------------
    def _update_screen(self):
        self.draw_ghana_background()   # ← 🇬🇭 NEW BACKGROUND

        for bullet in self.bullets:
            bullet.draw()

        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()
    # ---------------------------------------------------------

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._keydown(event)

            elif event.type == pygame.KEYUP:
                self._keyup(event)

    def _keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.ship.fire_bullet()
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
